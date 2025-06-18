
class ChunkerAgent:
    def chunk_text(self, text, max_tokens=1000):
        words = text.split()
        chunks = []
        for i in range(0, len(words), max_tokens):
            chunk = " ".join(words[i:i + max_tokens])
            chunks.append(chunk)
        return chunks
