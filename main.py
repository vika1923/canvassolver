import undetected_chromedriver as uc
import timeandpauses
import interact

options = uc.ChromeOptions()

print("Launching driver...")
driver = uc.Chrome(options=options, use_subprocess=True)

print("Opening page...")
driver.get("https://auttashkent.instructure.com/courses/238/pages/start-here-syllabus?module_item_id=4237")
# driver.get("https://en.wikipedia.org/wiki/Almaz")

timeandpauses.longpause()

if "Login" in driver.title:
    print("ATTENTION! login manually, then come back")
    timeandpauses.wait()

while True:
    if "quizzes" in driver.current_url:
        interact.solvequiz(driver=driver)
        timeandpauses.wait()
    else:
        interact.nextpage(driver=driver)
