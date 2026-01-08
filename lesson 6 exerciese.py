#Activity 1

import turtle
bob=turtle.Turtle()
bob.forward(50)


#Activity 2

silly=turtle.Turtle()
silly.forward(90)
silly.right(90)
silly.forward(50)
silly.right(90)
silly.forward(50)
silly.right(90)
silly.forward(50)
silly.right(90)


#Activity 3 

smart=turtle.Turtle()

smart.color("violet")
smart.begin_fill()
for i in range(4):
    smart.forward(50)
    smart.right(90)
smart.end_fill()

smart.color("green")
smart.begin_fill()
smart.circle(100)

smart.end_fill()

#Activity 4

st=turtle.Turtle()
for i in range(5):
    st.forward(50)
    st.right(144)


#Activity 5

sp=turtle.Turtle()
for i in range(20):
    sp.forward(i *10)
    sp.right(144)


#Activity 7

painter=turtle.Turtle()
painter.pencolor("blue")
for i in range(50):
    painter.forward(50)
    painter.left(123)
painter.pencolor("red")
for i in range(50):
    painter.forward(100)
    painter.left(123)


#Activity 8

polygon=turtle.Turtle()

num_sides=6
side_length=70
angle=360.0/num_sides

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

#Activity 9

matrix=turtle.Turtle()
dot_distance=25
width=5
height=7
matrix.penup()

for y in range(height):
    for i in range(width):
        matrix.dot()
        matrix.forward(dot_distance)
    matrix.backward(dot_distance * width)
    matrix.right(90)
    matrix.forward(dot_distance)
    matrix.left(90)

#Activity 10

ninja=turtle.Turtle()
ninja.speed(10)
for i in range(180):
    ninja.forward(100)
    ninja.right(30)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(50)
    ninja.right(30)
    ninja.penup()
    ninja.setposition(0,0)
    ninja.pendown()
    ninja.right(2)


