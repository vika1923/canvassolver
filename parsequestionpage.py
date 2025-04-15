from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

def getquestioncards(driver):
    questions = list()
    # Get all question elements, not just multiple choice
    question_uc_elems = driver.find_elements(By.CSS_SELECTOR, "div.display_question.question")
    for question in question_uc_elems:
        questions.append(question.get_attribute('outerHTML'))
    return questions

def getquestionslist(driver):
    formatted_QnAs = []
    for card in getquestioncards(driver):
        soup = BeautifulSoup(card, features="html.parser")
        
        question_div = soup.find('div', class_='question_text user_content enhanced')
        # print("question_div:", question_div)

        if question_div:
            question_text = question_div.get_text()
            
            answer_divs = soup.find_all('div', class_='answer')
            if answer_divs:
                answers = []
                for answer_div in answer_divs:
                    answer_text = answer_div.get_text(strip=True)
                    answers.append(answer_text)
                
                if question_text and answers:
                    formatted_QnAs.append(f"TEST. {question_text}, ANSWER CHOICES: {', '.join(answers)}")
            else:
                if question_text:
                    formatted_QnAs.append(f"OPEN ENDED QUESTION. {question_text}")
                else:
                    print("else case. getQnAs() appended nothing.  question_div:", question_div)


    print("formatted questions returned by getQnAs():", formatted_QnAs)
    return formatted_QnAs

# questions_and_answers = getQnAs(driver)
# print(questions_and_answers)