from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import timeandpauses
import random
import time
import parsequestionpage
import askai


# def click_element(driver, by_method, selector, timeout=30):
#     timeandpauses.pause()
#     wait = WebDriverWait(driver, timeout)
#     element = wait.until(EC.presence_of_element_located((by_method, selector)))
#     wait.until(EC.element_to_be_clickable((by_method, selector)))
    
#     actions = ActionChains(driver, duration=random.randint(200, 1000))
#     actions.move_to_element_with_offset(to_element=element, xoffset=random.randint(-14, 12), yoffset=random.randint(-10, 10))
#     actions.click(element)
#     actions.perform()
#     timeandpauses.shortpause()

def click_webelement(driver, element):
    timeandpauses.pause()
    actions = ActionChains(driver, duration=random.randint(200, 1000))
    actions.move_to_element(element)
    actions.click(element)
    actions.perform()
    timeandpauses.shortpause()


def nextpage(driver):
    print("trying to go to the next page")
    timeandpauses.shortpause()
    # total_height = driver.execute_script("return document.body.scrollHeight")
    # current_position = 0
    # while current_position < total_height:
    #     scroll_amount = random.randint(100, 300)
    #     current_position = min(current_position + scroll_amount, total_height)
    #     driver.execute_script(f"window.scrollTo(0, {current_position});")
    # timeandpauses.shortpause()
    
    # click_element(driver, By.CSS_SELECTOR, "a[aria-label='Next Module Item']")
    click_webelement(driver, driver.find_element(By.CSS_SELECTOR, "a[aria-label='Next Module Item']"))


def mocktyping(element, string):
    for c in string:
        time.sleep(random.uniform(0.02, 0.07))
        element.send_keys(c)
    

def solvequiz(driver):
    print("Working on the quiz...")
    # timeandpauses.shortpause()

    # try:
    #     click_webelement(driver, driver.find_element(By.CSS_SELECTOR, "div.take_quiz_button a.btn.btn-primary"))
    # except NoSuchElementException:
    #     click_webelement(driver, driver.find_element(By.CSS_SELECTOR, "a.btn.btn-primary[data-method='post']"))

    # get the list of the questions ---> 
    # for q in questions: get answer from the AI -> click_element(<answer>) ---> 
    # submit .|
    
    formatted_QnAs = parsequestionpage.getquestionslist(driver=driver)
    interels = parsequestionpage.get_interactive_elements(driver=driver)

    print("INTERELS:\n", interels)

    for i in range(len(formatted_QnAs)):

        formatted_question = formatted_QnAs[i]
        answer_uc_element = interels[i]

        # print(formatted_question)

        if formatted_question.find("OPEN ENDED QUESTION.") != -1:
            q = askai.getanswertext(formatted_question) 
                    
            if len(answer_uc_element) == 2 and answer_uc_element[0] == "OEQalmazOEQ":
                print("len(answer_uc_element) == 2 and answer_uc_element[0] == OEQalmazOEQ")
                a = answer_uc_element[1][0]         # won't work if there are several input fields for one question
                click_webelement(driver, a)
                mocktyping(a, q)

        elif formatted_question.find("TEST.") != -1:
            q = askai.getanswerindex(formatted_question)
            answer_uc_element[q].click()

        else:
            print("Some question types mismatch happened in interact.py")
        timeandpauses.shortpause()
    
    # WE ARE DONE WITH ALL THE QUESIONS.
    submit_button = driver.find_element(By.CSS_SELECTOR, "button#submit_quiz_button")
    click_webelement(driver, submit_button)
