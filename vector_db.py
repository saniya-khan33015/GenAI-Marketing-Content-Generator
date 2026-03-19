import faiss
import numpy as np
import os

VECTOR_DB_PATH = "faiss_index.bin"
DIMENSION = 512


def embed_text(text):

    np.random.seed(abs(hash(text)) % (10**6))

    return np.random.rand(DIMENSION).astype("float32")


def create_index():

    return faiss.IndexFlatL2(DIMENSION)


def load_index():

    if os.path.exists(VECTOR_DB_PATH):

        return faiss.read_index(VECTOR_DB_PATH)

    return create_index()


def save_index(index):

    faiss.write_index(index, VECTOR_DB_PATH)


def retrieve_similar_examples(query_text, k=3):

    index = load_index()

    if index.ntotal == 0:

        return []

    query_vec = embed_text(query_text)

    D, I = index.search(np.expand_dims(query_vec, axis=0), k)

    return [f"Marketing Example {i}" for i in I[0]]