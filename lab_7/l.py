import pygame
pygame.init()

WIDTH, HEIGHT = 500, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

BALL_RADIUS = 25
ball_x, ball_y = WIDTH // 2, HEIGHT // 2  
BALL_COLOR = (255, 0, 0)  
BG_COLOR = (255, 255, 255)  
MOVE_SPEED = 20 

running = True
while running:
    screen.fill(BG_COLOR) 
    pygame.draw.circle(screen, BALL_COLOR, (ball_x, ball_y), BALL_RADIUS)  # Draw ball
    pygame.display.flip()  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and ball_x - BALL_RADIUS > 0:
                ball_x -= BALL_RADIUS
            elif event.key == pygame.K_RIGHT and ball_x + BALL_RADIUS < WIDTH:
                ball_x += BALL_RADIUS
            elif event.key == pygame.K_UP and ball_y - BALL_RADIUS > 0:
                ball_y -= BALL_RADIUS
            elif event.key == pygame.K_DOWN and ball_y + BALL_RADIUS < HEIGHT:
                ball_y += BALL_RADIUS
    
    pygame.time.Clock().tick(24)

pygame.quit()