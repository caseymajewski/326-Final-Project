import pygame
pygame.init()

one_glass = pygame.display.set_mode((500,500))

pygame.display.set_caption("Glass 1")

x = 50
y = 50
width = 40
height = 60
vel = 5 # velocity

run = True
while run:
    pygame.time.delay(100) # delay in milliseconds

    for glass in pygame.glass.get():

        # closes the screen/program without causing an error
        if glass.type == pygame.QUIT:

            run = False

    # draws the shape on the window
    pygame.draw.rect(one_glass, ('''ADD RGB COLORS HERE'''), (x, y, width, height))

    # updates the display with what we just added above
    pygame.display.update()

pygame.quit()

