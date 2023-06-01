import turtle
import math
# Nhập bán kính từ người dùng
radius = float(input("Nhập bán kính của hình tròn: "))
def draw(rad):
      
    # draw circle
    turtle.circle(rad)
      
    # set the position by using setpos()
    turtle.up()
    turtle.setpos(0,-rad)
    turtle.down()