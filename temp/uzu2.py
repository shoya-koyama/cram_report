import turtle

def draw_spiral():
    turtle.speed(0)
    turtle.bgcolor("white")
    colors = ["red", "yellow", "blue", "green"]
    for x in range(100):
        turtle.pencolor(colors[x % 4])
        turtle.forward(x * 2)
        turtle.left(91)

draw_spiral()
turtle.done()