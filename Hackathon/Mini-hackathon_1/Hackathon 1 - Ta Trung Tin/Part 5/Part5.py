import random
import time

score = 0
lose = 0
print("""== FREAKING MATH CONSOLE ==
Give correct answers to get 
scores.
""")
while True:
    cROps = "+-*/"
    cRNum1 = random.randint(1, 100)
    cRNum2 = random.randint(1, 100)
    cRNum3 = random.randint(1, 100)
    rChosenOps = cROps[random.randint(0, 3)]
    selection = [cRNum1, cRNum2, cRNum3]

    if rChosenOps == "+":
        num1 = selection[random.randint(0, 2)] #Num1
        num2 = selection[random.randint(0, 2)] #Num3
        tRes = num1 + num2
        print(f"{num1} {rChosenOps} {num2} = {tRes}")
        cAnswer = input("1 for True, 0 for False: ")
        if tRes == (num1 + num2) and cAnswer == "1":
            score += 1
            print(f"Score: {score}")
        elif tRes != (num1 + num2) and cAnswer == "0":
            score += 1
            print(f"Score: {score}")
        elif (tRes != (num1 + num2) and cAnswer == "1") or (tRes == (num1 + num2) and cAnswer == "0"): 
            print(f"""== GAME OVER ==
Your total score is {score}""")
            break

    elif rChosenOps == "-":
        num1 = selection[random.randint(0, 2)] #Num1
        num2 = selection[random.randint(0, 2)] #Num3
        tRes = num1 - num2
        print(f"{num1} {rChosenOps} {num2} = {tRes}")
        cAnswer = input("1 for True, 0 for False: ")
        if tRes == (num1 - num2) and cAnswer == "1":
            score += 1
            print(f"Score: {score}")
        elif tRes != (num1 - num2) and cAnswer == "0":
            score += 1
            print(f"Score: {score}")
        elif (tRes != (num1 - num2) and cAnswer == "1") or (tRes == (num1 - num2) and cAnswer == "0"): 
            print(f"""== GAME OVER ==
Your total score is {score}""")
            break

    elif rChosenOps == "*":
        num1 = selection[random.randint(0, 2)] #Num1
        num2 = selection[random.randint(0, 2)] #Num3
        tRes = num1 * num2
        print(f"{num1} {rChosenOps} {num2} = {tRes}")
        cAnswer = input("1 for True, 0 for False: ")
        if tRes == (num1 * num2) and cAnswer == "1":
            score += 1
            print(f"Score: {score}")
        elif tRes != (num1 * num2) and cAnswer == "0":
            score += 1
            print(f"Score: {score}")
        elif (tRes != (num1 * num2) and cAnswer == "1") or (tRes == (num1 * num2) and cAnswer == "0"): 
            print(f"""== GAME OVER ==
Your total score is {score}""")
            break

    elif rChosenOps == "/":
        num1 = selection[random.randint(0, 2)] #Num1
        num2 = selection[random.randint(0, 2)] #Num3
        tRes = num1 / num2
        print(f"{num1} {rChosenOps} {num2} = {tRes}")
        cAnswer = input("1 for True, 0 for False: ")
        if tRes == (num1 / num2) and cAnswer == "1":
            score += 1
            print(f"Score: {score}")
        elif tRes != (num1 / num2) and cAnswer == "0":
            score += 1
            print(f"Score: {score}")
        elif (tRes != (num1 / num2) and cAnswer == "1") or (tRes == (num1 + num2) and cAnswer == "0"): 
            print(f"""== GAME OVER ==
Your total score is {score}""")
            break
