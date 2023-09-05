import pygame,sys,os

"""
pygame.init()

DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello world!')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
"""
pygame.init()
ez = pygame.display.set_mode((1000,600))
pygame.display.set_caption("SISI A LA DOTA")

ez.fill((255, 255, 255))
pygame.draw.rect(ez, (255, 0, 0), (100, 80, 150, 50))
pygame.display.update()
pygame.draw.rect(ez, (255, 0, 0), (200, 50, 150, 50))
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
           
