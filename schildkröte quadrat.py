import turtle
import time
wn=turtle.Screen()
wn.bgcolor("black")

quadrat=turtle.Turtle
quadrat=turtle.color("red")

def my_function(quadrat):
    for q in range(4):
        turtle.fd(100)
        turtle.rt(90)

my_function(quadrat)
