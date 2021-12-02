'''
CS 101 Lab
Program 12 - Turtle
Keagon Madison
kcmc2f@umkc.edu

PROBLEM:
We need to use the turtle module to draw a dot, circle, filled circle, box and filled box.
This needs to be done using classes and inheritance.

ALGORITHM:
There is a class called Point. This parent class has 4 'child' classes (Box, BoxFilled, Circle, CircleFilled).
Box creates a box, boxfilled fills in a box, circle creates a circle, and circlefilled fills in a circle.

ERROR HANDLING:
No error handling was necessary.

OTHER COMMENTS:
If I were to make this at a later time, I'm sure some classes could be merged and refined. 
'''

import turtle #turtle is necessary to draw

class Point(object):
    #The parent class. Makes a colored point.
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    
    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(self.color)
        turtle.setheading(0)
        self.draw_action()

    def draw_action(self):
        #creates a dot
        turtle.dot()

class Box(Point):
    #child class which creates a box inheriting attributes from the parent class.
    def __init__(self, x1, y1, width, height, color):
        super().__init__(x1, y1, color)
        self.width = width
        self.height = height
    def draw_action(self):
        #draws the box
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)
        turtle.right(90)
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)

class BoxFilled(Box):
    #child class which creates a filled class and inherits attributes from Box.
    def __init__(self, x1, y1, width, height, color, fillcolor):
        super().__init__(x1, y1, width, height, color)
        self.fillcolor = fillcolor
    def draw_action(self):
        turtle.fillcolor(self.fillcolor)
        turtle.begin_fill()
        Box.draw_action(self) #draws the box
        turtle.end_fill()#fills the box

class Circle(Point):
    #child class which creates a circle and inherits from the parent class
    def __init__(self, x1, y1, radius, color):
        super().__init__(x1, y1, color)
        self.radius = radius
    def draw_action(self):
        turtle.circle(self.radius) #draws circle

class CircleFilled(Circle):
    #child class which creates a filled circle and inherits from Circle.
    def __init__(self, x1, y1, radius, color, fillcolor):
        super().__init__(x1, y1, radius, color)
        self.fillcolor = fillcolor
    def draw_action(self):
        turtle.fillcolor(self.fillcolor)
        turtle.begin_fill()
        Circle.draw_action(self) #draws the circle
        turtle.end_fill() #fills the circle

if __name__ == '__main__':
    p = Point(-100, 100, 'blue') 
    p.draw()

    b = Box(100, 110, 50, 40, 'red')
    b.draw()

    boxFilled = BoxFilled(1, 2, 100, 200,'red','blue')
    boxFilled.draw()

    c = Circle(-150, 200, 30, 'green')
    c.draw()

    circleFilled = CircleFilled(-150, 200, 30, 'green', 'red')
    circleFilled.draw()