import turtle
  
# tạo turtle
t = turtle.Turtle()
  
# số cạnh 
n = int(input("số cạnh : "))
  
# độ dài các cạnh
l = int(input("độ dài các cạnh : "))
  
  
for _ in range(n):
    turtle.forward(l)
    turtle.right(360 / n)
turtle.done()