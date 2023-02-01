"""! @file encoder_reader.py
    
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
        self.pin1 = pin1
        self.pin2 = pin2
        self.timer = timer
        
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




