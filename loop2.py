import turtle
wn = turtle.Screen()
wn.bgcolor("black")

tess = turtle.Turtle()
tess.color("white")
tess.shape("turtle")

dist = 5
tess.up()	#lifts up the turtle
for _ in range(40):		#Start with size 2 and grow by 2
	tess.stamp()		#Leave an impression on canvas
	tess.forward(dist)	#Move tess along
	tess.right(24)		#and turn her
	dist = dist + 2
wn.exitonclick()
