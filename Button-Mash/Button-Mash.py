import pygame
import RPi.GPIO as GPIO
import sys

pygame.init()

#Colors & images
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
intro_img = "./images/into_image.jpg"

#Display parameters
displayHeight = 240
displayWidth = 320

#initilize the window
window = pygame.display.set_mode((displayWidth, displayHeight))

def buttonpress():
#Send signal to server.

def start():


def quit():
GPIO.cleanup()
pygame.quit()
sys.exit()


#Setup GPIO buttons
#A:16 Start:20 Select:21
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(16,GPIO.RISING,callback=buttonpress)
GPIO.add_event_detect(20,GPIO.RISING,callback=start)
GPIO.add_event_detect(21,GPIO.RISING,callback=quit)


#def hostmode():
#Create a new server connection.
#Chat_server.py
#Display IP address to connect to
#Wait for start button press
#Enter friendly name.
#Create leaderboard:
#   Array to store user ip, friendly name and button press count. (Size: [numUser, 3])
#Signal start of game to other devices.
#Call game start function.
#Recieve counter value from each player.

def clientmode():
#client.py
#Enter friendly name.
#Send friendly name to host.
#Get friendly names of players from server. and player count?
#Create array of players and poistions (size: [numPlayers, 2])
#Wait for signal from host to start game.
#Call game start function (this might be in the server)

def scoreupdate():
#Send counter to server every 300msec.
#Get score precents from server.
#Update player and position array.
#Update gameboard.

def gameloop()
#get the game board from server.
#Check for button press.
#If correct button pressed, incrememnt counter.
# Share data with server upon sub-increment.
# see if server says the game is over:
# If finished, end the game.

def gameintro():
#Show intro screen.
#Check for keypress.
#   If start button for "ready" pressed, call game loop
#   If select button pressed, exit. [optional]
window.blit(intro_img, [0,0])



for event in pygame.event.get():
    if event.type = pygame.QUIT:
        pygame.quit()
        sys.exit()
    if event.type = pygame.KEYDOWN:
        if event.key == pygame.K_LSHIFT:


