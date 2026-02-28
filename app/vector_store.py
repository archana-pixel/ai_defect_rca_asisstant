import faiss
import numpy as np
import logging

class VectorStore:
    def __init__(self, dimension=1536):
        logging.info("Initializing FAISS index...")
        self.index = faiss.IndexFlatL2(dimension)
        self.logs = []

    def add(self, embedding, log_text):
        vector = np.array([embedding]).astype("float32")
        self.index.add(vector)
        self.logs.append(log_text)

    def search_similar(self, embedding, k=3):
        if self.index.ntotal == 0:
            return []

        query = np.array([embedding]).astype("float32")
        distances, indices = self.index.search(query, k)

        results = []
        for idx in indices[0]:
            if idx < len(self.logs):
                results.append(self.logs[idx])

        return results