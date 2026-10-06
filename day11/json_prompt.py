# Day 11 - JSON Prompting and Structured Output

import json

prompt = """
Return the information in JSON format.

Topic: Machine Learning

Required fields:
- definition
- key_points
- example
"""

response = {
    "definition": "Machine Learning is a method where computers learn patterns from data.",
    "key_points": [
        "Learns from data",
        "Finds patterns",
        "Makes predictions"
    ],
    "example": "Email spam detection"
}

print("PROMPT:")
print(prompt)

print("\nSTRUCTURED OUTPUT:")
print(json.dumps(response, indent=4))