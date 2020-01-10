# Screen Snake game in Python 3 using turtle

import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0

# Set up screen
wn = turtle.Screen()
wn.title("Screen Snake by Brendan")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)

# Head of the snake
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("dim grey")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Snake body list
segments = []

# Score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0   High Score: 0", align="center", font=("Courier", 24, "normal"))


# Functions
def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)

    if head.direction == "down":
        head.sety(head.ycor() - 20)

    if head.direction == "right":
        head.setx(head.xcor() + 20)

    if head.direction == "left":
        head.setx(head.xcor() - 20)


def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def restart_game():
    time.sleep(1.5)
    # Pseudo way to delete the segments
    for seg in segments:
        seg.goto(1000, 1000)

    segments.clear()
    head.goto(0, 0)


# Keyboard
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Main loop for the game
while True:
    wn.update()

    # Check for collision with the food
    if head.distance(food) < 20:  # each turtle is 20x20 pixels
        # Move food to random location
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add segment
        new_seg = turtle.Turtle()
        new_seg.speed(0)
        new_seg.shape("square")
        new_seg.color("grey")
        new_seg.penup()
        segments.append(new_seg)

        # Shorten the delay
        delay -= 0.0005

        # Increase score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Move the end segments first
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    # Move segment zero to the head location
    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    # Border collision check
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        score = 0
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
        restart_game()
    
    move()

    # Body collision check
    for seg in segments:
        if seg.distance(head) < 20:
            score = 0
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",font=("Courier", 24, "normal"))
            restart_game()
    
    time.sleep(delay)

wn.mainloop()
