hard_word_list = []
f=open("HangmanGame\\hard_words.txt", "r")

while True:
    n = f.readline()
    if n=='zombie':
        hard_word_list.append('zombie')
        break
    hard_word_list.append(n[:len(n)-1])




