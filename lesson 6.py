import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen") # Set the window background color
wn.title("Hello, Tess!") # Set the window title
tess = turtle.Turtle()
tess.color("blue") # Tell tess to change her color
tess.pensize(3) # Tell tess to set her pen width
tess.forward(50) # you can short form forward, fd
tess.left(120)
tess.forward(50)
wn.mainloop()
import turtle
wn = turtle.Screen() # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("Tess & Alex")
tess = turtle.Turtle() # Create tess and set some attributes
tess.color("hotpink")
tess.pensize(5)
alex = turtle.Turtle() # Create alex
tess.fd(80) # Make tess draw equilateral triangle
tess.lt(120)
tess.fd(80)
tess.lt(120)
tess.fd(80)
tess.lt(120) # Complete the triangle
tess.rt(180) # Turn tess around
tess.fd(80) # Move her away from the origin
alex.forward(50) # Make alex draw a square
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
wn.mainloop()
turtle.color("black", "red")
turtle.begin_fill()
turtle.circle(60)
turtle.end_fill()
import turtle
alex= turtle.Turtle()
1
2
3
for i in [0,1,2,3]:
 alex.forward(50)
 alex.left(90)
import turtle
alex= turtle.Turtle()
for i in range(4):
 alex.fd(50)
 alex.lt(90)
for c in ["yellow", "red", "purple", "blue"]:
 alex.color(c)
 alex.forward(50)
 alex.left(90)
# Assign a list to a variable
clrs = ["yellow", "red", "purple", "blue"]
for c in clrs:
 alex.color(c)
 alex.forward(50)
 alex.left(90)
alex.penup() #pu
alex.forward(100) # This moves alex, but no line is drawn
alex.pendown() #pd
alex.shape("turtle")
alex.speed(10)
