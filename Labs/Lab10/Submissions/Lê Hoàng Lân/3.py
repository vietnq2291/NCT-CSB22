number_list = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 
               'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX']

newDict = {}
for i in range(0, len(number_list)):
    newDict[number_list[i]] = i+1

num = input("Input a Roman number: ")
if num in newDict.keys():
    print(f"Arabic number: {newDict[num]}")
else:
    print("Not found.")