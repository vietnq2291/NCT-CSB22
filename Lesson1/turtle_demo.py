import turtle

# Draw a square
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)

# move the pen to the left 
turtle.penup()
turtle.right(90)
turtle.forward(200)
turtle.pendown()

# Draw a pentagon
turtle.right(72)
turtle.forward(100)
turtle.right(72)
turtle.forward(100)
turtle.right(72)
turtle.forward(100)
turtle.right(72)
turtle.forward(100)
turtle.right(72)
turtle.forward(100)

# move the pen above the pentagon
turtle.penup()
turtle.right(90)
turtle.forward(180)
turtle.pendown()

# Draw the number 5
turtle.right(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)

# move the pen to the right
turtle.penup()
turtle.forward(100)
turtle.pendown()

# Draw a star
turtle.forward(200)
turtle.right(144)
turtle.forward(200)
turtle.right(144)
turtle.forward(200)
turtle.right(144)
turtle.forward(200)
turtle.right(144)
turtle.forward(200)


# Keep the window open
turtle.mainloop()