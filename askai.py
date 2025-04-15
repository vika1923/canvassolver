import os
import requests
import json
from openai import OpenAI

API_KEY = os.getenv("AI_API_KEY")
abdulaziz = "google/gemini-2.5-pro-exp-03-25:free"      # slow, correct.
almaz = "google/gemma-3-27b-it:free"                    # fast, wrong.

def ask_model(prompt, model=almaz):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content":"You are an excellent English professor. Use your knowledge to explain your reasoning behind choosing the answer. Your answer is a digit - serial number of the correct answer. End your response with a line 'Answer: <index of the right answer>'. If you are unsure, guess. EXAMPLE 1: if the group of the answers is ['apple', 'banana', 'orange'] and the correct answer is 'banana', your output must end with 'Answer: 2'); EXAMPLE 2: if the group of the answers is ['A) mother', 'B) uncle', 'C) friend'] and the correct answer is 'friend', your output must end with 'Answer: 3')"},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()

    try:
        return data["choices"][0]["message"]["content"]
    except:
        print("Хайюд")
        print(data)
        return None


if __name__ == "__main__":
    question = "Choose the correct word: 'She _____ to the store every day.'\nA) go\nB) goes\nC) going\nD) gone"
    answer = ask_model(question)
    print("Model Answer:\n", answer)
