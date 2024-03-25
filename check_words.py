#!python

import random
import os


with open("word_list.txt", mode="r", encoding="utf-8") as file_handle:
    j = file_handle.readlines()


words = []

for x in j:
    words.append(x.strip())


    
test_pass = []
test_fail = []

while True:
    os.system('clear')
    remaining = len(words)
    if remaining == 0:
        break
    i_dex = random.randrange(0, len(words))
    my_word = words.pop(i_dex)

    my_string = "".join(["\t",my_word,"\n", "\n"])
    
    response = input(my_string)

    if response in [*'yY']:
        test_pass.append(my_word)

    else:
        test_fail.append(my_word)

print("You got these words wrong!")
print(test_fail)
    
    


