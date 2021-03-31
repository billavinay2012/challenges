medium_word_list = []
f=open("HangmanGame\\medium_words.txt", "r")

while True:
    n = f.readline()
    if n=='spine':
        medium_word_list.append('spine')
        break
    medium_word_list.append(n[:len(n)-1])
print(medium_word_list)




