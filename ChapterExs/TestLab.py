
import turtle

def drawPoly(t, sideLength, numSides):
    for i in range(numSides):
        t.fd(sideLength)
        t.lt(360/numSides)

wn = turtle.Screen()
wn.bgcolor("green")
jen = turtle.Turtle()

drawPoly(jen, 30, 10)

wn.exitonclick()