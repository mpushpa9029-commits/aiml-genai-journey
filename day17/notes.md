# Day 17 - Conversation Memory

## What is Conversation Memory?
Conversation memory means storing previous messages so a chatbot can refer to them during a conversation.

## Why is it Useful?
- Maintains conversation context.
- Helps remember earlier messages during the current session.
- Supports multi-turn conversations.
- Improves continuity in chatbot applications.

## How Does It Work?
1. Receive a user message.
2. Store the message in conversation history.
3. Generate a reply.
4. Store the chatbot's reply.
5. Use previous messages when processing the next message.

## Python Concepts Used
- Lists
- Dictionaries
- Functions
- `append()`
- Loops and conditions

## Example
User: My name is Pushpa.

Chatbot: Nice to meet you, Pushpa!

User: What is my name?

Chatbot: Your name is Pushpa.

## Important Note
This project uses a Python list and rule-based replies to simulate conversation memory. It does not use an actual LLM, and the history is lost when the program stops.

## Day 17 Practice
- Created a simple chatbot.
- Stored user messages and chatbot responses.
- Retrieved information from previous messages.
- Displayed conversation history.

## Learning Outcome
Understood how conversation history can help a chatbot maintain context during a conversation.