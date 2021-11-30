import turtle
import os
import winsound

# create a window
wn = turtle.Screen()
wn.title("Pong by Jasmine")
wn.bgcolor("black")
# size of the window
wn.setup(width=800, height=600)
# it stops the window from updating, helps speeding our game.
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
# it's the speed of Animation not the speed at which our paddle moves
paddle_a.speed (0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
# to avoid drawing a line
paddle_a.penup()
# start our paddle at
paddle_a.goto(-350, 0) # -350 is the X-axis


# Paddle B
paddle_b = turtle.Turtle()
# it's the speed of Animation not the speed at which our paddle moves
paddle_b.speed (0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
# to avoid drawing a line
paddle_b.penup()
# start our paddle at
paddle_b.goto(350, 0) # -350 is the X-axis

# Ball
ball = turtle.Turtle()
# it's the speed of Animation not the speed at which our paddle moves
ball.speed (0)
ball.shape("circle")
ball.color("white")
# to avoid drawing a line
ball.penup()
# start our paddle at
ball.goto(0, 0) # start in the middle of the screen
# d means delta or change
# everytime our ball moves, it moves by 2 pixels
ball.dx = 0.1
ball.dy = -0.1

# Pen
pen = turtle.Turtle()
# animation speed not the movement speed
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Function
def paddle_a_up():
    # to know the current Y-coordinate
    # ycor() method returns the Y-coordinate
    y = paddle_a.ycor()
    # add 20 pixels to the Y-coordinate
    y += 20
    # sets y to the new y
    paddle_a.sety(y)

def paddle_a_down():
    # to know the current Y-coordinate
    # ycor() method returns the Y-coordinate
    y = paddle_a.ycor()
    # subtract 20 pixels to the Y-coordinate
    y -= 20
    # sets y to the new y
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard binding
wn.listen() # this will listen for keyboard input
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main Game Loop
# everytime the loop runs, it updates the screen
while True:
    wn.update()

    # Move the ball
    # take current x-coordinate
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    # once it gets to a certain point, it should bounce
    if ball.ycor() > 290:
        ball.sety(290)
        # it reverses the direction
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC) # when it touches the top

    if ball.ycor() < -290:
        ball.sety(-290)
        # it reverses the direction
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC) # when it touches the bottom

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1 # add 1 to Player A's score
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1  # add 1 to Player B's score
        # clears whatever is there in the screen
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC) # when it touches the paddle

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC) # when it touches the paddle