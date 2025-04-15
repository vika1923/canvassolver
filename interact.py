from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import timeandpauses
import random
import time
import parsequestionpage


def click_element(driver, by_method, selector, timeout=10):
    timeandpauses.pause()
    wait = WebDriverWait(driver, timeout)
    element = wait.until(EC.presence_of_element_located((by_method, selector)))
    wait.until(EC.element_to_be_clickable((by_method, selector)))
    
    actions = ActionChains(driver, duration=random.randint(200, 1000))
    actions.move_to_element_with_offset(to_element=element, xoffset=random.randint(-14, 12), yoffset=random.randint(-10, 10))
    actions.click(element)
    actions.perform()
    timeandpauses.shortpause()


def nextpage(driver):
    timeandpauses.shortpause()
    # total_height = driver.execute_script("return document.body.scrollHeight")
    # current_position = 0
    # while current_position < total_height:
    #     scroll_amount = random.randint(100, 300)
    #     current_position = min(current_position + scroll_amount, total_height)
    #     driver.execute_script(f"window.scrollTo(0, {current_position});")
    # timeandpauses.shortpause()
    
    click_element(driver, By.CSS_SELECTOR, "a[aria-label='Next Module Item']")


def mocktyping(driver, string):
    for c in string:
        time.sleep(random.uniform(0.02, 0.1))
        driver.send_keys(c)


def solvequiz(driver):
    print("Working on the quiz...")
    timeandpauses.shortpause()
    
    wait = WebDriverWait(driver, 10)
    quiz_title = wait.until(EC.presence_of_element_located((By.ID, "quiz_title")))
    print(quiz_title)
    
    if any(x in quiz_title.text.lower() for x in ["listen", "unit quiz", "video", "watch"]):
        # TODO >>> add speech to text recognition and solve listening tests <<< TODO
        print(f"ATTENTION! Skipping. solve quizz at {driver.current_url} manually")
        nextpage(driver)
    else: 
        try:
            click_element(driver, By.CSS_SELECTOR, "div.take_quiz_button a.btn.btn-primary")
        except NoSuchElementException:
            click_element(driver, By.CSS_SELECTOR, "a.btn.btn-primary[data-method='post']")

        # get the list of the questions ---> 
        # for q in questions: get answer from the AI -> click_element(<answer>) ---> 
        # submit .|

        parsequestionpage.getquestions(driver)
            