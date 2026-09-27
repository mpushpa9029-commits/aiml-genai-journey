# Day 3 - Prompt Engineering Basics

def create_prompt(role, task, context):
    prompt = f"""
Role: {role}
Task: {task}
Context: {context}
"""
    return prompt


prompt = create_prompt(
    "Python Mentor",
    "Explain Python functions",
    "I am a beginner"
)

print(prompt)
def create_prompt_with_format(role, task, context,output_format):
    prompt = f"""
    Role: {role}
    Task: {task}
    Context: {context}
    Output Format: {output_format}
    """
    return prompt

prompt_formatted = create_prompt_with_format(
    "Python Mentor",
    "Explain Python functions",
    "I am a beginner",
    "JSON"
)
print(prompt_formatted)
def few_shot_prompt():
    prompt = """
Example 1:
Question: What is Python?
Answer: Python is a programming language.

Example 2:
Question: What is AI?
Answer: AI is the ability of machines to perform intelligent tasks.

Now answer:
Question: What is Machine Learning?
"""
    return prompt


print(few_shot_prompt())