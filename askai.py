import requests
import timeandpauses
import rotateapikeys

API_KEY = rotateapikeys.choosevalidkey()
print(API_KEY)
# abdulaziz = "google/gemini-2.5-pro-exp-03-25:free"      # slow, accurate.
almaz = "google/gemma-3-27b-it:free"                    # fast, inaccurate. but good

def ask_model(prompt, model=almaz):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content":"""You are an excellent English professor. Use your knowledge to explain your reasoning behind choosing the answer. 
             **IF USER'S QUERY STARTS WITH 'TEST', YOUR ANSWER MUST END WITH A DIGIT** - serial number of the correct answer. End your response with a line 'Answer: <index of the right answer>'. If you are unsure, guess. 
             **IF USER'S QUERY STARTS WITH 'OPEN ENDED QUESTION', YOUR ANSWER MUST END WITH THE ANSWER TO PUT INTO THE BLANK SPACE**. End your response with a line 'Answer: <answer>'. If you are unsure, guess. 
             **DO NOT ADD ANYTHING AFTER YOU OUTPUT THE CORRECT ANSWER** 
             EXAMPLE 1: Question: "TEST. What is the capital of Russia? A) Sydney, B) Saint Petersburg, C) Vladimir Putin" your output must end with: 'Answer: 2') - even though the answer is wrong, it is the best guess; 
             EXAMPLE 2: If the group of the answers is ['A) mother', 'B) uncle', 'C) friend'] and the correct answer is 'friend', your output must end with 'Answer: 3');
             """
             },
            {"role": "user", "content": prompt}
        ],

        "response_format": {
            "type": "json_schema",
            "json_schema": {
            "name": "explanation and answer",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {
                "explanation": {
                    "type": "string",
                    "description": "Answer the question and describe your reasoning"
                },
                "Answer": {
                    "type": "string",
                    "description": "The correct choice, formatted as 'Answer: <index>'"
                },
                "required": ["explanation", "temperature", "Answer"],
                "additionalProperties": False
                    }
                }
            }
        }
    }

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()

    try:
        return data["choices"][0]["message"]["content"]
    except:
        print("Хайюд. askai.py")
        print(data)
        return None
    


def getanswerindex(question):               # STARTS AT 0
    response = ask_model(question)

    answer = response.split("\n")[-1]

    if not(1 + (answer.lower().find("answer:"))):
        print("AI is dumb. You should just quit at this point 0.1")
        timeandpauses.wait()
    else:
        hopefullynum = answer[-1]
        try:
            return(int(hopefullynum) - 1)
        except ValueError:
            print("AI is dumb. You should just quit at this point 0.2\n", response, answer, hopefullynum)
            timeandpauses.wait()

def getanswertext(question):
    response = ask_model(question)

    answer = response.split("\n")[-1]

    if not(1 + (answer.lower().find("answer:"))):
        print("AI is dumb. You should just quit at this point 1.1")
        timeandpauses.wait()
    else:
        try:
            answer_text = answer.split("Answer: ")[1].strip()
            return answer_text
        except IndexError:
            print("AI is dumb. You should just quit at this point 1.2\n", response, answer)
            timeandpauses.wait()

                

# print(getanswerindex("My mother ___ a doctor. a)is b)are c)works"))