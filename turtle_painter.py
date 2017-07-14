# -*- coding: utf-8 -*-
"""
Created on Tue May 24 11:31:40 2016

@author: Pengcheng Li(Nathan) 
@author: Ming Zeng (Adam) 89990

"""

import turtle 
def circle():
    painter = turtle.Turtle()
    
    painter.pencolor("blue")
    
    for i in range(50):
        painter.forward(50)
        painter.left(123) # Let's go counterclockwise this time 
        
    painter.pencolor("red")
    for i in range(50):
        painter.forward(100)
        painter.left(123)
    
    painter.pencolor("green")
    for i in range(50):
        painter.forward(150)
        painter.right(123)
        
    turtle.done()
circle()
