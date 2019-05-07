import pygame
import time



#Colors & images
red = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)


#Display parameters
displayHeight = 240
displayWidth = 320

pygame.init()
#initilize the window

window = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption('Button Mash')

clock = pygame.time.Clock()


intro_img = pygame.image.load('images\intro_image.png')
window.blit(intro_img, [0, 0])
pygame.display.flip()


time.sleep(1)
pygame.quit()

