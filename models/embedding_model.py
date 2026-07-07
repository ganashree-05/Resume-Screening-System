"""
Sentence Embedding Model
"""

from sentence_transformers import SentenceTransformer


class EmbeddingModel:

    def __init__(self):
        print("Loading AI Model...")
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        print("Model Loaded Successfully!")

    def encode(self, text):
        return self.model.encode(text)