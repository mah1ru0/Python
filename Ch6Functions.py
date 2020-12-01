

'''In a function definition, the keyword in the header is def, 
which is followed by the name of the function and some parameters enclosed in parentheses. 
The parameter list may be empty, or it may contain any number of parameters separated from one another by commas. 
In either case, the parentheses are required.
We need to say a bit more about the parameters. In the definition, 
the parameter list is more specifically known as the formal parameters. 
This list of names describes those things that the function will need to receive from the user of the function. 
When you use a function, you provide values to the formal parameters.'''


import turtle

def drawSquare(t, sz):
    '''make turtle t draw a square of with side sz.'''

    for i in range(4):
        t.fd(sz)
        t.lt(90)

wn = turtle.Screen()
wn.bgcolor("green")

alex = turtle.Turtle()
drawSquare(alex, 50)

alex.penup()
alex.goto(100,100)
alex.pendown()

drawSquare(alex, 75)

wn.exitonclick()
#-------------------------------------

'''docstrings

If the first thing after the function header is a string (some tools insist that it must be a triple-quoted string), 
it is called a docstring and gets special treatment in Python and in some of the programming tools.

Another way to retrieve this information is to use the interactive interpreter, 
and enter the expression <function_name>.__doc__, which will retrieve the docstring for the function. 
So the string you write as documentation at the start of a function is retrievable by python tools at runtime. 
This is different from comments in your code, which are completely eliminated when the program is parsed.

By convention, Python programmers use docstrings for the key documentation of their functions.'''

import turtle

def drawMulticolorSquare(t, sz):
    for i in ['black', 'blue', 'red', 'purple']:
        t.color(i)
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor("green")

tess = turtle.Turtle()
tess.pensize(3)

size = 20
for i in range(15):
    drawMulticolorSquare(tess, size)
    size = size + 10
    tess.fd(10)
    tess.right(18)

wn.exitonclick()

#--------------------------------------

def square(x):
    y = x * x
    return y

toSquare = 10
result = square(toSquare)
print("the result of", toSquare, "squared is", result)

#---------------------------------------

def square(x):
    '''raise x to the second power'''
    return x * x

import test
print('testing square function')
test.testEqual(square(10), 100)

#--First demonstration of the test module

def half(y):
    return y/2

print('testing...')
test.testEqual(half(6), 3)

def double(z):
    return z*2

print('testing...')
test.testEqual(double(6), 12)


#-----------------------------------------

def square(x):
    y = x * x
    return y

def sum_of_squares(x, y, z):
    a = square(x)
    b = square(y)
    c = square(z)
    return a + b + c

a = -5 #25
b = 2 #4
c = 10 #100
result = sum_of_squares(a, b, c)
print(result)
#---Result is 129
#-----------------------------------------

import turtle

def drawRectangle(t, w, h):
    for i in range(2):
        t.fd(w)
        t.lt(90)
        t.fd(h)
        t.lt(90)

def drawSquare(tx, sz):
    drawRectangle(tx, sz, sz)

wn = turtle.Screen()
wn.bgcolor("green")
tess = turtle.Turtle()
drawSquare(tess, 100)
wn.exitonclick()

#-----------------------------------------
'''Refined PolyGen from lab'''

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

