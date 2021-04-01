import random
import string
from generate_hard_words import hard_word_list
from generate_easy_words import easy_word_list
from generate_medium_words import medium_word_list
    
def choose():
    print("\nChoose the difficulty level to continue or End the game(4)")                   #display purpose only
    choice_number = int(input("1.Easy 2.Medium 3.Hard 4.Exit\n"))                           #menu driven game experience
    if choice_number == 1:                                                                  #switch-case like simulation
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

    original_word =''.join(word_to_be_guessed)                                 #Storing the question as a string
 
    answer=[]                                                                  #creating blank spaces for user
    for i in range(len(word_to_be_guessed)):
        answer.append('—')

    if len(word_to_be_guessed)<=5:                                              #display a letter if question has <=5 letters
        temp = random.randint(0,len(word_to_be_guessed)-1)
        answer[temp]=word_to_be_guessed[temp]
        word_to_be_guessed[temp]='—'
    else:
        temp_list = list(range(len(word_to_be_guessed)))                        #display two letters if question has >5 letters
        random.shuffle(temp_list)
        a1=temp_list.pop()
        answer[a1]=word_to_be_guessed[a1]
        word_to_be_guessed[a1]='—'
        random.shuffle(temp_list)
        a2=temp_list.pop()
        answer[a2]=word_to_be_guessed[a2]
        word_to_be_guessed[a2]='—'

    print(' '.join(answer))                                                     #initial display of question

    lives = len(word_to_be_guessed)                                             #Total number of lives are equal to total number of leters

    used_letter_set=set()

    while lives>0 and ''.join(answer)!=original_word:                          #loop until no lives are left or answered is guessed correctly
        print(f"\nYou have {lives} lives left")
        element = input("Enter the letter for word:  ").upper()

        if element in used_letter_set:                                          #used_letter_set stores letters already used
            print(f"You have already used {element}")
            print(' '.join(answer))
        elif element in word_to_be_guessed:                                     #if letter matches with letters in question
            for i in range(len(word_to_be_guessed)):
                if element==word_to_be_guessed[i]:
                    answer[i]=element
            print(' '.join(answer))
            used_letter_set.add(element)
        else:                                                                   #no match
            used_letter_set.add(element)
            print("Oops! wrong guess...")
            print(' '.join(answer))
            lives-=1    
        print(f"Used letters are: {used_letter_set}")

    if lives>0:                                                                 #indicates player has won because lives > 0
        print("Congrats you have correctly guessed ",original_word)
    else:                                                                       #indicates player has lost because lives < 0
        print("Oh no! The correct word is ",original_word)
    
def execute():
    print()                                                                                                     #display purpose only
    print("|   |  /\  |\  | |‾‾‾‾‾‾ |\    /|  /\  |\  |      |‾‾‾‾‾‾  /\  |\    /||‾‾‾‾‾‾ ")
    print("|———| /——\ | \ | |  |‾‾| | \  / | /——\ | \ |      |  |‾‾| /——\ | \  / ||—————  ")
    print("|   |/    \|  \| |_____| |  \/  |/    \|  \|      |_____|/    \|  \/  ||______ ")
    while True:                                                                                                 #for a menu driven game experience
        word_to_be_guessed=choose()
        if word_to_be_guessed==4:
            break
        elif word_to_be_guessed==0:
            pass
        else:
            game(word_to_be_guessed)
    
execute()


















