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
        self.en_pin = en_pin
        self.in1pin = in1pin
        self.in2pin = in2pin
        self.timer = timer
        
        # Turn the motor off for safety
        
    def set_duty_cycle (self, level):
        """!
        This method sets the duty cycle to be sent to the motor to the given 
        level. Positive values cause torque in one direction, negative values in 
        the opposite direction.
        @param level A signed integer holding the duty cycle of the voltage sent 
               to the motor 
        """
        # set the timer according to the specified PWM duty cycle 'level'
        # if level >= 0:
        #     set self.in1pin high, self.in2pin low
        #     send self.timer signal to in1pin
        # else:
        #     set self.in1pin low, self.in2pin high
        #     send self.timer signal to in2pin

        
if __name__ == "__main__":
    '''
    Test motor driver class: Send a range of duty cycles, both positive and 
    negative, and check that the motor moves both ways. Make sure to check “edge 
    cases” such as the maximum and minimum possible duty cycles for proper 
    operation.
    '''
    # MotorDriver test
    moe = MotorDriver (a_pin, another_pin, a_timer)
    moe.set_duty_cycle (-42)

