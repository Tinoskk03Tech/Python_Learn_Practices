import turtle

turtle.title("Flower Drawing with Turtle Graphics")
turtle.bgcolor("white")
turtle.speed(0.2)

def draw_flower():
    window = turtle.Screen()
    window.bgcolor("white")

    flower = turtle.Turtle()
    flower.shape("turtle")
    flower.color("red")
    flower.speed(10)

    for _ in range(36):
        for _ in range(6):
            flower.circle(50)
            flower.left(60)
        flower.right(10)

    flower.color("green")
    flower.right(90)
    flower.forward(200)

    window.exitonclick()
    
draw_flower()

turtle.done()