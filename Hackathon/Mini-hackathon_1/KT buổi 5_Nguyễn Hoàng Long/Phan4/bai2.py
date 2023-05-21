accounts = {}

#Đăng ký tài khoản
def register():
    print("Đăng ký tài khoản")
    #Nhập thông tin
    username = input("Tên đăng nhập: ")
    password = input("Mật khẩu: ")
    confirm_password = input("Nhập lại mật khẩu: ")
    email = input("Email: ")

    #Kiểm tra lại mật khẩu 
    if password != confirm_password:
        print("Lỗi: Mật khẩu và nhập lại mật khẩu không khớp!")
        return

    #Tạo tài khoản mới
    accounts[username] = {"password": password, "email": email}
    print("Tài khoản đã được tạo thành công!")

register()
