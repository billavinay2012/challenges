#pip install pyautogui

import pyautogui
import string
import random

chars=string.printable
char_list= list(chars)

actual_password = pyautogui.password("Enter your password:")
answer=""

while answer!=list(actual_password):
    answer = random.choices(char_list, k=len(actual_password))
    print("<<<<<<<<<<<<<<<",answer,">>>>>>>>>>>>>>>>")

pyautogui.alert(text=''.join(answer),title="Cracked Password ",button='OK')



