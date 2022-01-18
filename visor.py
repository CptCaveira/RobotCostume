import explorerhat as eh
from time import sleep

count_press = 0

while True:
    if eh.input.one.read() == 1:
        count_press += 1
        if count_press % 2 != 0:
            eh.motor.one.forward(65)
            eh.motor.two.forward(65)
            sleep(0.55)
            eh.motor.stop()
        elif count_press % 2 == 0:
            eh.motor.one.backward(65)
            eh.motor.two.backward(65)
            sleep(0.42)
            eh.motor.stop()
    