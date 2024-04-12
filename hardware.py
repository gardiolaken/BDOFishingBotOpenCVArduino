from pyfirmata import Arduino, SERVO, util
from time import sleep

port = 'COM4'
pin7 = 7
pin8 = 8
pin9 = 9
pin10 = 10
pin11 = 11
pin12 = 12
board = Arduino(port)

angle = 25

board.digital[pin7].mode = SERVO
board.digital[pin8].mode = SERVO
board.digital[pin9].mode = SERVO
board.digital[pin10].mode = SERVO
board.digital[pin11].mode = SERVO
board.digital[pin12].mode = SERVO

def reset():
    sleep(1)
    board.digital[pin7].write(0)
    sleep(1)
    board.digital[pin8].write(0)
    sleep(1)
    board.digital[pin9].write(0)
    sleep(1)
    board.digital[pin10].write(0)
    sleep(1)
    board.digital[pin11].write(0)
    sleep(1)
    board.digital[pin12].write(0)
    sleep(1)

def pressKey(letter):
    if letter == "W":
        board.digital[pin9].write(angle)
        sleep(0.25)
        board.digital[pin9].write(0)
        sleep(0.15)

    elif letter == "A":
        board.digital[pin10].write(angle)
        sleep(0.25)
        board.digital[pin10].write(0)
        sleep(0.15)

    elif letter == "S":
        board.digital[pin11].write(angle)
        sleep(0.25)
        board.digital[pin11].write(0)
        sleep(0.15)

    elif letter == "D":
        board.digital[pin12].write(angle)
        sleep(0.25)
        board.digital[pin12].write(0)
        sleep(0.15)
    
    elif letter == "SPACE":
        board.digital[pin7].write(angle)
        sleep(0.25)
        board.digital[pin7].write(0)
        sleep(0.25)
    
    elif letter == "R":
        board.digital[pin8].write(angle)
        sleep(0.25)
        board.digital[pin8].write(0)
        sleep(0.25)



