import undetected_chromedriver as uc
import timeandpauses
import requests

options = uc.ChromeOptions()

print("Launching driver...")
driver = uc.Chrome(options=options, use_subprocess=True)

print("Opening page...")
# driver.get("https://auttashkent.instructure.com/courses/238/quizzes/691/take")
# driver.get("https://auttashkent.instructure.com/courses/238/pages/start-here-syllabus?module_item_id=4237")
# https://auttashkent.instructure.com/courses/238/quizzes/691/take
driver.get("https://en.wikipedia.org/wiki/Almaz")

# response = requests.get('https://en.wikipedia.org/wiki/Almaz')
# print(response.encoding) 

timeandpauses.wait()

