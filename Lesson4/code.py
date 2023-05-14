# For loop
"""
s = 0
for i in range(5):
    s = s + i
print(s)
"""

# While loop ------------------------------------------------
s = 0
i = 0
while i < 5:
    s = s + i
    i = i + 1
print(s)
# -----------------------------------------------------------
# Note: These 2 loops have the same result


# print 0 1 2 3 5 (except 4)
"""
i = 0
while i < 10:
    if i == 4: # i đang bằng 4
        i = i + 1
        continue # thì nhảy vào vòng tiếp theo luôn
    if i > 5:
        break
    print(i)
    i = i + 1
"""


