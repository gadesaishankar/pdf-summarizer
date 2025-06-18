from openai import OpenAI

client = OpenAI(
    api_key="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",  # Replace with your real key
    base_url="https://api.groq.com/openai/v1"  # Groq's base endpoint
)

class SummarizerAgent:
    def summarize_chunk(self, chunk):
        try:
            response = client.chat.completions.create(
                model="llama3-70b-8192",
                messages=[
                    {"role": "system", "content": "You are a helpful summarizer."},
                    {"role": "user", "content": f"Summarize this: {chunk}"}
                ],
                temperature=0.5
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"❌ API Error: {e}")
            return "⚠️ Summary could not be generated due to server error. Please try again later."
