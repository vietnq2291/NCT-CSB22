accounts = {}
def register():
    print("Đăng ký tài khoản")
    # Nhập thông tin
    username = input("Tên đăng nhập: ")
    password = input("Mật khẩu: ")
    email = input("Email: ")
# Tạo tài khoản mới
    accounts[username] = {"password": password, "email": email}
    print("Tài khoản đã được tạo thành công!")
register()