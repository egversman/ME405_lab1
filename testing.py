"""! @file 
    
"""
# Should be motor controller class?
# import motor_driver.py
# import encoder_reader.py



def chAB_setup():
    """!
        
    """
    pC6 = pyb.Pin("PC6", pyb.Pin.IN)
    pC7 = pyb.Pin("PC7", pyb.Pin.IN)
    
    tim = pyb.Timer(3, prescaler = 0, period = 0xFFFF) 
    
    ch1 = tim.channel(1, pyb.Timer.PWM, pin=pC6) 
    ch2 = tim.channel(2, pyb.Timer.PWM, pin=pC7)

    return tim

if __name__ == "__main__":
    while True:
        tim = chAB_setup()
        tim.counter()
    # figure out what timer # works
    # Rotate motor by hand and use tim.counter() to verify ??
    


