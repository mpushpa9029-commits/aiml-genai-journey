# Day 28 - Similarity Search

from PyPDF2 import PdfReader
import math


# PDF location
pdf_path = "day26/sample.pdf"


# Read PDF
reader = PdfReader(pdf_path)

all_text = ""

for page in reader.pages:
    text = page.extract_text()

    if text:
        all_text += text + "\n"


# Create chunks
chunk_size = 200

chunks = []

for i in range(0, len(all_text), chunk_size):
    chunk = all_text[i:i + chunk_size].strip()

    if chunk:
        chunks.append(chunk)


# Simple embedding function
def create_embedding(text):
    text = text.lower()

    return [
        text.count("python"),
        text.count("machine"),
        text.count("learning"),
        text.count("artificial"),
        text.count("intelligence"),
        text.count("data"),
        len(text.split())
    ]


# Cosine similarity
def cosine_similarity(vector_a, vector_b):

    dot_product = sum(
        a * b for a, b in zip(vector_a, vector_b)
    )

    magnitude_a = math.sqrt(
        sum(a * a for a in vector_a)
    )

    magnitude_b = math.sqrt(
        sum(b * b for b in vector_b)
    )

    if magnitude_a == 0 or magnitude_b == 0:
        return 0

    return dot_product / (
        magnitude_a * magnitude_b
    )


# Create vector store
vector_store = []

for number, chunk in enumerate(chunks, start=1):

    embedding = create_embedding(chunk)

    vector_store.append({
        "chunk_id": number,
        "text": chunk,
        "embedding": embedding
    })


# User question
query = "What is Machine Learning?"

query_embedding = create_embedding(query)


# Search relevant chunks
results = []

for item in vector_store:

    score = cosine_similarity(
        query_embedding,
        item["embedding"]
    )

    results.append({
        "chunk_id": item["chunk_id"],
        "text": item["text"],
        "score": score
    })


# Sort by similarity
results.sort(
    key=lambda item: item["score"],
    reverse=True
)


# Display results
print("----- USER QUERY -----")
print(query)

print("\n----- RETRIEVED CHUNKS -----")

for result in results:

    print(f"\nChunk ID: {result['chunk_id']}")
    print("Similarity:", round(result["score"], 3))
    print("Text:", result["text"])