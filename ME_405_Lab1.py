"""! @file main.py
    This file controls a motor.
"""

import time

def chAB_setup():
    """!
        
    """
    pinB6 = pyb.Pin (pyb.Pin.board.PB6, pyb.Pin.OUT_PP)
    pinB7 = pyb.Pin (pyb.Pin.board.PB7, pyb.Pin.OUT_PP)
    tim = pyb.Timer(ENC_AB, prescaler = 0, period = 0xFFFF)
    
    ch1 = tim.channel (1, pyb.Timer.PWM_INVERTED, pin=pinB6)
    ch2 = tim.channel (2, pyb.Timer.PWM_INVERTED, pin=pinB7)


    return ch1

if __name__ == "__main__":
    chAB_setup()

