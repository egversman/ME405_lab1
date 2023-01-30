"""! @file 
    
"""
# Should be motor controller class?
# import motor_driver.py
# import encoder_reader.py



def chAB_setup():
    """!
        
    """
    pC6 = pyb.Pin(pyb.Pin.board.PC6, pyb.Pin.OUT_PP)
    pC7 = pyb.Pin(pyb.Pin.board.PC7, pyb.Pin.OUT_PP)
    
    tim = pyb.Timer(8, prescaler = 0, period = 0xFFFF) 
    
    ch1 = tim.channel(1, pyb.Timer.ENC_AB, pin=pC6) 
    ch2 = tim.channel(2, pyb.Timer.ENC_AB, pin=pC7)

    return tim

if __name__ == "__main__":
    tim = chAB_setup()
    while True:
        print(tim.counter()) # this works better in the command line
    # figure out what timer # works
    # Rotate motor by hand and use tim.counter() to verify ??
    


