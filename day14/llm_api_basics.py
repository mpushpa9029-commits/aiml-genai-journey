# Day 14 - LLM API Basics

def simulate_llm_api(prompt):
    """
    Simulates an LLM API request and response.
    This function does not call a real AI model.
    """

    print("Sending request to the AI service...")
    print("Prompt:", prompt)

    # Simulated response
    response = {
        "status": "success",
        "answer": (
            "Machine Learning is a branch of AI "
            "that learns patterns from data."
        )
    }

    return response


user_prompt = "Explain Machine Learning in simple words."

result = simulate_llm_api(user_prompt)

print("\n----- API RESPONSE -----")
print("Status:", result["status"])
print("Answer:", result["answer"])