# Day 28 - Top-K Retrieval

## What is Retrieval?

Retrieval means finding relevant information from a collection of documents or text chunks.

In RAG, retrieval happens before the final answer is generated.

## What is Top-K Retrieval?

Top-K retrieval means selecting the K most relevant results from a collection.

For example:

K = 2

means that the system retrieves the top 2 most relevant results.

## Basic Flow

User Query
↓
Create Query Embedding
↓
Compare with Document Embeddings
↓
Calculate Similarity
↓
Sort Results
↓
Select Top-K
↓
Return Relevant Information

## Example

User Query:

"What is Machine Learning?"

The system compares the query with available documents.

The documents are ranked according to their similarity scores.

The top 2 results are selected as the most relevant information.

## Why Top-K is Useful

- Reduces unnecessary information.
- Provides only relevant results.
- Helps control the amount of context sent to an LLM.
- Makes retrieval more efficient.
- Is commonly used in RAG pipelines.

## RAG Connection

Documents
↓
Embeddings
↓
Vector Store
↓
User Query
↓
Query Embedding
↓
Similarity Search
↓
Top-K Relevant Chunks
↓
LLM
↓
Final Answer

## Python Concepts Used

- Functions
- Lists
- Dictionaries
- Loops
- Sorting
- Lambda functions
- List slicing
- Cosine similarity

## Day 28 Practice

- Created a collection of documents.
- Converted documents into simple vectors.
- Converted a user query into a vector.
- Calculated similarity scores.
- Sorted the results.
- Retrieved the top-K relevant documents.

## Important Note

This is a simplified educational implementation.

The embedding function is manually created for learning.

Real RAG applications use trained embedding models and vector databases.

## Learning Outcome

Understood how Top-K retrieval selects the most relevant information from a collection of documents using similarity scores.