from utils import buttonSwitch as button
import time

def switch():
    global lamp
    if lamp == 'on':
        button.buttonOn()
        lamp = 'off'
    else:
        button.buttonOff()
        lamp = 'on'
    print(lamp)

button.on_button.config(command = switch)

lamp = 'off'

while button.x == True:
    button.update()
