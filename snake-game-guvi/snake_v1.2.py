import random
import pygame
import sys

pygame.init()

white = (255, 255, 255)
black = (100, 0, 0)
red = (255, 0, 0)
window_width = 800
window_height = 600

game_display = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('slither')
font = pygame.font.SysFont(None, 25, bold=True)


def my_quit():
    pygame.quit()
    sys.exit(0)


clock = pygame.time.Clock()
fps = 5
block_size = 20
no_pixel = 0


def snake(block_size, snake_list):
    for size in snake_list:
        pygame.draw.rect(game_display, black, [size[0] + 5, size[1], block_size, block_size], 2)


def msg_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    game_display.blit(screen_text, [window_width / 2, window_height / 2])


def game_loop():
    game_exit = False
    game_over = False

    lead_x = window_width / 2
    lead_y = window_height / 2

    change_pixels_of_x = 0
    change_pixels_of_y = 0

    snake_list = []
    snake_length = 1

    random_apple_x = round(random.randrange(0, window_width - block_size) / 10.0) * 10.0
    random_apple_y = round(random.randrange(0, window_height - block_size) / 10.0) * 10.0

    while not game_exit:

        while game_over:

            game_display.fill(white)

            msg_to_screen("Game over, press c to play again or Q to quit", red)

            pygame.display.update()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    game_over = False
                    game_exit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False

                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game_exit = True

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    my_quit()

                left_arrow = event.key == pygame.K_LEFT

                right_arrow = event.key == pygame.K_RIGHT

                up_arrow = event.key == pygame.K_UP

                down_arrow = event.key == pygame.K_DOWN

                if left_arrow:

                    change_pixels_of_x = -block_size

                    change_pixels_of_y = no_pixel

                elif right_arrow:

                    change_pixels_of_x = block_size

                    change_pixels_of_y = no_pixel

                elif up_arrow:

                    change_pixels_of_y = -block_size

                    change_pixels_of_x = no_pixel

                elif down_arrow:

                    change_pixels_of_y = block_size

                    change_pixels_of_x = no_pixel

            if lead_x >= window_width or lead_x < 0 or lead_y >= window_height or lead_y < 0:
                game_over = True

        lead_x += change_pixels_of_x

        lead_y += change_pixels_of_y

        game_display.fill(white)

        apple_thickness = 20

        print([int(random_apple_x), int(random_apple_y), apple_thickness, apple_thickness])

        pygame.draw.rect(game_display, red, [random_apple_x, random_apple_y, apple_thickness, apple_thickness])

        spiritualist = [lead_x, lead_y]

        snake_list.append(spiritualist)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for eachSegment in snake_list[:-1]:

            if eachSegment == spiritualist:
                game_over = True

        snake(block_size, snake_list)

        pygame.display.update()

        if random_apple_x <= lead_x <= random_apple_x + apple_thickness:

            if random_apple_y <= lead_y <= random_apple_y + apple_thickness:
                random_apple_x = round(random.randrange(0, window_width - block_size) / 10.0) * 10.0

                random_apple_y = round(random.randrange(0, window_height - block_size) / 10.0) * 10.0

                snake_length += 1

        clock.tick(fps)

    pygame.quit()

    quit()


game_loop()
