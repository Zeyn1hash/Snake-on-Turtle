from turtle import*
from random import*
from time import sleep

class Snake(Turtle):
    def __init__(self, x, y, color, shape, speed, step, direction=None):
        Turtle.__init__(self)
        self.penup()
        self.color(color)
        self.shape(shape)
        self.speed(speed)
        self.goto(x, y)
        self.step=step
        self.direction=direction
    
    def move(self):
        self.forward(self.step)
    
    def move_up(self):
        self.setheading(90)
        self.direction="up"
    
    def move_down(self):
        self.setheading(-90)
        self.direction="down"
    
    def move_left(self):
        self.setheading(180)
        self.direction="left"
    
    def move_right(self):
        self.setheading(0)
        self.direction="right"
    
    def touch(self, sprite):
        dist=self.distance(sprite.xcor(), sprite.ycor())
        if dist<=30:
            return True
        else:
            return False
head=Snake(0, 0, "green", "square", 0, 20)
apple=Snake(randint(-190, 220), randint(-220, 180), "red", "circle", 0, 0)
builder=Turtle()

col=choice(["limegreen", "black", "gray", "orange"])

builder.speed(0)
builder.width(10)
builder.color(col)
builder.up()
builder.goto(-250, 250)
builder.down()
builder.right(90)
builder.begin_fill()
for i in range(4):
    builder.forward(500)
    builder.left(90)
builder.end_fill()

def square():
    if col=="limegreen":
        builder.color("green")
        col1="darkgreen"
        col2="lime"
    elif col=="black":
        builder.color("darkgray")
        col1="darkgray"
        col2="lightgray"
    elif col=="gray":
        builder.color("gray")
        col1="darkgray"
        col2="lightgray"
    elif col=="orange":
        builder.color("darkorange")
        col1="orangered"
        col2="gold"
    builder.begin_fill()
    for i in range(4):
        builder.forward(50)
        builder.left(90)
    builder.end_fill()

    builder.color(col1)
    for i in range(2):
        builder.forward(50)
        builder.left(90)
    builder.color(col2)
    for i in range(2):
        builder.forward(50)
        builder.left(90)
    builder.up()
    builder.forward(60)
    builder.down()

#coordinates=Turtle()
#coordinates.up()
#coordinates.goto(-200, -230)

for i in range(9):
    square()
for i in range(8):
    builder.left(90)
    builder.up()
    builder.forward(60)
    builder.left(90)
    builder.forward(60)
    builder.right(180)
    builder.down()
    square()
for i in range(8):
    builder.up()
    builder.goto(builder.xcor(), builder.ycor()+120)
    builder.down()
    square()
for i in range(7):
    builder.up()
    builder.goto(builder.xcor()-60, builder.ycor()+60)
    builder.down()
    square()
builder.hideturtle()

#coordinates.goto(230, 190)

pen = Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.down()
pen.goto(0, 0)
pen.write("Score : 0  High Score : 0", align="center",
          font=("candara", 24, "bold"))

scr=head.getscreen()
scr.listen()
scr.onkey(head.move_up, "W")
scr.onkey(head.move_down, "S")
scr.onkey(head.move_left, "A")
scr.onkey(head.move_right, "D")

score=0
high_score=0
#-200 230
#-230 190
segments=list()

while True:
    if head.xcor() >= 220 or head.xcor() <= -210 or head.ycor() >= 180 or head.ycor() <= -210:
        sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"
        #colors = choice(['red', 'blue', 'green'])
        #shapes = choice(['square', 'circle'])
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))
    if head.distance(apple) < 20:
        x = randint(-190, 220)
        y = randint(-220, 180)
        apple.goto(x, y)
 
        # Adding segment
        new_segment = Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")  # tail colour
        new_segment.penup()
        segments.append(new_segment)
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))
    # Checking for head collisions with body segments
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    head.move()
    for segment in segments:
        if segment.distance(head) < 20:
            head.goto(0, 0)
            head.direction = "stop"
            colors = choice(['red', 'blue', 'green'])
            shapes = choice(['square', 'circle'])
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
 
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(
                score, high_score), align="center", font=("candara", 24, "bold"))
