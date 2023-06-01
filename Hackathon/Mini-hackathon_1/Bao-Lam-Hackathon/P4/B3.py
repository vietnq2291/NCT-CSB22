print("== Registration ==")
u = input("Username: ")
p = input("Password: ")
while True:
    rp = input("Repeat password: ")
    if rp != p:
        print("Passwords not match. Please input again.")
    else:
        break
while True:
    e = input("Email: ")
    if "@gmail.com" in e and len(e) >= 8:
        print("a")
        break
    else:
        print("b")
print("Registered successfully.")