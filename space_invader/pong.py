import turtle

wn = turtle.Screen()
wn.title("Pong by Yitianiscool")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

padA = turtle.Turtle()
padA.speed(0)
padA.shape("square")
padA.color("white")
padA.shapesize(stretch_wid = 5, stretch_len=1)
padA.penup()
padA.goto(-350, 0)

padB = turtle.Turtle()
padB.speed(0)
padB.shape("square")
padB.color("white")
padB.shapesize(stretch_wid = 5, stretch_len=1)
padB.penup()
padB.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.shapesize(stretch_wid = 1, stretch_len=1)
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

scoreA = 0
scoreB = 0

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))

def padA_up():
    y = padA.ycor()
    y += 20
    if y < 290:
        padA.sety(y)

def padA_down():
    y = padA.ycor()
    y -= 20
    if y > -290:
        padA.sety(y)

def padB_up():
    y = padB.ycor()
    y += 20
    if y < 290:
        padB.sety(y)

def padB_down():
    y = padB.ycor()
    y -= 20
    if y > -290:
        padB.sety(y)

wn.listen()
wn.onkeypress(padA_up, "w")
wn.onkeypress(padA_down, "s")
wn.onkeypress(padB_up, "Up")
wn.onkeypress(padB_down, "Down")

while True:
    wn.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
        scoreA += 1
        ball.goto(0, 0)
    if ball.xcor() < -390:
        scoreB += 1
        ball.goto(0, 0)
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < padB.ycor() + 40 and ball.ycor() > padB.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < padA.ycor() + 40 and ball.ycor() > padA.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
    pen.clear()
    pen.write("Player A: {} Player B: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "normal"))
