import pygame
from paddle import Paddle
from ball import Ball

pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")
carryOn = True
clock = pygame.time.Clock()
paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 250
paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 770
paddleB.rect.y = 250
ball = Ball(WHITE, 10, 10)
ball.rect.x = 394
ball.rect.y = 295
scoreA = 0
scoreB = 0


all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                carryOn = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)

    all_sprites_list.update()

    if ball.rect.x >= 790:
        scoreA += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        scoreB += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y > 590:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]

    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
        ball.bounce()

    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, [398, 0], [398, 600], 5)
    all_sprites_list.draw(screen)
    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, WHITE)
    screen.blit(text, (300,10))
    text = font.render(str(scoreB), 1, WHITE)
    screen.blit(text, (520,10))
    pygame.display.flip()
    clock.tick(60)



pygame.quit()
