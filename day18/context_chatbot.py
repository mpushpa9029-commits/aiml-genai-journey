# Day 18 - Context-Aware Chatbot

conversation_history = []


def chat(user_message):
    conversation_history.append({
        "role": "user",
        "message": user_message
    })

    message = user_message.lower()

    if "my favorite language is" in message:
        language = user_message.split("is", 1)[1].strip()
        reply = f"I'll remember for this session that you like {language}."

    elif "what is my favorite language" in message:
        language = None

        for item in conversation_history:
            old_message = item["message"].lower()

            if "my favorite language is" in old_message:
                language = item["message"].split("is", 1)[1].strip()

        if language:
            reply = f"Your favorite language is {language}."
        else:
            reply = "You haven't told me your favorite language yet."

    else:
        reply = "I don't know that information yet."

    conversation_history.append({
        "role": "assistant",
        "message": reply
    })

    return reply


print("User: My favorite language is Python.")
print("Chatbot:", chat("My favorite language is Python."))

print("\nUser: What is my favorite language?")
print("Chatbot:", chat("What is my favorite language?"))

print("\n--- Conversation History ---")

for item in conversation_history:
    print(f"{item['role']}: {item['message']}")