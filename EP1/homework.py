from turtle import *
import turtle
tao = turtle.Pen()
tao.shape('turtle')
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(150)
    if abs(pos()) < 1:
        break
end_fill()
done()
