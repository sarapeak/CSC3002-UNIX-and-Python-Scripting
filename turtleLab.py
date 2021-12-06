# -*- coding: utf-8 -*-
"""
Created on Sat May 15 23:16:57 2021

@author: sarap
"""
import turtle

#Creates the trunk of the tree 
def trunk(x,y,z):
    #loops through it twice to make a rectangle
    for i in range(2):
        turtle.forward(x)
        turtle.left(y)
        turtle.forward(z)
        turtle.left(y)

#Creates the leaves of the tree
def makeLeaves():
    turtle.color("green")
    turtle.setposition(-58,20)  #sets the postion for the first circle
    turtle.pendown() #puts the pen down to start drawing
    turtle.begin_fill()
    turtle.circle(30) #makes a circle
    turtle.end_fill()
    turtle.penup()   #puts the pen up to stop drawing
    turtle.setposition(-2,20)   #Sets the position for the second circle
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()
    turtle.penup()
    turtle.setposition(-30,55)   #sets the position for the third circle
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()
    turtle.penup()
    
#Creates the fruit in the tree
def makeFruit(fruit, size, x, y):
    turtle.setposition(x, y)  #sets the original postion
    turtle.pensize(5)   #creates a thicker outline for the fruit
    #loops through the number of colors
    for i in fruit:
        turtle.fillcolor(i) #makes the fill the color in the list
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(size) #sets the size of the fruit
        turtle.end_fill()
        turtle.penup()
        turtle.setposition(x+40,y+17) #finds a new position
        size = size+3  #finds a new size for the fruit

turtle.penup()
turtle.color("brown")  #sets the color to brown
turtle.setposition(-45,-75)  #sets the starting position
turtle.begin_fill()  #begins to fill the trunk
turtle.pendown()
trunk(30,90,125)   #calls on the trunk function
turtle.end_fill()  #stops the fill
turtle.penup()
makeLeaves()  #calls on the make leaves function
fruitColors=["red", "yellow"] #creates a list of colors
makeFruit(fruitColors,10,-50,30) #calls on the make fruit function
turtle.setposition(-50, 125) #goes to a different postion
turtle.color("white") #sets the color to white
#writes text to the canvas
turtle.write("A lonely tree on a lonely plain", True, align="center", font=(10))
turtle.bgcolor("blue")  #changes the background to blue
turtle.exitonclick()