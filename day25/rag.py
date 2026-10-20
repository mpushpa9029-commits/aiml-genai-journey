# Day 25 - Basic RAG Pipeline

documents = [
    "Python is a high-level programming language used for software development.",
    "Machine Learning is a branch of AI that learns patterns from data.",
    "Deep Learning uses neural networks with multiple layers.",
    "Natural Language Processing helps computers understand human language.",
    "RAG combines information retrieval with language generation."
]


def retrieve_documents(query):
    query_words = query.lower().split()

    scored_documents = []

    for document in documents:
        document_words = document.lower().split()

        score = 0

        for word in query_words:
            if word in document_words:
                score += 1

        scored_documents.append((score, document))

    scored_documents.sort(reverse=True)

    return [
        document
        for score, document in scored_documents
        if score > 0
    ]


def generate_answer(query, context):
    if not context:
        return "I could not find relevant information."

    answer = f"""
Question: {query}

Relevant Information:
{context}

Answer:
Based on the retrieved information, the answer is available from the relevant context above.
"""

    return answer


# User question
query = "What is Machine Learning?"

# Step 1: Retrieve
retrieved_documents = retrieve_documents(query)

# Step 2: Create context
context = "\n".join(retrieved_documents)

# Step 3: Generate answer
answer = generate_answer(query, context)

print("----- BASIC RAG -----")
print(answer)