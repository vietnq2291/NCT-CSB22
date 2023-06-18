n = (input("Input a text: "))
def reverse_str(n):
    str = ""
    for i in n:
        str = i + str
    return str
print(reverse_str(n))


