import os

api_keys = os.getenv("API_KEYS").split()
number_of_keys = len(api_keys)

i = 0
# api_key_index = 0
# def choosevalidkey():
#     global i, api_key_index
#     if i == 10:
#         api_key_index = api_key_index % number_of_keys
#         api_key_index += 1
#         i = 0
#         if api_key_index == number_of_keys:
#             api_key_index = 0
#     i += 1
#     print(api_keys[api_key_index], "("+str(api_key_index), str(i)+")")
#     return api_keys[api_key_index]

def choosevalidkey():
    global i
    i += 1
    return api_keys[(i - 1)%number_of_keys]
