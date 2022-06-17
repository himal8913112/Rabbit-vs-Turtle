# created by HIMAL KUMAR SINGH
    
# ------------------TURTLE vs RABBIT-------------------

import pygame

# initialize pygame
pygame.init()

# GAME VALUES

# window dimensions
WIDTH = 1200
HEIGHT = 600

# constants
RABBIT_VELOCITY = 5
TURTLE_VELOCITY = 20
FPS = 30
FOLDER = "D:/Programming/Pygame/RABBIT vs TURTLE/"

# colors
LIGHT_GREEN = pygame.Color(181, 230, 29)
RED = pygame.Color(237, 28, 36)
DARK_GREEN = pygame.Color(29, 148, 65)
ORANGE = pygame.Color(255, 127, 39)
BLACK = pygame.Color(0, 0, 0)

# actors
rabbit = pygame.image.load(FOLDER + 'rabbit.png')
rabbit_rect = rabbit.get_rect()
rabbit_rect.right = 64
rabbit_rect.centery = HEIGHT//3

turtle = pygame.image.load(FOLDER + 'turtle.png')
turtle_rect = turtle.get_rect()
turtle_rect.right = 64
turtle_rect.centery = 2 * HEIGHT // 3

# game font
game_font1 = pygame.font.Font(FOLDER + 'TarrgetHalfToneRegular.otf', 50)
game_font2 = pygame.font.Font(FOLDER + 'SportypoReguler.ttf', 40)

# texts
you_win = game_font1.render('..........YOU WIN..........', True, DARK_GREEN)
you_win_rect = you_win.get_rect()
you_win_rect.center = (WIDTH//2, HEIGHT//3)

you_lose = game_font1.render('..........YOU LOSE..........', True, RED)
you_lose_rect = you_lose.get_rect()
you_lose_rect.center = (WIDTH//2, HEIGHT//3)

restart = game_font2.render('press R to replay', True, ORANGE)
restart_rect = restart.get_rect()
restart_rect.centerx = WIDTH // 2
restart_rect.centery = 2 * HEIGHT // 3

# sound
gunshot = pygame.mixer.Sound(FOLDER + 'gun shot.mp3')
gunshot.set_volume(0.7)

# music
pygame.mixer.music.load(FOLDER + 'background music.mp3')
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)

# CREATE WINDOW
display_surface = pygame.display.set_mode(size=(WIDTH, HEIGHT))
pygame.display.set_caption('RABBIT vs TURTLE')

# MAIN GAME LOOP
running = True
game_status = 0  # before countdown
clock = pygame.time.Clock()
offset = 90
show = 1

while running:

    # countdown (game starts when offset becomes 0)
    if offset > 0:
        offset -= 1  # reduce value by 1
    elif offset == 0:
        # game starts
        gunshot.play()
        game_status = 1  # game is running
        offset = -1

    # events
    for ev in pygame.event.get():

        # if cross button is clicked or alt+F4 is pressed
        if ev.type == pygame.QUIT:
            running = False

        # if r is pressed then restart
        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_r and game_status == 2:
                game_status = 0
                offset = 90
                show = 0
                pygame.mixer.music.play(-1)  # play music
                rabbit_rect.right = 64  # set rabbit at start line
                turtle_rect.right = 64  # set turtle at start line

        # moving turtle
        elif ev.type == pygame.KEYDOWN or ev.type == pygame.KEYUP:
            if ev.key == pygame.K_RIGHT and game_status == 1:
                # right arrow key is pressed or released
                turtle_rect.right += TURTLE_VELOCITY

    # background grass
    display_surface.fill(LIGHT_GREEN)

    # start line
    start = (64, 0)
    end = (64, HEIGHT)
    pygame.draw.line(surface=display_surface, start_pos=start, end_pos=end, color=DARK_GREEN, width=5)

    # finish line
    start = (WIDTH - 64, 0)
    end = (WIDTH - 64, HEIGHT)
    pygame.draw.line(surface=display_surface, start_pos=start, end_pos=end, color=RED, width=5)

    # putting actors
    display_surface.blit(source=rabbit, dest=rabbit_rect)
    display_surface.blit(source=turtle, dest=turtle_rect)

    if game_status == 1:
        # moving rabbit
        rabbit_rect.right += RABBIT_VELOCITY

    elif game_status == 2:
        # printing restart directions with blinking effect
        if show % 5 == 0:
            display_surface.blit(source=restart, dest=restart_rect)
        show += 1

    # deciding winner
    if rabbit_rect.right >= WIDTH - 64:
        # rabbit wins
        display_surface.blit(source=you_lose, dest=you_lose_rect)
        game_status = 2  # game has ended
        pygame.mixer.music.stop()

    elif turtle_rect.right >= WIDTH - 64:
        # turtle wins
        display_surface.blit(source=you_win, dest=you_win_rect)
        game_status = 2  # game has ended
        pygame.mixer.music.stop()

    # refresh display
    pygame.display.update()

    # iteration frequency control
    clock.tick(FPS)

# deallocate the resources
pygame.quit()
