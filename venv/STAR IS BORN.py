import turtle

ninja = turtle
ninja.speed(20)
side = 20
ninja.penup()
ninja.goto(-20,-20)
ninja.pendown()




def star():
    for i in range(5):
        ninja.forward(side)
        ninja.right(144)

for i in range(65):
    star()
    ninja.right(5)
    side += 2

ninja.penup()
ninja.goto(250,100)
ninja.pendown()
ninja.color("orange")
side = 20




for i in range(65):
    star()
    ninja.right(5)
    side += 2

ninja.penup()
ninja.goto(-250,100)
ninja.pendown()
ninja.color("red")
side = 20




for i in range(65):
    star()
    ninja.right(5)
    side += 2

















ninja.exitonclick()