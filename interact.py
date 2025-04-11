from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import timeandpauses
import random
import time


def click_element(driver, by_method, selector):
    timeandpauses.shortpause()
    element = driver.find_element(by_method, selector)
    actions = ActionChains(driver, duration=random.randint(200, 1000))
    actions.move_to_element_with_offset(to_element=element, xoffset=random.randint(-14, 12), yoffset=random.randint(-10, 10))
    timeandpauses.shortpause()
    actions.click(element)
    actions.perform()
    timeandpauses.longpause()

def nextpage(driver):
    timeandpauses.shortpause()
    total_height = driver.execute_script("return document.body.scrollHeight")
    current_position = 0
    while current_position < total_height:
        scroll_amount = random.randint(100, 300)
        current_position = min(current_position + scroll_amount, total_height)
        driver.execute_script(f"window.scrollTo(0, {current_position});")
        timeandpauses.shortpause()
    timeandpauses.shortpause()
    
    click_element(driver, By.CSS_SELECTOR, "a[aria-label='Next Module Item']")


def mocktyping(driver, string):
    for c in string:
        time.sleep(random.uniform(0.02, 0.1))
        driver.send_keys(c)


def solvequiz(driver):
    print("Working on the quiz")
    timeandpauses.shortpause()
    try:
        click_element(driver, By.ID, "take_quiz_link")
    except NoSuchElementException:
        click_element(driver, By.CSS_SELECTOR, "a.btn.btn-primary[data-method='post']")

