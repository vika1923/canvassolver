# import undetected_chromedriver as uc
# import timeandpauses
# import requests

# options = uc.ChromeOptions()

# print("Launching driver...")
# driver = uc.Chrome(options=options, use_subprocess=True)

# print("Opening page...")
# # driver.get("https://auttashkent.instructure.com/courses/238/quizzes/691/take")
# # driver.get("https://auttashkent.instructure.com/courses/238/pages/start-here-syllabus?module_item_id=4237")
# # https://auttashkent.instructure.com/courses/238/quizzes/691/take
# driver.get("https://en.wikipedia.org/wiki/Almaz")

# # response = requests.get('https://en.wikipedia.org/wiki/Almaz')
# # print(response.encoding) 

# timeandpauses.wait()

# class bcolors:
#     HEADER = '\033[95m'
#     OKBLUE = '\033[94m'
#     OKCYAN = '\033[96m'
#     OKGREEN = '\033[92m'
#     WARNING = '\033[93m'
#     FAIL = '\033[91m'
#     ENDC = '\033[0m'
#     BOLD = '\033[1m'
#     UNDERLINE = '\033[4m'

# print(f"{bcolors.HEADER}Warning: No active frommets remain. Continue?")
# print(f"{bcolors.OKBLUE}Warning: No active frommets remain. Continue?")
# print(f"{bcolors.OKCYAN}Warning: No active frommets remain. Continue?")
# print(f"{bcolors.OKGREEN}Warning: No active frommets remain. Continue?")
# print(f"{bcolors.WARNING}Warning: No active frommets remain. Continue?")
# print(f"{bcolors.FAIL}Warning: No active frommets remain. Continue?")
# print(f"{bcolors.ENDC}Warning: No active frommets remain. Continue?")
# print(f"{bcolors.BOLD}Warning: No active frommets remain. Continue?")
# print(f"{bcolors.UNDERLINE}Warning: No active frommets remain. Continue?{bcolors.ENDC}")

# l = [1,2,3,4,5]
# print(l.pop(0))
# print(l)

# print("jjjjjopopop op op opakkk".find("opak"))

import os

tl = os.getenv("TEST")
print(tl.split())