from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import colordialogue

def get_interactive_elements(driver):
    interactive_elements = list()
    question_uc_elems = driver.find_elements(By.CSS_SELECTOR, "div.display_question.question")
    
    for question in question_uc_elems:
        text_inputs = question.find_elements(By.CSS_SELECTOR, "div.form-control.text-box-question-holder input.question_input")
        if text_inputs:
            interactive_elements.append(["OEQalmazOEQ", text_inputs])           # assume that no test option will be "OEQalmazOEQ" -> will later check and if it is, then will use the open ended question functionality
        radio_inputs = question.find_elements(By.CSS_SELECTOR, "div.answer input.question_input[type='radio']")
        if radio_inputs:
            interactive_elements.append(radio_inputs)
    
    return interactive_elements

def getquestioncards(driver):
    questions = list()
    question_uc_elems = driver.find_elements(By.CSS_SELECTOR, "div.display_question.question")  # all question elements, not just multiple choice
    for question in question_uc_elems:
        questions.append(question.get_attribute('outerHTML'))
    return questions

def getquestionslist(driver):
    formatted_QnAs = []
    questioncards = getquestioncards(driver)
    
    for card in questioncards:
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
                    formatted_QnAs.append(f"TEST. {question_text} ANSWER CHOICES: {', '.join(answers)}")
            else:
                if question_text:
                    formatted_QnAs.append(f"OPEN ENDED QUESTION. {question_text}")
                else:
                    print("else case. getQnAs() appended nothing.  question_div:", question_div)

    return formatted_QnAs

def isnotlistening(driver):
    quiz_header_html = driver.find_element(By.CLASS_NAME, "quiz-header")
    # print("QUIZZHEADER: >>>", quiz_header_html)
    quiz_header = quiz_header_html.get_attribute('outerHTML').lower()
    # print(quiz_header)
    ret = not (bool(1 + quiz_header.find("listen")) or 
               bool(1 + quiz_header.find("unit quiz")) or 
               bool(1 + quiz_header.find("final")) or
               bool(1 + quiz_header.find("hear")))
    print ("isnotlistening() returned", ret)
    if not ret:
        colordialogue.print_y("listening, final and unit quizzes should be solved manually. solve quiz at" + driver.current_url + "yourself")
    return ret
