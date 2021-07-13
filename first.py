import turtle
list=["purple","blue","red","orange","green","yellow","black"]
turtle.bgcolor("white")
turtle.speed(0)
for i in range(250):
    turtle.color(list[i%7])
    turtle.pensize(10)
    turtle.forward(i)
    turtle.left(59)
turtle.hideturtle()
turtle.done;