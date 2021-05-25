import turtle
#Creating Screen
screen=turtle.Screen()
screen.title('2 player Pong')
screen.bgcolor('black')
screen.setup(width=800,height=600)
screen.tracer()
#Score
score_a=0
score_b=0

#Paddle A
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.color('red')
paddle_a.penup()
paddle_a.goto(-350,0)

          
#Functions to move paddle A & B

def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)
def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)
def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)
def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)


screen.listen()
screen.onkeypress(paddle_a_up,'w')
screen.onkeypress(paddle_a_down,'s')
screen.onkeypress(paddle_b_up,'Up')
screen.onkeypress(paddle_b_down,'Down')




#Paddle B

paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.color('blue')
paddle_b.penup()
paddle_b.goto(350,0)





#Ball

ball=turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('yellow')
ball.penup()
ball.goto(0,0)


ball.dx=7
ball.dy=-7








while True:
    screen.update()
    #Move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #Border checking
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *=-1

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *=-1

    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1
        score_a+=1
        
       

        
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*=-1
        score_b+=1
     


    #Paddle and ball coliding
    if ball.xcor()>340 and ball.xcor()<350 and (ball.ycor()<paddle_b.ycor()+40 and ball.ycor()>paddle_b.ycor()-50):
        ball.setx(340)
        ball.dx *=-1
    if ball.xcor()<-340 and ball.xcor()>-350 and (ball.ycor()<paddle_a.ycor()+40 and ball.ycor()>paddle_a.ycor()-50):
        ball.setx(-340)
        ball.dx *=-1
        
        


        








    
