from turtle import Turtle, Screen

t = Turtle()
t.shape("turtle")
t.color("#228B22")


def triangle():
    t.pencolor("yellow")
    for n in range(3):
        t.forward(100)
        t.right(120)


def square():
    t.pencolor("orange")
    for n in range(4):
        t.forward(100)
        t.right(90)


def pentagon():
    t.pencolor("red")
    for n in range(5):
        t.forward(100)
        t.right(72)


def hexagon():
    t.pencolor("pink")
    for n in range(6):
        t.forward(100)
        t.right(60)


def heptagon():
    t.pencolor("brown")
    for n in range(7):
        t.forward(100)
        t.right(51.43)


def octagon():
    t.pencolor("black")
    for n in range(8):
        t.forward(100)
        t.right(45)


def nonagon():
    t.pencolor("purple")
    for n in range(9):
        t.forward(100)
        t.right(40)


def decagon():
    t.pencolor("blue")
    for n in range(10):
        t.forward(100)
        t.right(36)


def remove_first_line():
    t.pencolor("white")
    t.forward(100)
    t.back(100)


triangle()
square()
pentagon()
hexagon()
heptagon()
octagon()
nonagon()
decagon()
remove_first_line()


screen = Screen()
screen.exitonclick()
