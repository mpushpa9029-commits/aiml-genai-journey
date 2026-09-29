# Day 4 - Prompting Techniques

def zero_shot():
    return """
Task: Classify the sentiment of this sentence.
Sentence: I love learning Generative AI.
"""


def one_shot():
    return """
Example:
Sentence: I love Python.
Sentiment: Positive

Now classify:
Sentence: I am confused about Git.
"""


def few_shot():
    return """
Example 1:
Sentence: This course is excellent.
Sentiment: Positive

Example 2:
Sentence: This bug is frustrating.
Sentiment: Negative

Now classify:
Sentence: I enjoy building AI projects.
"""


print("ZERO-SHOT")
print(zero_shot())

print("ONE-SHOT")
print(one_shot())

print("FEW-SHOT")
print(few_shot())