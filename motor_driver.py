"""! @file motor_driver.py
    
"""

class MotorDriver:
    """! 
    This class implements a motor driver for an ME405 kit. 
    """

    def __init__ (self, en_pin, in1pin, in2pin, timer):
        """! 
        Creates a motor driver by initializing GPIO pins and turning off the 
        motor for safety. 
        @param en_pin Motor driver enable pin. Set high to enable the motor.
        @param in1pin First directional pin. Set this pin high and send it a PWM
               signal (with in2pin set low) to power the motor CW (?).
        @param in2pin Second directional pin. Set this pin high and send it a 
               PWM signal (with in1pin set low) to power the motor CCW (?).
        @param timer Motor driver timer which generates PWM signals whose 
               frequency determines the motor speed.
        """
        # en_pin
        if en_pin.lower() == "a" or en_pin.lower() == "ena":
            self.en_pin = pyb.Pin(pyb.Pin.board.PA10,pyb.Pin.OUT_OD, pyb.Pin.PULL_UP)
        elif en_pin.lower() == "b" or en_pin.lower() == "enb":
            self.en_pin = pyb.Pin(pyb.Pin.board.PC1, pyb.Pin.OUT_OD, pyb.Pin.PULL_UP)
        else:
            raise AttributeError
        
        # in1pin
        if in1pin.lower() == "a" or in1pin.lower() == "in1a":
            self.in1pin = pyb.Pin(pyb.Pin.board.PB4, pyb.Pin.OUT_PP)
        elif in1pin.lower() == "b" or in1pin.lower() == "in1b":
            self.in1pin = pyb.Pin(pyb.Pin.board.PA0, pyb.Pin.OUT_PP)
        else:
            raise AttributeError
    
        # in2pin
        if in2pin.lower() == "a" or in2pin.lower() == "in2a":
            self.in2pin = pyb.Pin(pyb.Pin.board.PB5, pyb.Pin.OUT_PP)
        elif in2pin.lower() == "b" or in2pin.lower() == "in2b":
            self.in2pin = pyb.Pin(pyb.Pin.board.PA1, pyb.Pin.OUT_PP)
        else:
            raise AttributeError
        
        #timer
        if timer.lower() == "tim3":
            self.timer = pyb.Timer(3, prescaler = 0, period = 0xFFFF)
        elif timer.lower() == "tim5":
            self.timer = pyb.Timer(5, prescaler = 0, period = 0xFFFF)
        else:
            raise AttributeError
        
        # Turn the motor off for safety
        self.en_pin.low()
        
    def set_duty_cycle (self, level):
        """!
        This method sets the duty cycle to be sent to the motor to the given 
        level. Positive values cause torque in one direction, negative values in 
        the opposite direction.
        @param level A signed integer holding the duty cycle of the voltage sent 
               to the motor 
        """
        ch1 = self.timer.channel(1, pyb.Timer.PWM, pin=self.in1pin) 
        ch2 = self.timer.channel(2, pyb.Timer.PWM, pin=self.in2pin)
        
        self.en_pin.high() #enable motor
        
        # set the timer according to the specified PWM duty cycle 'level'
        if level >= 0:
            ch1.pulse_width_percent(abs(level)) #IN1A low
            ch2.pulse_width_percent(0) #PWM signal to IN2A
        else:
            ch1.pulse_width_percent(0) #IN1A low
            ch2.pulse_width_percent(abs(level)) #PWM signal to IN2A
        
        print (f"Setting duty cycle to {level}")

        
if __name__ == "__main__":
    '''
    Test motor driver class: Send a range of duty cycles, both positive and 
    negative, and check that the motor moves both ways. Make sure to check “edge 
    cases” such as the maximum and minimum possible duty cycles for proper 
    operation.
    '''
    # MotorDriver test
    moe = MotorDriver ('ena','in1a','in2a','tim3')
    moe.set_duty_cycle (-99) # only abs 20-99 plz

