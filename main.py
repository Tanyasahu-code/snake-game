import pygame
import random
pygame.init()
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255,255,255)
Pink = (255, 105, 180)
BLOCK_SIZE = 20  
snake_x = 200
snake_y = 200
width = 800
height = 600
direction = "RIGHT"
snake_body=[(snake_x,snake_y)]
snake_length=3
score=0
food_x=random.randint(0,
                (width//BLOCK_SIZE)-1)*BLOCK_SIZE
food_y=random.randint(0,
                      (height//BLOCK_SIZE)-1)*BLOCK_SIZE
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game Snake")
clock = pygame.time.Clock()
font=pygame.font.SysFont(None,60)
running = True
while running:
    for event in pygame.event.get():
     if event.type == pygame.QUIT:
        running = False
     if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            direction = "UP"
        elif event.key == pygame.K_DOWN:
            direction = "DOWN"
        elif event.key == pygame.K_LEFT:
            direction = "LEFT"
        elif event.key == pygame.K_RIGHT:
            direction = "RIGHT"

    if direction == "RIGHT":
            snake_x += BLOCK_SIZE 
    elif direction == "LEFT":
            snake_x -= BLOCK_SIZE
    elif direction == "UP":
            snake_y -= BLOCK_SIZE
    elif direction == "DOWN":
            snake_y += BLOCK_SIZE
    if ( 
         snake_x < 0
           or snake_x >= width 
           or snake_y < 0 
           or snake_y >= height 
           ):
         
        screen.fill(BLACK)
        game_over_text=font.render(
            "GAME OVER",
            True,
            WHITE
        )
        screen.blit(game_over_text,(250,250))
        pygame.display.update()
        pygame.time.delay(2000)
        running=False
    screen.fill(BLACK)
    score_text=font.render(
         f"score:{score}",
        True,
        WHITE
    )
    screen.blit(score_text,(10,10))
    pygame.draw.rect(
         screen,
         (255,0,0),
         (food_x,food_y,BLOCK_SIZE,BLOCK_SIZE)
    )
    head=(snake_x,snake_y)
    snake_body.insert(0,head)
    if len(snake_body)>snake_length:
         snake_body.pop()
    for segment in snake_body:
         pygame.draw.rect(
              screen,
              Pink,
              (segment[0],segment[1],BLOCK_SIZE,BLOCK_SIZE)
         )
    if snake_x==food_x and snake_y==food_y:
              snake_length+=1
              score+=1
              food_x=random.randint(0,
                                    (width//BLOCK_SIZE)-1)*BLOCK_SIZE
              food_y=random.randint(0,
                                    (height//BLOCK_SIZE)-1)*BLOCK_SIZE
    pygame.display.update()
    clock.tick(8)
pygame.quit()