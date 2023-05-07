# get input
num1 = float(input("number 1: "))
num2 = float(input("number 2: "))
num3 = float(input("number 3: "))

# compare numbers
# initialize max to num1
max_num = num1
# compare max_num with num2, num3 to find the larger value if exists
if max_num < num2:
    max_num = num2
if max_num < num3:
    max_num = num3

print("The largest number is:", max_num)