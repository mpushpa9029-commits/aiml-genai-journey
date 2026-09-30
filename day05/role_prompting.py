def create_prompt(role,task,constraints):
    prompt=f"""
    role:{role}
    task:{task}
    constraints:{constraints}
    """
    return prompt

prompt=create_prompt(
    "your my python mentor",
    "explain python functions at a beginner level",
    """
    1 use simple words,
    2 give one example also,
    3 give me simple short,
    """
)
print(prompt)
# Constraint Example

constraint_prompt = """
You are an AI/ML mentor.

Task:
Explain Machine Learning.

Constraints:
1. Use simple English.
2. Give only 3 points.
3. Give one real-world example.
"""

print("\n--- CONSTRAINT PROMPT ---")
print(constraint_prompt)