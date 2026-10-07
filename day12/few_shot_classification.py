# Day 12 - Few-Shot Prompting

def create_few_shot_prompt(sentence):
    prompt = f"""
You are a sentiment classifier.

Example 1:
Sentence: I love this course.
Sentiment: Positive

Example 2:
Sentence: This movie is terrible.
Sentiment: Negative

Example 3:
Sentence: Python is very useful.
Sentiment: Positive

Now classify the following sentence:

Sentence: {sentence}

Return only:
Positive or Negative
"""
    return prompt


sentence1 = "I really enjoyed learning Generative AI."
sentence2 = "This project is frustrating."


print("----- INPUT 1 -----")
print(create_few_shot_prompt(sentence1))

print("\n----- INPUT 2 -----")
print(create_few_shot_prompt(sentence2))