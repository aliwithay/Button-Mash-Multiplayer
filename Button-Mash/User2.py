import pygame
import RPi.GPIO as GPIO
import sys
import socket
import select
import time
import os

#os.putenv('SDL_VIDEODRIVER', 'fbcon')
pygame.init()
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Colors & images
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
intro_img = "./images/intro_image.jpg"

#Display parameters
displayHeight = 240
displayWidth = 320

#Bar positions


#initilize the window
window = pygame.display.set_mode((displayWidth, displayHeight), pygame.FULLSCREEN)

def button_press(channel):
#Send signal to server.
    server.send(b's')

#Setup GPIO buttons
#A:16 Start:20 Select:21
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(36, GPIO.RISING, callback=button_press)


def text_objects(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()


def message_display(text, indexA, indexB):
    largeText = pygame.font.Font('freesansbold.ttf',12)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((indexA),(indexB))
    window.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)

def clientsetup():
#client.py
    if len(sys.argv) != 3:
        print("Correct usage: Button-Mash.py, IP address, port number")
        exit()
    IP_address = str(sys.argv[1])
    Port = int(sys.argv[2])
    server.connect((IP_address, Port))

def winner_screen(read_sockets):
    for socket in read_sockets:
        if socket == server:
            message = socket.recv(2048)
    updateboard(message)
    time.sleep(10)
    pygame.quit()



def updateboard(scores):
    colours = [blue, green]
    arr = scores.split()
    print(arr)
    for i in range(len(arr)):
        pygame.draw.rect(window, colours[i], [(128*i)+64, 200-(arr[i]*2), 64, arr[i]*2])



def gameloop():
    #write initial board
    window.fill(white)
    pygame.draw.line(window, red, (0, 50), (320, 50))
    pygame.draw.line(window, red, (0, 100), (320, 100))
    pygame.draw.line(window, red, (0, 150), (320, 150))
    pygame.draw.line(window, red, (0, 200), (320, 200))
    message_display(username, 96+(p*128), 220)
    pygame.display.flip()
    clock.tick(60)
    while True:
        socket_list = [sys.stdin, server]
        read_sockets, write_sockets, error_socket = select.select(socket_list, [], [])
        for s in read_sockets:
            if s == server:
                message = s.recv(2048)
                print("message received = " + str(message))
                if message == b"gameover":
                    winner_screen(read_sockets)
                #"p1 p2 p3 p4"
                elif message == b'ready':
                    message_display(message, 160, 20)
                    time.sleep(2)
                    message_display('GO!', 160, 40)
                else:
                    updateboard(message)

def gameintro():
#Show intro screen.
#Check for keypress.
#   If start button for "ready" pressed, call game loop
#   If select button pressed, exit. [optional]
    window.blit(intro_img, [0,0])
    pygame.display.flip()
    clientsetup()
    gameloop()

clock = pygame.time.Clock()
username = 'James'
p = 1
intro_img = pygame.image.load('images/intro_image.png')
gameintro()

