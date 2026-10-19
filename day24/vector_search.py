# Day 24 - Vector Search Basics

import math


documents = [
    "Python is a programming language.",
    "Python is widely used in Machine Learning.",
    "Machine Learning learns patterns from data.",
    "Deep Learning uses neural networks.",
    "Cricket is a popular sport in India."
]


def create_vector(text):
    text = text.lower()

    return [
        text.count("python"),
        text.count("machine"),
        text.count("learning"),
        text.count("deep"),
        text.count("cricket"),
        len(text.split())
    ]


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

    return dot_product / (magnitude_a * magnitude_b)


# Create vectors for documents
document_vectors = []

for document in documents:
    vector = create_vector(document)

    document_vectors.append({
        "text": document,
        "vector": vector
    })


# User query
query = "Python Machine Learning"

query_vector = create_vector(query)

print("----- QUERY -----")
print(query)

print("\n----- SEARCH RESULTS -----")

results = []

for item in document_vectors:

    similarity = cosine_similarity(
        query_vector,
        item["vector"]
    )

    results.append({
        "text": item["text"],
        "similarity": similarity
    })


# Sort by similarity
results.sort(
    key=lambda item: item["similarity"],
    reverse=True
)


# Display results
for number, result in enumerate(results, start=1):

    print(f"\n{number}. {result['text']}")
    print("Similarity:", round(result["similarity"], 3))