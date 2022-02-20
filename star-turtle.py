# Python program to draw a star shape

import turtle
star = turtle.Turtle()
 
star.right(75)
star.forward(1008)
 
for i in range(4):
    star.right(144)
    star.forward(100)
     
turtle.done()
