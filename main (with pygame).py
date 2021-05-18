import pygame
from playsound import playsound
pygame.font.init()

# VARIABLES
width, height = 800, 600
win = pygame.display.set_mode((width,height))
pygame.display.set_caption('Pong')
font = pygame.font.SysFont('courier', 45)

class Paddle:
    def __init__(self, color, x, y, xspeed, yspeed, score=0):
        self.color = color
        self.x = x
        self.y = y
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.score = score

    def draw(self):
        pygame.draw.rect(win, self.color, (self.x, self.y, 20,150))

class Ball:
    def __init__(self, color, x, y, xspeed=0.2, yspeed=0.2):
        self.color = color
        self.x = x
        self.y = y
        self.xspeed = xspeed
        self.yspeed = yspeed
    
    def draw(self):
        pygame.draw.rect(win, self.color, (self.x, self.y, 20,20))

def draw_window(player1, player2, ball):
    player1.draw()
    player2.draw()
    ball.draw()
    text = font.render('Player A: {}  Player B: {}'.format(player1.score, player2.score), 1, (255,255,255))
    win.blit(text, (width/2 - text.get_width()/2, 40))

def main():
    run = True
    paddle_a = Paddle((0,0,255), 50, 225, 20,20)
    paddle_b = Paddle((0,0,255), 730, 225, 20,20)
    ball = Ball((255,255,0), 400, 300)
    winner = font.render('', 1, (255,0,0))

    while run:
        win.fill((0,0,0))
        draw_window(paddle_a, paddle_b, ball)

        # MOVE BALL
        ball.x += ball.xspeed
        ball.y += ball.yspeed

        # BORDER CHECKING
        # TOP AND BOTTOM
        if ball.y > 580:
            ball.yspeed *= -1
            playsound('bounce.wav')
        
        if ball.y < 0:
            ball.yspeed *= -1
            playsound('bounce.wav')
        
        # LEFT AND RIGHT
        if ball.x > 800:
            ball.x, ball.y = 400, 300
            ball.xspeed *= -1
            paddle_a.score += 1
        
        if ball.x < 0:
            ball.x, ball.y = 400, 300
            ball.xspeed *= -1
            paddle_b.score += 1

        # PADDLE AND BALL COLISIONS
        if 50 < ball.x < 70 and  paddle_a.y < ball.y < paddle_a.y + 150:
            ball.x = 70
            ball.xspeed *= -1
            playsound('bounce.wav')
        
        if 710 < ball.x < 730 and  paddle_b.y < ball.y < paddle_b.y + 150:
            ball.x = 710
            ball.xspeed *= -1
            playsound('bounce.wav')

        # CHECK WINNER
        if paddle_a.score > paddle_b.score and paddle_a.score == 6:
            winner = font.render('Player A Wins!', 1, (255,0,0))
            run = False
            end = True
        elif paddle_b.score > paddle_a.score and paddle_b.score == 6:
            winner = font.render('Player B Wins!', 1, (255,0,0))
            run = False
            end = True
        win.blit(winner, (width/2 - winner.get_width()/2, height/2 - winner.get_height()/2))
        pygame.display.update()
  
        if not run:
            pygame.time.wait(1000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    paddle_a.y -= paddle_a.yspeed
                elif event.key == pygame.K_s:
                    paddle_a.y += paddle_a.yspeed
                elif event.key == pygame.K_UP:
                    paddle_b.y -= paddle_b.yspeed
                elif event.key == pygame.K_DOWN:
                    paddle_b.y += paddle_b.yspeed

def menu_screen():
    run = True

    while run:
        win.fill((0,0,0))
        text = font.render('Press Any Key To Play', 1, (255,255,255))
        win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                main()

menu_screen()