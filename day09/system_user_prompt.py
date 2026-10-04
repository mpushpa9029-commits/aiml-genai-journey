# Day 9 - System Prompt vs User Prompt

system_prompt = """
You are a Python Mentor.
Explain concepts in simple language.
Give practical examples.
"""

user_prompt = """
Explain Python functions to a beginner.
Give one simple example.
"""

final_prompt = f"""
SYSTEM INSTRUCTIONS:
{system_prompt}

USER REQUEST:
{user_prompt}
"""

print("----- SYSTEM PROMPT -----")
print(system_prompt)

print("----- USER PROMPT -----")
print(user_prompt)

print("----- FINAL PROMPT -----")
print(final_prompt)