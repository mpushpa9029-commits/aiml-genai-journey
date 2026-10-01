# Day 6 - Prompt Chaining

def step1_summary(topic):
    return f"Summary of {topic}: It is a concept in Artificial Intelligence."


def step2_questions(summary):
    return f"Create 3 interview questions from this summary:\n{summary}"


def step3_answers(questions):
    return f"Provide simple answers for these questions:\n{questions}"


# Step 1
summary = step1_summary("Machine Learning")
print("STEP 1 - SUMMARY")
print(summary)

# Step 2
questions = step2_questions(summary)
print("\nSTEP 2 - QUESTIONS")
print(questions)

# Step 3
answers = step3_answers(questions)
print("\nSTEP 3 - ANSWERS")
print(answers)