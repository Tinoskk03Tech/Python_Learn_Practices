import turtle

turtle.title("Kossi Code")

turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0.2)
colors = ["red", "yellow", "blue", "green", "orange", "purple"]
for x in range(360):
    turtle.pencolor(colors[x % 6])
    turtle.forward(x * 3 / 1)
    turtle.left(59)
    



turtle.done()