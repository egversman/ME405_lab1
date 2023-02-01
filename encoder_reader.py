"""! @file encoder_reader.py
    
"""
"""!
    pC6 = pyb.Pin(pyb.Pin.board.PC6, pyb.Pin.OUT_PP)
    pC7 = pyb.Pin(pyb.Pin.board.PC7, pyb.Pin.OUT_PP)
    tim = pyb.Timer(8, prescaler = 0, period = 0xFFFF)
    ch1 = tim.channel(1, pyb.Timer.ENC_AB, pin=pC6) 
    ch2 = tim.channel(2, pyb.Timer.ENC_AB, pin=pC7)





"""

class EncoderReader:
    """! 
    This class implements... 
    """

    def __init__ (self, pin1, pin2, timer):
        """!
        Creates an encoder reader by...
        @param pin1 
        @param pin2 
        @param timer 
        """
        
        #this is going to assume, for now, that we're only going to use/input the pins and timer that we know works/have already used for the encoder reader
        if pin1 == "PC6":
            self.pin1 = pyb.Pin(pyb.Pin.board.PC6, pyb.Pin.OUT_PP)
        else:
            raise AttributeError
        if pin2 == "PC7":
            self.pin2 = pyb.Pin(pyb.Pin.board.PC7, pyb.Pin.OUT_PP)
        else:
            raise AttributeError
        if timer == "8":
            self.timer = pyb.Timer(8, prescaler = 0, period = 0xFFFF)
        else:
            raise AttributeError
        ch1 = self.timer.channel(1, pyb.Timer.ENC_AB, pin=self.pin1) 
        ch2 = self.timer.channel(2, pyb.Timer.ENC_AB, pin=self.pin2)
    def read (self):
        """!
        Returns the current position of the motor.
        """
        
        return self.timer.counter()
    
    
    def zero (self):
        """!
        Reads the current position of the motor and sets the count to 0 at that 
        current position.
        """
        self.timer.counter().reset()
        
        
if __name__ == "__main__":
    '''
    Test encoder class: Turn the motor by hand and run the motor under power. 
    Does the code return reasonable results when the motor moves a revolution or 
    two one way, then back? Does it work when the motor is moving quickly? The 
    code must work if the timer overflows (counts above 216 − 1) or underflows 
    (counts below zero).
    '''
    encoder = EncoderReader("PC6", "PC7", "8")
    lastcount = 0
    newcount = 0
    rotation = 0
    flow = 0
    
    while True:
        newcount = encoder.read()
        if (abs(newcount - lastcount) < 60000):
            rotation = rotation + (newcount - lastcount)
            lastcount = newcount
        elif newcount < lastcount:
            flow = (65535 - lastcount) + newcount
            rotation = rotation + flow
            lastcount = newcount
        else:
            flow = (65535 - newcount) + lastcount
            rotation = rotation - flow
            lastcount = newcount
        print(rotation)

