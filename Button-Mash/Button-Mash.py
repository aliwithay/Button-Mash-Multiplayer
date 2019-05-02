import pygame
import RPi.GPIO as GPIO
import sys
import socket
import select

pygame.init()
server = socket.socket(socket.AF_INET, socket.SOCK_STREAK)

#Colors & images
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
intro_img = "./images/intro_image.jpg"

#Display parameters
displayHeight = 240
displayWidth = 320

#initilize the window
window = pygame.display.set_mode((displayWidth, displayHeight))

def buttonpress():
#Send signal to server.
    message = b"s"
    server.send(message)

#Setup GPIO buttons
#A:16 Start:20 Select:21
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(16,GPIO.RISING,callback=buttonpress)

def clientsetup():
#client.py
    if len(sys.argv) != 3:
        print("Correct usage: Button-Mash.py, IP address, port number")
        exit()
    IP_address = str(sys.argv[1])
    Port = int(sys.argv[2])
    server.connect((IP_address, Port))

def gameloop()
    while True:
        socket_list = [sys.stdin, server]
        read_sockets, write_sockets, error_socket = select.slect(sockets_list, [], [])
        for socket in read_soket:
            if socket == server:
                message = socket.recv(2048)
                updateboard()

def gameintro():
#Show intro screen.
#Check for keypress.
#   If start button for "ready" pressed, call game loop
#   If select button pressed, exit. [optional]
    window.blit(intro_img, [0,0])
    clientsetup()
    gameloop()

gameintro()


