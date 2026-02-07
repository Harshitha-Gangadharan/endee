from sentence_transformers import SentenceTransformer

class LocalEmbedder:
    def __init__(self):
        # 384 dimensions, runs fast on i5 CPU
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def generate_vector(self, text: str):
        return self.model.encode(text).tolist()