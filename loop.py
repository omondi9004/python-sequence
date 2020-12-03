import turtle
wn = turtle.Screen()

elan = turtle.Turtle()
distance = 50
angle = 90

for _ in range(18):
	elan.forward(distance)
	elan.right(angle)
	distance = distance + 20
	angle = angle - 3


