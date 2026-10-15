# Day 20 - Prompt Chaining

def create_summary(topic):
    return f"{topic} is a technology that helps computers learn and solve problems."


def create_questions(summary):
    return [
        f"What is the main idea of this topic?",
        f"Why is this topic useful?",
        f"Give one real-world example related to: {summary}"
    ]


def create_answers(questions):
    answers = []

    for question in questions:
        answers.append(
            f"Answer: This is related to understanding and applying the concept."
        )

    return answers


# Step 1 - Generate Summary
topic = "Machine Learning"

summary = create_summary(topic)

print("----- STEP 1: SUMMARY -----")
print(summary)


# Step 2 - Generate Questions
questions = create_questions(summary)

print("\n----- STEP 2: QUESTIONS -----")

for number, question in enumerate(questions, start=1):
    print(f"{number}. {question}")


# Step 3 - Generate Answers
answers = create_answers(questions)

print("\n----- STEP 3: ANSWERS -----")

for answer in answers:
    print(answer)