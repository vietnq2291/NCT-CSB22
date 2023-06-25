def is_palindrome(string):
    return string == string[::-1]
user_input = input("Nhập chuỗi cần kiểm tra: ")
if is_palindrome(user_input):
    print("Chuỗi là palindrome")
else:
    print("Chuỗi không phải là palindrome")
