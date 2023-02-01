"""! @file encoder_reader.py
   This class contains an implementation of an encoder reader class. The file main includes a test to make sure it works properly. 
"""

import pyb

class EncoderReader:
    """! 
    This implements an encoder reader for the ME 405.
    """

    def __init__ (self, pin1, pin2, tim_num: int):
        """!
        Creates an encoder reader by...
        @param pin1 
        @param pin2 
        @param timer 
        """
        
        #this is going to assume, for now, that we're only going to use/input the pins and timer that we know works/have already used for the encoder reader
        self.pin1 = pyb.Pin(pin1, pyb.Pin.OUT_PP)
        self.pin2 = pyb.Pin(pin2, pyb.Pin.OUT_PP)
        self.timer = pyb.Timer(tim_num, prescaler = 0, period = 0xFFFF)

        # self.pin1 = pyb.Pin(..)
        self.timer.channel(1, pyb.Timer.ENC_AB, pin=self.pin1) 
        self.timer.channel(2, pyb.Timer.ENC_AB, pin=self.pin2)
        
        self.curr_pos = 0
        self.prev_count = 0
        
    def read (self):
        """!
        Returns the current position of the motor.
        """
    
        curr_count = self.timer.counter()
        difference = curr_count - self.prev_count
        
        if (difference) > (65535 // 2):
            difference -= 65535
            
        if (difference) < -(65535 // 2):
            difference += 65535
        
        self.curr_pos += difference
        self.prev_count = curr_count
        
        return self.curr_pos
    

    
    def zero (self):
        """!
        Reads the current position of the motor and sets the count to 0 at that 
        current position.
        """
        self.prev_count = self.timer.counter()
        self.curr_pos = 0
        
        
if __name__ == "__main__":
    '''
    Test encoder class: Turn the motor by hand and run the motor under power. 
    Does the code return reasonable results when the motor moves a revolution or 
    two one way, then back? Does it work when the motor is moving quickly? The 
    code must work if the timer overflows (counts above 216 − 1) or underflows 
    (counts below zero).
    '''
    import motor_driver
    
    moe = motor_driver.MotorDriver(pyb.Pin.board.PA10, pyb.Pin.board.PB4, pyb.Pin.board.PB5, 3)
    enc = EncoderReader(pyb.Pin.board.PC6, pyb.Pin.board.PC7, 8)
    moe.set_duty_cycle(100)
    while True:
        print(enc.read())
    
    


