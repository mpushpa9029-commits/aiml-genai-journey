import tiktoken

text = "I am learning Generative AI"

encoding = tiktoken.get_encoding("cl100k_base")

tokens = encoding.encode(text)

print("Text:", text)
print("Tokens:", tokens)
print("Number of tokens:", len(tokens))