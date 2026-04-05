import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_question(topic):
    prompt = f"Ask one basic interview question on {topic}"

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


def evaluate_answer(question, answer):
    prompt = f"""
You are a strict technical interviewer.

Question: {question}
Answer: {answer}

Evaluate based on:
- Accuracy
- Clarity
- Completeness

Give response in this format:

Score: X/10

Feedback:
- ...

Correct Answer:
- ...
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content