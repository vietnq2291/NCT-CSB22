def is_palindrome(string):
    string = string.replace("","").lower()

    if string == string[::-1]:
        return True
    else:
        return False
string = input("Nhập Chuỗi:")

if is_palindrome(string):
    print("Chuỗi là palidrome")
else:
    print("Chuỗi không phải là palidrome")