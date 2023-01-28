"""! @file 
    
"""
# Should be motor controller class?
# import motor_driver.py
# import encoder_reader.py

def chAB_setup(pin1, pin2):
    """!
        
    """
    p1 = pyb.Pin(pyb.Pin.board.pin1, pyb.Pin.OUT_PP)
    p2 = pyb.Pin(pyb.Pin.board.pin2, pyb.Pin.OUT_PP) 
    
    tim = pyb.Timer(ENC_AB, prescaler = 0, period = 0xFFFF) 
    
    ch1 = tim.channel(1, pyb.Timer.PWM, pin=p1) 
    ch2 = tim.channel(2, pyb.Timer.PWM, pin=p2)

    return tim

if __name__ == "__main__":
    tim = chAB_setup(PB6, PB)
    # Rotate motor by hand and use tim.counter() to verify ??
    


