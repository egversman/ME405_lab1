"""! @file 
    
"""
# Should be motor controller class?
# import motor_driver.py
# import encoder_reader.py


if __name__ == "__main__":
    pin_C6 = pyb.Pin(pyb.Pin.board.PC6, pyb.Pin.OUT_PP)
    pin_C7 = pyb.Pin(pyb.Pin.board.PC7, pyb.Pin.OUT_PP)
    pin_ENA = pyb.Pin(pyb.Pin.board.PA10, pyb.Pin.OUT_OD, pyb.Pin.PULL_UP)
    pin_IN1A = pyb.Pin(pyb.Pin.board.PB4, pyb.Pin.OUT_PP)
    pin_IN2A = pyb.Pin(pyb.Pin.board.PB5, pyb.Pin.OUT_PP)
    
    
    timer_3 = pyb.Timer(3, prescaler = 0, period = 0xFFFF)
    timer_5 = pyb.Timer(5, prescaler = 0, period = 0xFFFF)
    timer_8 = pyb.Timer(8, prescaler = 0, period = 0xFFFF)
    
    
    t3_ch1 = timer_3.channel(1, pyb.Timer.PWM, pin=pin_IN1A) 
    t3_ch2 = timer_3.channel(2, pyb.Timer.PWM, pin=pin_IN2A)
    t8_ch1 = timer_8.channel(1, pyb.Timer.ENC_AB, pin=pin_C6)
    t8_ch2 = timer_8.channel(2, pyb.Timer.ENC_AB, pin=pin_C7)
    
    
    pin_ENA.high() #enable motor
    t3_ch1.pulse_width_percent(70) #IN1A low
    t3_ch2.pulse_width_percent(0) #PWM signal to IN2A
    

 
    # figure out what timer # works
    # Rotate motor by hand and use tim.counter() to verify ??
    


