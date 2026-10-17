# Day 22 - Text Chunking

document = """
Machine Learning is a branch of Artificial Intelligence.
It allows computers to learn patterns from data.
Supervised learning uses labelled data for training.
Unsupervised learning finds patterns in data without labels.
Deep Learning uses neural networks with multiple layers.
RAG combines information retrieval with text generation.
It can be used for question answering over documents.
"""


def split_into_chunks(text, chunk_size):
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks


chunks = split_into_chunks(document, 20)

print("----- DOCUMENT CHUNKS -----")

for number, chunk in enumerate(chunks, start=1):
    print(f"\nChunk {number}:")
    print(chunk)

print("\nTotal Chunks:", len(chunks))