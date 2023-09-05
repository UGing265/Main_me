import turtle
red1 = turtle.Turtle()
red2 = turtle.Turtle()
red2.dot(10000,"black")

red1.pencolor("red")
red2.pencolor("red")

red1.penup()
red2.penup()
red1.goto(0,-480)
red2.goto(0,-480)
red1.pendown()
red2.pendown()
red1.speed(0)
red2.speed(0)

red1.left(150)
red2.left(30)
for x in range(30): #đi thẳng
  red1.forward(8)
  red1.right(0.2)
  red1.circle(-x)
  red2.forward(8)
  red2.left(0.2)
  red2.circle(x)
for x in range(30,60): #cong 1 chút
  red1.forward(8)
  red1.right(0.5)
  red1.circle(-x)
  red2.forward(8)
  red2.left(0.5)
  red2.circle(x)
for x in range(60,80): #cong tiep
  red1.forward(8)
  red1.right(0.4)
  red1.circle(-x)
  red2.forward(8)
  red2.left(0.4)
  red2.circle(x)
for x in range(80,175):#cong gap
  red1.forward(9.5)
  red1.right(1.5)
  red1.circle(-x)
  red2.forward(9.5)
  red2.left(1.5)
  red2.circle(x)
for x in range(175,200):#cong nhe ti nua
  red1.forward(9.5)
  red1.right(1)
  red1.circle(-x)
  red2.forward(9.5)
  red2.left(1)
  red2.circle(x)

red1.penup()
red2.penup()
red1.goto(0,-100)

turtle.done()








