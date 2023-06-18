def is_palindrome(x):
    if x == x[::-1]:
        return True
    else:
        return False

str_input = input("Input a text: ")
if is_palindrome(str_input) == True:
    print("This is a palindrome.")
else:
    print("This is not a palindrome.")