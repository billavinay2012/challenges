easy_word_list = []
f=open("HangmanGame\\easy_words.txt", "r")

while True:
    n = f.readline()
    if n=='moon':
        easy_word_list.append('moon')
        break
    easy_word_list.append(n[:len(n)-1])
print(easy_word_list)




