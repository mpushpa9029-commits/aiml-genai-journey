# Day 19 - Conversation History in Prompt

conversation_history = [
    {
        "role": "user",
        "message": "My favorite programming language is Python."
    },
    {
        "role": "assistant",
        "message": "That's great! Python is widely used in AI and Machine Learning."
    },
    {
        "role": "user",
        "message": "I am learning Generative AI."
    }
]


def create_prompt(history, new_question):
    prompt = "You are a helpful AI mentor.\n\n"
    prompt += "Conversation History:\n"

    for message in history:
        prompt += f"{message['role']}: {message['message']}\n"

    prompt += f"\nCurrent User Question:\n{new_question}\n"

    prompt += """
Answer the current question using the conversation history as context.
Use simple English.
"""

    return prompt


question = "What programming language am I learning?"

final_prompt = create_prompt(conversation_history, question)

print("----- FINAL PROMPT -----")
print(final_prompt)