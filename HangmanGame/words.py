import random
import string
from generate_easy_words import easy_word_list
from generate_medium_words import medium_word_list
from generate_hard_words import hard_word_list
    
def choice():
    while True:
        print("\nChoose the difficulty level to continue or End the game(4)")
        choice = int(input("1.Easy 2.Medium 3.Hard 4.Exit"))
        if choice == 1:
            return list(random.choice(easy_word_list).upper())
        elif choice==2:
            return list(random.choice(medium_word_list).upper())
        elif choice==3:
            return list(random.choice(hard_word_list).upper())
        elif choice==4:
            exit(0)
        else:
            print("Please enter a valid choice:")

def game():

    #choosing a word as the question
    word_to_be_guessed=choice()

    #creating blank spaces for user
    answer=[]
    for i in range(len(word_to_be_guessed)):
        answer.append('—')
    print(' '.join(answer))

    #Total number of lives
    lives = len(word_to_be_guessed)

    used_word_set=set()

    while lives>0 and ''.join(answer)!=''.join(word_to_be_guessed):
        print(f"\nYou have {lives} lives left")
        element = input("Enter the letter for word:  ").upper()

        if element in used_word_set:
            print(f"You have already used {element}")
        elif element in word_to_be_guessed:
            for i in word_to_be_guessed:
                if element==i:
                    answer[word_to_be_guessed.index(i)]=i
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
    choice()


        
print("|   |  /\  |\  | |‾‾‾‾‾‾ |\    /|  /\  |\  |      |‾‾‾‾‾‾  /\  |\    /||‾‾‾‾‾‾ ")
print("|———| /——\ | \ | |  |‾‾| | \  / | /——\ | \ |      |  |‾‾| /——\ | \  / ||—————  ")
print("|   |/    \|  \| |_____| |  \/  |/    \|  \|      |_____|/    \|  \/  ||______ ")
game()



















