# Day 17 - Conversation Memory

conversation_history = []


def chat(user_message):
    # Store the user's message
    conversation_history.append({
        "role": "user",
        "message": user_message
    })

    # Simple rule-based reply for practice
    if "my name is" in user_message.lower():
        name = user_message.split("is", 1)[1].strip()
        reply = f"Nice to meet you, {name}!"

    elif "what is my name" in user_message.lower():
        previous_name = None

        for item in conversation_history:
            message = item["message"].lower()

            if "my name is" in message:
                previous_name = item["message"].split("is", 1)[1].strip()

        if previous_name:
            reply = f"Your name is {previous_name}."
        else:
            reply = "You haven't told me your name yet."

    else:
        reply = "I received your message."

    # Store the chatbot's response
    conversation_history.append({
        "role": "assistant",
        "message": reply
    })

    return reply


print("Chatbot:", chat("My name is Pushpa"))
print("Chatbot:", chat("What is my name?"))

print("\n--- Conversation History ---")

for item in conversation_history:
    print(f"{item['role']}: {item['message']}")