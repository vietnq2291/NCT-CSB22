# age = 10
# if age > 18:
#     print ("you can watch movies")
# elif age == 10:
#     print ("ok")
# else:
#     print ("no you can't")
# Chall 1
a = 1 
b = 2 
c = 3
print (max (a,b,c))

# Chall 2 

# n = int(input("Year:"))
# if n % 400 != 0:
#     print ("This is a leap year")
# elif n % 4 == 0 and n % 100 != 0:
#     print ("This is a leap year")
# else: 
#     print ("Nah!")

# Chall 3 
a = float(input("a:"))
b = float(input("b:"))
c = float (input("c:"))
Delta = b*b - 4*a*c
if Delta > 0:
    print ("x1 = ", -b/2*a + sqrt(Delta)/2*a)
    print ("x2 = ", -b/2*a - sqrt(Delta)/2*a)
elif Delta == 0:
    print ("x1 = ", -b/2*a)
else:
    print ("No solution!")