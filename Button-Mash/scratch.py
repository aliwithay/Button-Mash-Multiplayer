import pygame
import time
import RPi.GPIO as GPIO

def button_callback(channel):
    print("A Button was pressed")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(36,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge



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

window = pygame.display.set_mode((displayWidth, displayHeight), pygame.FULLSCREEN)
pygame.display.set_caption('Button Mash')

clock = pygame.time.Clock()


intro_img = pygame.image.load('images/intro_image.png')
window.blit(intro_img, [0, 0])
pygame.display.flip()

while True:
    print("waiting")
    time.sleep(3)


time.sleep(10)
pygame.quit()

