n = (input("Input a text: "))
def is_palindrome():
    str = ""
    for char in n:
        str = char + str
    if str == n:
        return True
    return False
if is_palindrome():
    print("This is a palindrome.")
else:
    print("This is not a palindrome.")