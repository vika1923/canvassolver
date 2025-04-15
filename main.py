import undetected_chromedriver as uc
import timeandpauses
import interact

options = uc.ChromeOptions()

# print("Launching driver...")
driver = uc.Chrome(options=options, use_subprocess=True)

# print("Opening page...")
driver.get("https://auttashkent.instructure.com/courses/238/pages/1-dot-2-technology-case-file-1-vocabulary?module_item_id=4240")
# driver.get("https://en.wikipedia.org/wiki/Almaz")
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
