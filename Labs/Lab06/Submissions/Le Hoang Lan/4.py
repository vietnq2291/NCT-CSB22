input_str = input("Write a sentence: ")
word_list = input_str.split(' ')
print(word_list)
count = 0
used_word = []
for x in word_list:
    if x not in used_word:
        used_word.append(x)
        count +=1
print(count)