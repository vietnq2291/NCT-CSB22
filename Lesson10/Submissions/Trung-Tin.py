def ex1():
    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]
    newDict = {}
    for x in range(len(keys)):
        newDict[keys[x]] = values[x]
    return newDict 

print(ex1())

def ex2():
    dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
    dict1.update(dict2)
    return dict1 # {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

print(ex2())

def ex3():
    sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
                }
            }
        }
    }

    print(sampleDict["class"]["student"]["marks"]["history"])
    # print value of key 'history'
ex3()

def ex4():
    sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

    # Keys to extract
    keys = ["name", "salary"]

    newDict2 = {}
    for x in range(len(keys)):
        newDict2[keys[x]] = sample_dict[keys[x]]

    return newDict2
print(ex4())

def ex5():
    sample_dict = {
        'Physics': 82,
        'Math': 65,
        'history': 75
    }

    min_val = sample_dict["Physics"]
    for values in sample_dict.values():
        if values < min_val:
            min_val = values

    return min_val # key of the mimimum value in the dict
print(ex5())