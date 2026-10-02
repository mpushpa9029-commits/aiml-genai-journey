# Day 7 - Structured Prompting

def create_structured_prompt(role, task, context, constraints, output_format):
    prompt = f"""
Role: {role}

Task: {task}

Context: {context}

Constraints:
{constraints}

Output Format:
{output_format}
"""
    return prompt


prompt = create_structured_prompt(
    "AI Mentor",
    "Explain Machine Learning",
    "I am a beginner",
    "- Use simple English\n- Give 5 points\n- Give one example",
    "Bullet points"
)

print(prompt)