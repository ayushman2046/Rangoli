from turtle import *
def drcircle(vivan,x,y,radius,color):
    vivan.up()
    vivan.goto(x,y)
    vivan.down()
    vivan.begin_fill()
    vivan.circle(radius)
    vivan.fillcolor(color)
    vivan.end_fill()
    vivan.up()
    vivan.home()
def rou(azad,x,y,colorr):
    #azad = Turtle()
    azad.up()
    azad.goto(x,y)
    azad.down()
    for i in range(40):
        azad.pensize(i // 10 + 1)
        azad.color(colorr[i % 9])
        azad.forward(i)
        azad.left(59)
    vivan.up()
    vivan.home()
wh = Screen()
wh.bgcolor("white")
abhinav  = Turtle()
abhinav.speed(20)
abhinav.begin_fill()
abhinav.color("turquoise")
abhinav.fillcolor("navy")
abhinav.up()
abhinav.pensize(10)
abhinav.goto(0,-330)
abhinav.down()
abhinav.circle(370,360,3)
#bgcolor("white")
abhinav.up()
abhinav.pensize(10)
abhinav.goto(0,410)
abhinav.down()
#abhinav.color("dark green")
abhinav.setheading(-180)
abhinav.circle(370,360,3)
abhinav.end_fill()
abhinav.hideturtle()
vivan = Turtle()

#bgcolor("white")
vivan.speed(20)
vivan.shape("turtle")
vivan.pensize(3)
vivan.color("black")
drcircle(vivan,0,-140,180,"maroon")
vivan.color("white")
drcircle(vivan,0,-60,100,"dark blue")
drcircle(vivan,0,140,40,"black")
drcircle(vivan,0,-140,40,"black")
drcircle(vivan,-140,0,40,"black")
drcircle(vivan,140,0,40,"black")
#drcircle(vivan,0,0,40,"green")
colorr = ["green","red","violet","gold","silver","teal","yellow","blue","maroon"]
vivan.speed(20)
drcircle(vivan,100,100,40,"black")
drcircle(vivan,100,-100,40,"black")
drcircle(vivan,-100,100,40,"black")
drcircle(vivan,-100,-100,40,"black")
rou(vivan,140,40,colorr)
rou(vivan,-140,40,colorr)
rou(vivan,0,180,colorr)
rou(vivan,0,-100,colorr)
rou(vivan,100,140,colorr)
rou(vivan,-100,140,colorr)
rou(vivan,100,-60,colorr)
rou(vivan,-100,-60,colorr)
abhinav = Turtle()
abhinav.color("yellow")
abhinav.up()
abhinav.pensize(15)
abhinav.goto(0,40)
abhinav.down()
abhinav.lt(90)
abhinav.fd(50)
abhinav.rt(90)
abhinav.fd(50)
abhinav.up()
abhinav.goto(0,40)
abhinav.down()
abhinav.setheading(270)
abhinav.fd(50)
abhinav.rt(90)
abhinav.fd(50)
abhinav.up()
abhinav.goto(0,40)
abhinav.down()
abhinav.setheading(180)
abhinav.fd(50)
abhinav.rt(90)
abhinav.fd(50)
abhinav.up()
abhinav.goto(0,40)
abhinav.down()
abhinav.setheading(360)
abhinav.fd(50)
abhinav.rt(90)
abhinav.fd(50)
abhinav.up()
abhinav.goto(25,65)
abhinav.down()
abhinav.begin_fill()
abhinav.fillcolor("maroon")
abhinav.circle(1)
abhinav.end_fill()
abhinav.up()
abhinav.goto(25,15)
abhinav.down()
abhinav.begin_fill()
abhinav.fillcolor()
abhinav.circle(1)
abhinav.end_fill()
abhinav.up()
abhinav.goto(-25,65)
abhinav.down()
abhinav.begin_fill()
abhinav.fillcolor("maroon")
abhinav.circle(1)
abhinav.end_fill()
abhinav.up()
abhinav.goto(-25,15)
abhinav.down()
abhinav.begin_fill()
abhinav.fillcolor("maroon")
abhinav.circle(1)
abhinav.end_fill()
abhinav.up()
abhinav.hideturtle()
abhinav.home()
ayushman = Turtle()
ayushman.up()
ayushman.goto(0,-200)
ayushman.down()
ayushman.pensize(20)
show = ("courier",30,"bold")
abhinav = Turtle()
abhinav.speed(20)
abhinav.color("orange")
abhinav.up()
abhinav.goto(0,-170)
abhinav.down()
abhinav.pensize(57)
abhinav.circle(210)
abhinav.color("indigo")
abhinav.up()
abhinav.goto(0,-210)
abhinav.down()
abhinav.pensize(5)
abhinav.color("black")
abhinav.up()
abhinav.goto(0,-200)
abhinav.down()
abhinav.circle(240)
circ = Turtle()
circ.speed(20)
circ.begin_fill()
circ.up()
circ.goto(-330,-20)
circ.down()
circ.pensize(5)
circ.fillcolor("maroon")
circ.circle(60)
circ.end_fill()
circ.up()
circ.goto(-330,0)
circ.down()
circ.begin_fill()
circ.fillcolor("chocolate")
circ.circle(40)
circ.end_fill()
circ.up()
circ.goto(-330,20)
circ.down()
circ.begin_fill()
circ.fillcolor("violet")
circ.circle(20)
circ.end_fill()
circ.begin_fill()
circ.up()
circ.goto(330,-20)
circ.down()
circ.pensize(5)
circ.fillcolor("maroon")
circ.circle(60)
circ.end_fill()
circ.up()
circ.goto(330,0)
circ.down()
circ.begin_fill()
circ.fillcolor("chocolate")
circ.circle(40)
circ.end_fill()
circ.up()
circ.goto(330,20)
circ.down()
circ.begin_fill()
circ.fillcolor("violet")
circ.circle(20)
circ.end_fill()
circ.begin_fill()
circ.up()
circ.goto(170,250)
circ.down()
circ.pensize(5)
circ.fillcolor("maroon")
circ.circle(60)
circ.end_fill()
circ.up()
circ.goto(170,270)
circ.down()
circ.begin_fill()
circ.fillcolor("chocolate")
circ.circle(40)
circ.end_fill()
circ.up()
circ.goto(170,290)
circ.down()
circ.begin_fill()
circ.fillcolor("violet")
circ.circle(20)
circ.end_fill()
circ.begin_fill()
circ.up()
circ.goto(-170,250)
circ.down()
circ.pensize(5)
circ.fillcolor("maroon")
circ.circle(60)
circ.end_fill()
circ.up()
circ.goto(-170,270)
circ.down()
circ.begin_fill()
circ.fillcolor("chocolate")
circ.circle(40)
circ.end_fill()
circ.up()
circ.goto(-170,290)
circ.down()
circ.begin_fill()
circ.fillcolor("violet")
circ.circle(20)
circ.end_fill()
circ.begin_fill()
circ.up()
circ.goto(-170,-290)
circ.down()
circ.pensize(5)
circ.fillcolor("maroon")
circ.circle(60)
circ.end_fill()
circ.up()
circ.goto(-170,-270)
circ.down()
circ.begin_fill()
circ.fillcolor("chocolate")
circ.circle(40)
circ.end_fill()
circ.up()
circ.goto(-170,-250)
circ.down()
circ.begin_fill()
circ.fillcolor("violet")
circ.circle(20)
circ.end_fill()
circ.begin_fill()
circ.up()
circ.goto(170,-290)
circ.down()
circ.pensize(5)
circ.fillcolor("maroon")
circ.circle(60)
circ.end_fill()
circ.up()
circ.goto(170,-270)
circ.down()
circ.begin_fill()
circ.fillcolor("chocolate")
circ.circle(40)
circ.end_fill()
circ.up()
circ.goto(170,-250)
circ.down()
circ.begin_fill()
circ.fillcolor("violet")
circ.circle(20)
circ.end_fill()
vivan.hideturtle()
circ.hideturtle()
abhinav.hideturtle()
ayushman.hideturtle()
done()
