import turtle
turtle.pensize(10)
radius = int(input())
circlenum = int(input())
pencolor = input()
turtle.pencolor(pencolor)
turtle.circle(radius, 360)    
for i in range(circlenum-1):                
    turtle.penup()
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.down()
    turtle.circle(radius+20, 360)
    radius=radius+20
    
   
turtle.hideturtle()
turtle.down()
                         
