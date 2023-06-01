print("== Registration ==")
u = input("Username: ")
p = input("Password: ")
while True:
    rp = input("Repeat password: ")
    if rp != p:
        print("Passwords not match. Please input again.")
    else:
        break
e = input("Email: ")
print("Registered successfully.")