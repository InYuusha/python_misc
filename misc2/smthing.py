import pygame, time, random

pygame.init()

# SOUND/TEXTURES
icon = pygame.image.load("C:\\Users\\op\\Desktop\\ball.png")
pygame.display.set_icon(icon)

# VARIABLES
white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 155, 0)
bright_green = (0, 250, 0)
bright_red = (255, 0, 0)

font_size = 50
font = pygame.font.SysFont(None, font_size)

# FUNCTIONS

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameWindow, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == "play":
                game_loop()

            elif action == "quit":
                gameRun = False
                gameWindow.fill(white)
                message_to_screen("Closing Game...", black, 280, 280)
                pygame.display.update()
                time.sleep(1)
                pygame.quit()
                quit()

    else:
        pygame.draw.rect(gameWindow, ic, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameWindow.blit(textSurf, textRect)

def snake(rect_x, rect_y, block_size):
    pygame.draw.rect(gameWindow, green, [rect_x, rect_y, block_size, block_size])

def message_to_screen(msg, color, x, y):
    screen_text = font.render(msg, True, color)
    gameWindow.blit(screen_text, [x, y])


# WINDOW/SURFACE
display_w = 800
display_h = 600
window_title = "Window"

gameWindow = pygame.display.set_mode((display_w, display_h))
pygame.display.set_caption(window_title)

# FPS/Clock
clock = pygame.time.Clock()


# Game Loop


def game_loop():
    # RECT OPTIONS
    moveSpeed = 10
    block_size = 10

    rect_x = display_w / 2
    rect_y = display_h / 2

    change_x = 0
    change_y = 0

    randApplex = round(random.randrange(0, display_w - block_size) / 10.0) * 10.0
    randAppley = round(random.randrange(0, display_h - block_size) / 10.0) * 10.0

    global gameRun, gameOver
    gameRun = True
    gameOver = False

    while gameRun:

        while gameOver:
            gameRun = False
            gameWindow.fill(white)
            # button(msg, x, y, w, h, ic, ac, action=None)
            message_to_screen("Game Over!", red, 300, 300)
            button("Restart", 150, 450, 100, 50, green, bright_green, "play")
            button("Quit", 550, 450, 100, 50, red, bright_red, "quit")
            pygame.display.update()

           # RIGHT HERE!

            for event in pygame.event.get():
                None

           # RIGHT THERE!

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameRun = False
                gameOver = False
                gameWindow.fill(white)
                message_to_screen("Closing Game...", black, 280, 280)
                pygame.display.update()
                time.sleep(1)
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    change_y = -moveSpeed
                    change_x = 0
                elif event.key == pygame.K_s:
                    change_y = moveSpeed
                    change_x = 0
                elif event.key == pygame.K_a:
                    change_x = -moveSpeed
                    change_y = 0
                elif event.key == pygame.K_d:
                    change_x = moveSpeed
                    change_y = 0

        # BOARDER CRASH
        if rect_x >= display_w or rect_x < 0 or rect_y >= display_h or rect_y < 0:
            gameOver = True
        # LOGIC
        rect_x += change_x
        rect_y += change_y

        if rect_x == randApplex and rect_y == randAppley:
            randApplex = round(random.randrange(0, display_w - block_size) / 10.0) * 10.0
            randAppley = round(random.randrange(0, display_h - block_size) / 10.0) * 10.0

        # RENDER
        gameWindow.fill(white)

        pygame.draw.rect(gameWindow, red, [randApplex, randAppley, block_size, block_size])
        snake(rect_x, rect_y, block_size)
        pygame.display.update()

        clock.tick(15)

    message_to_screen("You Lose!", red, 325, 300)
    pygame.display.update()
    time.sleep(1)
    message_to_screen("Closing Game!", black, 280, 350)
    pygame.display.update()
    time.sleep(1)

    # QUIT
    pygame.quit()
    quit()


game_loop()
