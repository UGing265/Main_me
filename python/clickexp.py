import turtle
 # Phuding thúc Screen0 de tao màn hinh
wn = turtle.Screen()
# Tao môt bút vē (bán chat là doi tudong rùa)
pen = turtle.Turtle()
# dinh nghia hàm de vê tam giác
def triangle(x, y):
  # nhãc bút lên
  pen.penup()
  # di chuyen tói vi trí X và y tuding ung
  pen.goto(x, y)
  # dãt bút xuong
  pen.pendown()
 # dung vòng lap for vē 3 canh tam giác
  for i in range(3):
   # vē doan thang dài 100
   pen.forward(100)
   # xoay trái 120 dô
   pen.left(120)
   # ve tiêp doan thang 100
   pen.forward(100)
# khi nhan chuôt vào màn hinh
# khi nhan chuôt vào màn hinh thi sē goi
 # hàm triangle0 dudc xây dung à trên
 # de vē tam giác
turtle.onscreenclick(triangle, 1)
# lang nghe хет có nhan chuôt vô
# màn hinh không
turtle.listen()
 # giu màn hinh
turtle.done()
