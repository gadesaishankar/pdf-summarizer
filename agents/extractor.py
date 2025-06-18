
import PyPDF2

class ExtractorAgent:
    def extract_text(self, pdf_file_path):
        text = ""
        with open(pdf_file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() or ""
        return text
