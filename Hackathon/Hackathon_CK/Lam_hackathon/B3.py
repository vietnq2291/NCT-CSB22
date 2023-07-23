def is_palindrome(i):
    reversed_i = i[::-1]
    if i == reversed_i:
        return True
    else:
        return False
user_input = input("Input a text: ")
if is_palindrome(user_input):
    print("This is a palindrome.")
else:
    print("This is not a palindrome.")
