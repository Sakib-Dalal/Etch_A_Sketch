# Note:-
"""
    W:- To move forward
    S:- To move backward
    A:- To move left
    D:- To move right
    C:- To reset etch a sketch
    O:- To change color to black
    P:- To change color to random color
    L:- To increase pen size
    K:- To decrease pen size
"""

import turtle as t
import random


def move_forward():
    my_turtle.forward(10)


def move_backward():
    my_turtle.backward(10)


def turn_right():
    my_turtle.right(10)


def turn_left():
    my_turtle.left(10)


def clear_screen():
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()
    my_turtle.pensize(0)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors


def change_color_to_black():
    my_turtle.color("black")


def change_color_to_random():
    my_turtle.color(random_color())


def increase_pen_size():
    global pen_size
    pen_size += 2
    my_turtle.pensize(pen_size)
    print(pen_size)


def decrease_pen_size():
    global pen_size
    pen_size -= 2
    if pen_size < 0:
        pen_size = 0
    my_turtle.pensize(pen_size)
    print(pen_size)


t.colormode(255)
my_turtle = t.Turtle()
my_screen = t.Screen()
my_screen.listen()
pen_size = 0

my_screen.title("Etch A Sketch")

# movements
my_screen.onkey(key="w", fun=move_forward)
my_screen.onkey(key="s", fun=move_backward)
my_screen.onkey(key="d", fun=turn_right)
my_screen.onkey(key="a", fun=turn_left)

# functions
my_screen.onkey(key="c", fun=clear_screen)
my_screen.onkey(key="o", fun=change_color_to_black)
my_screen.onkey(key="p", fun=change_color_to_random)
my_screen.onkey(key="l", fun=increase_pen_size)
my_screen.onkey(key="k", fun=decrease_pen_size)

my_screen.exitonclick()
