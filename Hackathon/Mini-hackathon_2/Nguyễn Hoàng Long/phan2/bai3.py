import turtle
colors = ["blue", "red", "teal", "green"]

t = turtle.Turtle()

t.width(5)

for i in range(50):
    color = colors[i % len(colors)]
    t.pencolor(color)
    t.forward(4)

t.forward(400)


turtle.done()
