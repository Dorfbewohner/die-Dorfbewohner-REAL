import turtle

window = turtle.Screen()
window.bgcolor ("black")

brandon = turtle.Turtle()
brandon.fillcolor('blue')
brandon.pencolor('blue')
brandon.pensize(2)

def schildkroete (t,s):
    for i in range(4):
        t.forward(s)
        t.left(90)
for _ in range (20):
    brandon.left(18)
    schildkroete (brandon,50)
    
