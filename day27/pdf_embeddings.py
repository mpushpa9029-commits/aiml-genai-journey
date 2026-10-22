# Day 27 - PDF Chunks to Embeddings

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


# Create text chunks
chunk_size = 200

chunks = []

for i in range(0, len(all_text), chunk_size):
    chunk = all_text[i:i + chunk_size].strip()

    if chunk:
        chunks.append(chunk)


# Simple embedding function
def create_embedding(text):
    text = text.lower()

    vector = [
        text.count("python"),
        text.count("machine"),
        text.count("learning"),
        text.count("artificial"),
        text.count("intelligence"),
        text.count("data"),
        len(text.split())
    ]

    return vector


# Create embeddings for each chunk
vector_store = []

for number, chunk in enumerate(chunks, start=1):

    embedding = create_embedding(chunk)

    vector_store.append({
        "chunk_id": number,
        "text": chunk,
        "embedding": embedding
    })


# Display stored vectors
print("----- VECTOR STORE -----")

for item in vector_store:

    print(f"\nChunk ID: {item['chunk_id']}")
    print("Text:", item["text"])
    print("Embedding:", item["embedding"])


print("\nTotal Chunks:", len(vector_store))