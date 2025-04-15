import undetected_chromedriver as uc
import timeandpauses
import interact

options = uc.ChromeOptions()

# print("Launching driver...")
driver = uc.Chrome(options=options, use_subprocess=True)

# print("Opening page...")
driver.get("https://auttashkent.instructure.com/courses/239/pages/1-dot-5a-getting-acquainted-grammar-guide-1-was-slash-were?module_item_id=4405")

timeandpauses.pause()

if "Login" in driver.title:
    print("ATTENTION! login manually, then come back")
    timeandpauses.wait()

while True:
    if "quizzes" in driver.current_url:
        interact.solvequiz(driver=driver)
        timeandpauses.longpause()
    else:
        interact.nextpage(driver=driver)
