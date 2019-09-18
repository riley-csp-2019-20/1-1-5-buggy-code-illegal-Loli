import turtle as trtl
trtl.goto(0,55) 
trtl.pensize(20)
trtl.circle(10)




x = trtl.Turtle()
x.pensize(40)
x.circle(20)
w = 9
y = 70
z = 360 / w
x.pensize(5)
n = 0
while (n < w):
  x.goto(0,0)
  x.setheading(z*n)
  x.forward(y)
  n = n + 1

trtl.goto(-10,65) 
trtl.color("red")
trtl.pensize(5)
trtl.circle(3)


trtl.penup()
trtl.goto(10,65) 
trtl.pendown()
trtl.color("red")
trtl.pensize(5)
trtl.circle(3)

x.hideturtle()
wn = trtl.Screen()
wn.mainloop()