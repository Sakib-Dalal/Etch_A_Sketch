# Note:-
"""
    W:- To move forward
    S:- To move backward
    A:- To move left
    D:- To move right
    C:- To reset etch a sketch
"""

import turtle as t


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


my_turtle = t.Turtle()
my_screen = t.Screen()
my_screen.listen()

my_screen.onkey(key="w", fun=move_forward)
my_screen.onkey(key="s", fun=move_backward)
my_screen.onkey(key="d", fun=turn_right)
my_screen.onkey(key="a", fun=turn_left)
my_screen.onkey(key="c", fun=clear_screen)

my_screen.exitonclick()
