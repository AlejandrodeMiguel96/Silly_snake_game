import pygame
import time
import random

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
yellow = (255, 255, 102)

dis_width = 800
dis_height = 600
dis_color = black

snake_block = 10
snake_color = blue
snake_speed = 30

food_block = snake_block
food_color = red

pygame.init()
dis = pygame.display.set_mode([dis_width, dis_height])  # sets up the display
pygame.display.set_caption('Snake game by Alejandro de Miguel')
clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 30)
score_font = pygame.font.SysFont("comicsansms", 35)


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/3, dis_height/3])


def makefood():
    x2 = round(random.randrange(0 + snake_block, dis_width - snake_block) / snake_block) * snake_block
    y2 = round(random.randrange(0 + snake_block, dis_height - snake_block) / snake_block) * snake_block
    return x2, y2


def drawsnake(surf, color, snake_list, blocksize):
    for x in snake_list:
        pygame.draw.rect(surf, color, [x[0], x[1], blocksize, blocksize])


def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


def gameloop():
    game_over = False
    game_close = False

    x1_change = 0
    y1_change = 0
    x1 = round((dis_width / 2)/snake_block) * snake_block  # snake's x initial position
    y1 = round((dis_height / 2)/snake_block) * snake_block  # snake's y initial position

    snake_list = []
    snake_length = 1

    foodx, foody = makefood()

    while not game_over:

        while game_close:
            message('You lost! Press Q-Quit or R-Reset Game', red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_r:
                        gameloop()
                if event.type == pygame.QUIT:  # so clicking on the x closes the window
                    game_over = True
                    game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # so clicking on the x closes the window
                game_over = True
            if event.type == pygame.KEYDOWN:  # adds key controls
                if event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block  # negative because y is positive downwards
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
                elif event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0

        if x1 < 0 or x1 > dis_width or y1 < 0 or y1 > dis_height:  # finish game if hit a wall
            game_close = True
            dis.fill(dis_color)
            message('You hit a wall. You lost!', red)
            pygame.display.update()
            time.sleep(1.5)

        x1 += x1_change
        y1 += y1_change

        dis.fill(dis_color)
        pygame.draw.rect(dis, food_color, [foodx, foody, food_block, food_block])  # draw food

        snake_head = [x1, y1]
        snake_list.append(snake_head)  # so the head of snake is the last element on the list
        if len(snake_list) > snake_length:
            del snake_list[0]

        drawsnake(dis, snake_color, snake_list, snake_block)
        your_score(snake_length - 1)
        pygame.display.update()

        if x1 == foodx and y1 == foody:  # when snake encounters food
            print('+1 point')
            snake_length += 1
            foodx, foody = makefood()

        for x in snake_list[:-1]:  # if the snake bites itself, loses
            if x == snake_head:
                message('You bit yourself! You lost!', red)
                game_over = True

        clock.tick(snake_speed)

    time.sleep(3)
    pygame.quit()
    quit()


gameloop()

# personalizar con mi cara y trabajo en vez de comida???
