from rag.loader import load_cv_text
from rag.embedder import embed_text
from rag.vector_store import VectorStore
from sentence_transformers import SentenceTransformer
import openai
import os

model = SentenceTransformer("all-MiniLM-L6-v2")

def split_text(text, chunk_size=300):
    words = text.split()
    return [
        " ".join(words[i:i+chunk_size])
        for i in range(0, len(words), chunk_size)
    ]

class CVRAG:
    def __init__(self):
        text = load_cv_text()
        self.chunks = split_text(text)
        self.embeddings = embed_text(self.chunks)
        self.store = VectorStore(self.embeddings)

    def ask(self, question):
        q_embedding = model.encode(question)
        idxs = self.store.search(q_embedding)

        context = "\n".join([self.chunks[i] for i in idxs])

        prompt = f"""
        Sadece aşağıdaki CV bilgilerine dayanarak cevap ver.
        Eğer bilgi yoksa "CV'de bu bilgi yer almıyor" de.

        CV:
        {context}

        Soru:
        {question}
        """

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content
