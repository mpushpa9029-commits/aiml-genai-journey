# Day 12 - Few-Shot Prompting

## What is Few-Shot Prompting?

Few-shot prompting means giving an AI model multiple examples before asking it to perform a new task.

## Example

Example 1:
Input: I love this course.
Output: Positive

Example 2:
Input: This movie is terrible.
Output: Negative

New Input:
I enjoyed learning AI.

Expected Output:
Positive

## Why Use Few-Shot Prompting?

- Shows the model the expected pattern.
- Helps guide the output format.
- Useful for classification and extraction tasks.
- Can improve consistency.

## Prompt Pattern

Examples → New Input → Expected Output

## Day 12 Practice

- Created a few-shot prompt.
- Provided multiple examples.
- Used a variable for new input.
- Reused the same prompt template for different inputs.
- Practiced sentiment classification prompt design.

## Important

The Python program in this exercise only constructs the prompt.
It does not call an actual AI model.