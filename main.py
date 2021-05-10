import turtle # This is a module that makes it possible to build a window
import winsound # This is used to import sound into the program

win = turtle.Screen() # This creates the screen
win.title("Pong by @TokyoEdTech") # This is the title of the window
win.bgcolor("black") # Set the background color to black
win.setup(width=800, height=600) # Set up the size of the screen
win.tracer(0) # It stops the window from updating and make the game quicker
# If you don't do this the game would be much slower

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle() # It creates a turtle object and assign it to "paddle_a"
paddle_a.speed(0) # Speed of the animation. The 0 value is the maximum speed
paddle_a.shape("square") # Shape of the paddle a
paddle_a.color("blue") # Color of the paddle a
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # This streches the square and makes a rectangle with this size: 1x5
paddle_a.penup() # This put the penup. This means that it won't show the line of the pen
paddle_a.goto(-350,0) # This sets the initial position of the object

# Paddle B
paddle_b = turtle.Turtle() # It creates a turtle object and assign it to "paddle_b"
paddle_b.speed(0) # Speed of the animation. The 0 value is the maximum speed
paddle_b.shape("square") # Shape of the paddle b
paddle_b.color("blue") # Color of the paddle b
paddle_b.shapesize(stretch_wid=5, stretch_len=1) # This streches the square and makes a rectangle with this size: 1x5
paddle_b.penup() # This put the penup. This means that it won't show the line of the pen
paddle_b.goto(350,0) # This sets the initial position of the object

# Ball
# The ball isn't streched, so it is a square
ball = turtle.Turtle() # It creates a turtle object and assign it to "ball"
ball.speed(0) # Speed of the animation. The 0 value is the maximum speed
ball.shape("square") # Shape of the ball
ball.color("yellow") # Size of the ball
ball.penup() # This put the penup. This means that it won't show the line of the pen
ball.goto(0,0) # This sets the initial position of the object
ball.xspeed = 0.1 # This sets the X axis speed. It can also be written as ball.dx = 0.1
ball.yspeed = 0.1 # This sets the Y axis speed. It can also be written as ball.dy = 0.1

# Pen
pen = turtle.Turtle() # It creates a turtle object and assign it to "pen"
pen.speed(0) # Speed of the animation. The 0 value is the maximum speed
pen.color("white") # Size of the ball
pen.penup() # This put the penup. This means that it won't show the line of the pen
pen.hideturtle() # This will hide the entire object (pen) and show only what it has written
pen.goto(0, 260) # This sets the initial position of the object
pen.write("Player A: 0  Player B: 0", align= "center", font=("Courier", 24, "normal"))
# The line above is what the pen will write

# Movements of the paddles
def paddle_a_up():
    # This adds 20 to the Y cordinates of the paddle a (move a up)
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    # This subtracts 20 to the Y cordinates of the paddle a (move a down)
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    # This adds 20 to the Y cordinates of the paddle b (move b up)
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    # This subtracts 20 to the Y cordinates of the paddle b (move b down)
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard binding
# This sets the functions above to specific keys on the keyboard
win.listen() # This prepares the program to listen for keys inputs
win.onkeypress(paddle_a_up,"w") # "w" makes paddle a go up
win.onkeypress(paddle_a_down,"s") # "s" makes paddle a go down
win.onkeypress(paddle_b_up,"Up") # Key "Up" makes the paddle b go up
win.onkeypress(paddle_b_down,"Down") # Key "Down" makes the paddle b go down

# Main game loop
while True: # It means that it'll loop forever
    win.update() # Every time the loop runs the window updates

    # Move the ball
    ball.setx(ball.xcor() + ball.xspeed) # It adds the current X coordinate to the ball X speed(0.1)
    ball.sety(ball.ycor() + ball.yspeed) # It adds the current Y coordinate to the ball Y speed(0.1)

    # Border checking

    # Top and bottom
    if ball.ycor() > 290: # It checks if the ball is on the top bezel
        ball.sety(290)
        ball.yspeed *= -1 # It reverses the movement of the ball, in this case it goes down
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC) # When this happens the sound is played
    
    if ball.ycor() < -290: # It checks if the ball is on the bottom bezel
        ball.sety(-290)
        ball.yspeed *= -1 # It reverses the movement of the ball, in this case it goes up
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC) # When this happens the sound is played
    
    # Left and right
    if ball.xcor() > 390: # It checks if the ball is on the top bezel
        ball.goto(0,0) # If the ball goes to the right bezel it comes back to the initial position
        ball.xspeed *= -1 # It reverses the movement of the ball, in this case it goes left
        score_a += 1 # If the ball goes to the right, the player a, which is the left one, gets one point
        pen.clear() # It'll clear the pen so the score gets updated
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align= "center", font=("Courier", 24, "normal")) 
        # The line above updates the score

    if ball.xcor() < -390: # It checks if the ball is on the bottom bezel
        ball.goto(0,0) # If the ball goes to the left bezel it comes back to the initial position
        ball.xspeed *= -1 # It reverses the movement of the ball, in this case it goes right
        score_b += 1 # If the ball goes to the left, the player b, which is the right one, gets one point
        pen.clear() # It'll clear the pen so the score gets updated
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align= "center", font=("Courier", 24, "normal")) 
        # The line above updates the score
    
    # Paddle and ball colisions
    if (350 > ball.xcor() > 340) and (paddle_b.ycor() - 40 < ball.ycor() < paddle_b.ycor() + 40): 
        # The line above checks if the X coordinate of the ball is between the right & left and the top & bottom borders of the paddle b
        ball.setx(340)
        ball.xspeed *= -1 # It reverses the movement of the ball
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC) # When this happens the sound is played
    
    if (-340 > ball.xcor() > -350) and (paddle_a.ycor() - 40 < ball.ycor() < paddle_a.ycor() + 40): 
        # The line above checks if the X coordinate of the ball is between the right & left and the top & bottom borders of the paddle a
        ball.setx(-340)
        ball.xspeed *= -1 # It reverses the movement of the ball
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC) # When this happens the sound is played