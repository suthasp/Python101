import turtle
turtle.pensize(1)
turtle.shape("turtle")
turtle.bgcolor("yellow")
turtle.goto(0,-200)
turtle.speed(0)
for i in range(0,50,3):
   # for colors in("red","white","blue"):
        turtle.color("red")
        turtle.circle(i-200)
turtle.hideturtle()
turtle.done()    
