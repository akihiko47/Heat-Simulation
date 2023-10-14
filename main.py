import pygame
from grad_generator import create_color_palette
from random import random


def draw_sqrs(count, height, width, separator, lst):
    for row in range(count):
        y = row * height + (row + 1) * separator
        for col in range(count):
            x = col * width + (col + 1) * separator
            """melted part"""
            if lst[row][col] > len(full_color_palette)-1:
                pygame.draw.rect(display, (0, 0, 0), (x, y, width, height))
            else:
                """reduce heat part"""
                if full_cool:
                    if 1 < lst[row][col] < len(full_color_palette)-1:
                        lst[row][col] -= cool_speed
                else:
                    if len(full_color_palette)//2+100 < lst[row][col] < len(full_color_palette)-1:
                        lst[row][col] -= cool_speed

                """checks negative"""
                if lst[row][col] < 0:
                    lst[row][col] = 0

                """drawing"""
                pygame.draw.rect(display, full_color_palette[lst[row][col]], (x, y, width, height))


pygame.init()


"""settings"""
colors_hex = [
              '#808080', '#604d4d', '#9d786c', '#b5735c', '#ad3737', '#cd0000',
              '#ff0000', '#ff6600', '#ff7f00', '#ffa64d', '#e6ae22', '#fffd01', '#ffffe6', '#ffffff'
             ]

full_color_palette = create_color_palette(colors_hex)

display_color = (10, 10, 10)
color_num = 0

number_of_sqr = 200
pen_size = 40
cool_speed = 5
heat_speed = 30
full_cool = True
grad_len_per_color = 100
sep = 0
sqr_width = 5
sqr_height = 5

"""clock"""
clock = pygame.time.Clock()

"""display part"""
display_width = (sqr_width + sep) * number_of_sqr + sep
display_height = (sqr_height + sep) * number_of_sqr + sep
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Heat")

"""field"""
lst = [[0 for x in range(number_of_sqr)] for y in range(number_of_sqr)]


def main():
    """main game loop"""
    in_game = True
    while in_game:
        for event in pygame.event.get():
            """closing game"""
            if event.type == pygame.QUIT:
                in_game = False
                pygame.quit()
                quit()

        mouse = pygame.mouse.get_pressed(3)
        if mouse[0]:
            """getting mouse pos"""
            x_mouse, y_mouse = pygame.mouse.get_pos()

            """finding position in sqrs from mouse pos"""
            column = x_mouse // (sep + sqr_width)
            row = y_mouse // (sep + sqr_height)

            if lst[row][column] < len(full_color_palette):
                for i in range(-pen_size, pen_size+1):
                    for j in range(-pen_size, pen_size+1):
                        try:
                            if (-i/pen_size < random() > i/pen_size) and (-j/pen_size < random() > j/pen_size):
                                lst[row + i][column + j] += heat_speed
                        except IndexError:
                            continue

        """drawing"""
        draw_sqrs(number_of_sqr, sqr_height, sqr_width, sep, lst)

        clock.tick(60)
        pygame.display.update()


if __name__ == '__main__':
    main()
