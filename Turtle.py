import turtle

sc = turtle.Screen()
pen = turtle.Turtle()

def semi_circle(col, rad, val):
    pen.color(col)
    pen.circle(rad, -360)
    pen.up()
    pen.setpos(val, 0)
    pen.down()
    pen.right(360)

col = ['violet', 'indigo', 'blue', 'green', 'yellow','pink', 'orange', 'red']
sc.setup(600, 600)
sc.bgcolor('gray')    
pen.right(90)
pen.width(20)
pen.speed(8)
for i in range(8):
    semi_circle(col[i], 13*(i + 8), -13*(i + 1))
pen.hideturtle()    