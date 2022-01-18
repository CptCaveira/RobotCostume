import RPi.GPIO as GPIO
import vlc
import random
from time import sleep


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(17, GPIO.OUT)


def robot(pin):
    player = vlc.Instance(' --aout alsa,none')
    robot1 = player.media_new('/home/pi/Desktop/Robot/robot1.ogg')
    robot2 = player.media_new('/home/pi/Desktop/Robot/robot2.ogg')
    robot3 = player.media_new('/home/pi/Desktop/Robot/robot3.ogg')
    robot4 = player.media_new('/home/pi/Desktop/Robot/robot4.ogg')
    robot5 = player.media_new('/home/pi/Desktop/Robot/robot5.ogg')
    robot6 = player.media_new('/home/pi/Desktop/Robot/robot6.ogg')
    robot7 = player.media_new('/home/pi/Desktop/Robot/robot7.ogg')
    robot8 = player.media_new('/home/pi/Desktop/Robot/robot8.ogg')
    robotsounds = [robot1, robot2, robot3, robot4, robot5, robot6, robot7, robot8]
    into = random.choice(robotsounds)
    media_player = player.media_player_new()
    media_player.set_media(into)
    media_player.play()
    sleep(5)
    
    
GPIO.add_event_detect(27, GPIO.RISING, callback = robot, bouncetime = 5000)
while True:
    try:
        if GPIO.input(27) == 1:
            GPIO.output(17, GPIO.HIGH)
            sleep(5)
            GPIO.output(17,GPIO.LOW)
    except:
        GPIO.cleanup()
