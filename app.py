
from flask import Flask, render_template, request
from agents.extractor import ExtractorAgent
from agents.chunker import ChunkerAgent
from agents.summarizer import SummarizerAgent
from agents.combiner import CombinerAgent
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    final_summary = None

    if request.method == 'POST':
        pdf_file = request.files['pdf']
        path = os.path.join(app.config['UPLOAD_FOLDER'], pdf_file.filename)
        pdf_file.save(path)

        extractor = ExtractorAgent()
        chunker = ChunkerAgent()
        summarizer = SummarizerAgent()
        combiner = CombinerAgent()

        text = extractor.extract_text(path)
        chunks = chunker.chunk_text(text)
        summaries = [summarizer.summarize_chunk(chunk) for chunk in chunks]
        final_summary = combiner.combine_summaries(summaries)

    return render_template('index.html', summary=final_summary)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
