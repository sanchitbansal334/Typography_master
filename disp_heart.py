import turtle

def display_heart():
    def curve(x) :
        for i in range(200):
            x.right(1)
            x.forward(1)

    a = turtle.Turtle()
    a.pensize(3)
    a.speed(30)
    a.color("red" , "pink")
    a.up()
    a.right(90)
    a.forward(200)
    a.left(90)
    a.down()
    a.begin_fill()
    a.left(140)
    a.forward(111.65)
    curve(a)

    a.left(120)
    curve(a)
    a.forward(111.65)
    a.end_fill()
    a.hideturtle()
