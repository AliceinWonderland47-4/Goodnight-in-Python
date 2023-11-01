import turtle
import math

text = "晚安，好梦"

# Draw a heart
turtle.penup()
turtle.goto(0, 150)
turtle.down()
turtle.color('red')
turtle.begin_fill()
turtle.fillcolor('red')
turtle.speed(1)
turtle.left(45)
turtle.forward(150)
turtle.right(45)
turtle.forward(100)
turtle.right(45)
turtle.forward(100)
turtle.right(45)
turtle.forward(100)
turtle.right(45)
turtle.forward(250 + math.sqrt(2) * 100)
turtle.right(90)
turtle.speed(2)
turtle.forward(250 + 100 * math.sqrt(2))
turtle.right(45)
turtle.forward(100)
turtle.right(45)
turtle.forward(100)
turtle.right(45)
turtle.forward(100)
turtle.right(45)
turtle.forward(150)
turtle.end_fill()

# Say the words
turtle.goto(0, 50)
turtle.pencolor('white')

turtle.pu()
x = len(text)
for i in text:
    turtle.write(i, font=('consolas', 24, 'normal'))
    turtle.rt(360 / x)
    turtle.pu()
    turtle.fd(30)

turtle.hideturtle()
turtle.exitonclick()
