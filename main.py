import undetected_chromedriver as uc
import parsequestionpage
import timeandpauses
import interact
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import colordialogue

options = uc.ChromeOptions()

# print("Launching driver...")
driver = uc.Chrome(options=options, use_subprocess=True)

# print("Opening page...")
driver.get("https://auttashkent.instructure.com/courses/239/pages/1-dot-11-getting-acquainted-final-video?module_item_id=4418")

timeandpauses.pause()

if "Login" in driver.title:
    colordialogue.print_y("ATTENTION! login manually, then come back")
    timeandpauses.wait()

while True:
    url = driver.current_url
    print("url:", url)
    if "quizzes" in url and parsequestionpage.isnotlistening(driver=driver):
        print("on quizzes page")
        if("take" in url) :         # Already ON the quizz page (one with the actual questions)
            interact.solvequiz(driver=driver)
        else:
            try:
                element = driver.find_element(By.CSS_SELECTOR, "a#take_quiz_link")          # click that blue "take quiz" button
                if "again" in element.text.lower():                 # quizz already solved
                    interact.nextpage(driver=driver)
                else:
                    print("Quiz already solved!")
                    interact.click_webelement(driver=driver, element=element)
            except NoSuchElementException:
                try:
                    element = driver.find_element(By.XPATH, "//a[text()='Resume Quiz']")            # same thing (as ^^^) but different
                    interact.click_webelement(driver=driver, element=element)
                except:
                    print("NoSuchElementException. nextpage()")
                    interact.nextpage(driver=driver)
    else:
        print('"quizzes" in url and parsequestionpage.isnotlistening(driver=driver) WAS FALSE')
        interact.nextpage(driver=driver)
    # timeandpauses.wait()