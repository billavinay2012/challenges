import random
import string
from generate_hard_words import hard_word_list
from generate_easy_words import easy_word_list
from generate_medium_words import medium_word_list
    
def choose():
    print("\nChoose the difficulty level to continue or End the game(4)")
    choice_number = int(input("1.Easy 2.Medium 3.Hard 4.Exit\n"))
    if choice_number == 1:
        return list(random.choice(easy_word_list).upper())
    elif choice_number==2:
        return list(random.choice(medium_word_list).upper())
    elif choice_number==3:
        return list(random.choice(hard_word_list).upper())
    elif choice_number==4:
        print("Good Bye!")
        return 4
    else:
        print("Please enter a valid choice!!!")
        return 0

def game(word_to_be_guessed):

    #creating blank spaces for user
    answer=[]
    for i in range(len(word_to_be_guessed)):
        answer.append('—')
    print(' '.join(answer))

    if len(word_to_be_guessed)<=5:
        temp = random.randint(0,len(word_to_be_guessed)-1)
        answer[temp]=word_to_be_guessed[temp]
    else:
        temp = random.randint(0,len(word_to_be_guessed)-1)
        answer[temp]=word_to_be_guessed[temp]

    #Total number of lives
    lives = len(word_to_be_guessed)

    used_word_set=set()

    while lives>0 and ''.join(answer)!=''.join(word_to_be_guessed):
        print(f"\nYou have {lives} lives left")
        element = input("Enter the letter for word:  ").upper()

        if element in used_word_set:
            print(f"You have already used {element}")
            print(' '.join(answer))
        elif element in word_to_be_guessed:
            for i in range(len(word_to_be_guessed)):
                if element==word_to_be_guessed[i]:
                    answer[i]=element
            print(' '.join(answer))
            used_word_set.add(element)
        else:
            used_word_set.add(element)
            print("Oops! wrong guess...")
            print(' '.join(answer))
            lives-=1    
        print(f"Used letters are: {used_word_set}")

    word_to_be_guessed=''.join(word_to_be_guessed)
    if lives>0:
        print("Congrats you have correctly guessed ",word_to_be_guessed)
    else:
        print("Oh no! The correct word is ",word_to_be_guessed)
    
def execute():
    print()    
    print("|   |  /\  |\  | |‾‾‾‾‾‾ |\    /|  /\  |\  |      |‾‾‾‾‾‾  /\  |\    /||‾‾‾‾‾‾ ")
    print("|———| /——\ | \ | |  |‾‾| | \  / | /——\ | \ |      |  |‾‾| /——\ | \  / ||—————  ")
    print("|   |/    \|  \| |_____| |  \/  |/    \|  \|      |_____|/    \|  \/  ||______ ")
    while True:
        word_to_be_guessed=choose()
        if word_to_be_guessed==4:
            break
        elif word_to_be_guessed==0:
            pass
        else:
            game(word_to_be_guessed)
    
execute()


















