from selenium.webdriver.common.by import By

def getquestions(driver):
    questions = driver.find_elements(By.CSS_SELECTOR, "div.display_question.question.multiple_choice_question")
    for question in questions:
        print("Question HTML:")
        print(question.get_attribute('outerHTML'))
        print("\n" + "-"*50 + "\n")