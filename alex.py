import turtle                     #allows us to use the turtle library
wn = turtle.Screen()
wn.bgcolor = ("lightgreen")       #Creates a graphic window

alex = turtle.Turtle()            #Creates a turtle named alex
alex.color("hotpink")
alex.pensize(5)

tess = turtle.Turtle()
tess.color("blue")
tess.pensize(5)

tess.forward(50)
tess.left(120)
tess.forward(50)
tess.left(120)
tess.forward(50)

alex.forward(320)                 #Tell alex to move forwad by 150 units
alex.left(90)                     #turn 90 degress
alex.forward(100)                 #Complete the second side of the rectangle
alex.left(90)
alex.forward(320)
alex.left(90)
alex.forward(100)


wn.exitonclick()




