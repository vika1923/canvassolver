from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from testonalmaz import driver

def getquestioncards(driver):
    questions = list()
    question_uc_elems = driver.find_elements(By.CSS_SELECTOR, "div.display_question.question.multiple_choice_question")
    for question in question_uc_elems:
        questions.append(question.get_attribute('outerHTML'))
    return questions

def getQnAs(driver):
    QnAs = dict()
    for card in getquestioncards(driver):
        soup = BeautifulSoup(card, features="html.parser")
        
        question_div = soup.find('div', class_='question_text user_content enhanced')
        if question_div:
            question_text = question_div.get_text()
            
            answers = []
            answer_divs = soup.find_all('div', class_='answer')
            for answer_div in answer_divs:
                answer_text = answer_div.get_text(strip=True)
                answers.append(answer_text)
            
            if question_text and answers:
                QnAs[question_text] = answers
    
    return QnAs

# Example usage
questions_and_answers = getQnAs(driver)
print(questions_and_answers)

# vkim@aut-edu.uz
# pwNoOneNeeds1