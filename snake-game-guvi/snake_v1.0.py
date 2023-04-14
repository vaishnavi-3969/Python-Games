import py, sys, os
import pygame

from pygame.locals import *

catx = 10
caty = 10
screen = 0

def myquit():
    pygame.quit()
    sys.exit(0)


def check_input(events):
    global catx, caty, screen
    for event in events:
        if event.type == QUIT:
            quit()
        else:
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    myquit()
                elif event.key == K_LEFT:
                    catx -= 5
                    print("Mov rect left")
                elif event.key == K_RIGHT:
                    catx += 5
                    print("Mov rect right")
                elif event.key == K_UP:
                    caty += 5
                    print("Mov rect up")
                elif event.key == K_DOWN:
                    caty -= 5
                    print("Mov rect down")
                else:
                    print(event.key)
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (catx, 50, 50, 10))
    pygame.display.update()


def main():
    global screen
    #     iniitalize pygame
    pygame.init()
    # set up window
    window = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("Slither.eat- The snake game")
    # set up drawing surface
    screen = pygame.display.get_surface()
    pygame.display.set_caption("snake")
    # pygame.display.flip()
    pygame.display.update()
    while True:
        check_input(pygame.event.get())


if __name__ == '__main__':
    main()
