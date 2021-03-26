import pyautogui
import random
import string

chars=string.printable
char_list=list(chars)

password= pyautogui.password("Enter your password:")
s=""
i=0
while True:
    answer=random.choices( char_list, k=1)
    print(answer)
    if answer==list(password[i]):
       s+=password[i]
       i+=1
    if s==password:
        break 
pyautogui.alert(text=s,title="Cracked Password",button='OK')
