# Day 21 - RAG Basics

documents = [
    "Python is a programming language used in AI, Machine Learning and web development.",
    "Machine Learning allows computers to learn patterns from data.",
    "RAG stands for Retrieval-Augmented Generation.",
    "RAG retrieves relevant information from external data before generating an answer."
]


def retrieve_information(question):
    question_words = question.lower().split()

    relevant_documents = []

    for document in documents:
        document_lower = document.lower()

        for word in question_words:
            if len(word) > 3 and word in document_lower:
                relevant_documents.append(document)
                break

    return relevant_documents


def create_rag_prompt(question, retrieved_documents):
    context = "\n".join(retrieved_documents)

    prompt = f"""
You are a helpful AI assistant.

Use the following context to answer the question.

Context:
{context}

Question:
{question}

Answer using only the provided context.
"""

    return prompt


question = "What is RAG?"

retrieved_documents = retrieve_information(question)

print("----- RETRIEVED INFORMATION -----")

for document in retrieved_documents:
    print(document)

final_prompt = create_rag_prompt(
    question,
    retrieved_documents
)

print("\n----- RAG PROMPT -----")
print(final_prompt)