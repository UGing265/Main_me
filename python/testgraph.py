import turtle
a = turtle.Turtle()
b = turtle.Turtle() 
c = turtle.Turtle()
d = turtle.Turtle()
e = turtle.Turtle()



a.pencolor("red")
a.dot(10000,"black")
b.pencolor("yellow")
c.pencolor("blue")
d.pencolor("white")
e.pencolor("green")

a.speed(0)
b.speed(0)
c.speed(0)
d.speed(0)
e.speed(0)

d.right(90)
c.right(90)
e.left(76)
for x in range(50):
 a.forward(4)
 a.left(0.5)
 a.circle(x)
 b.back(4)
 b.right(0.5)
 b.circle(x)
 c.forward(3)
 c.circle(x)
 d.forward(3)
 d.circle(-x)
 e.circle(x)
 e.forward(3.5)
#for x in range(1000):
 #turtle.forward(x)
# turtle.circle(91)

for x in range(50,1000):
 a.forward(4)
 a.left(-1)
 a.circle(x)
 b.back(5)
 b.right(-1)
 b.circle(x)
 c.forward(4)
 c.circle(x)
 c.left(0.5)
 d.forward(4)
 d.circle(-x)
 d.right(0.5)
 e.circle(x)
 e.forward(3)
 

