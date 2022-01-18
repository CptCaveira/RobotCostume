import RPi.GPIO as GPIO
import pygame
import random
from time import sleep

pygame.init()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(17, GPIO.OUT)

robot1 = pygame.mixer.Sound('/home/pi/Desktop/Robot/robot1.ogg')
robot2 = pygame.mixer.Sound('/home/pi/Desktop/Robot/robot2.ogg')
robot3 = pygame.mixer.Sound('/home/pi/Desktop/Robot/robot3.ogg')
robot4 = pygame.mixer.Sound('/home/pi/Desktop/Robot/robot4.ogg')
robot5 = pygame.mixer.Sound('/home/pi/Desktop/Robot/robot5.ogg')
robot6 = pygame.mixer.Sound('/home/pi/Desktop/Robot/robot6.ogg')
robot7 = pygame.mixer.Sound('/home/pi/Desktop/Robot/robot7.ogg')
robot8 = pygame.mixer.Sound('/home/pi/Desktop/Robot/robot8.ogg')
robotsounds = [robot1, robot2, robot3, robot4, robot5, robot6, robot7, robot8]


def robot(pin):
    into = random.randint(0,7)
    robotsounds[into].play()
    if pygame.mixer.get_busy() == True:
        sleep(1)
    
    
GPIO.add_event_detect(27, GPIO.RISING, callback = robot, bouncetime = 5000)
while True:
    try:
        if GPIO.input(27) == 1:
            GPIO.output(17, GPIO.HIGH)
            sleep(5)
            GPIO.output(17,GPIO.LOW)
    except:
        GPIO.cleanup()