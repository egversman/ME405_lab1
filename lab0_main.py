"""! @file main.py
    This file controls the brightness of an LED.
"""
import time

def led_setup():
    """! Set up the LED
        @returns The configured channel used to control the LED"""
    pinA0 = pyb.Pin (pyb.Pin.board.PA0, pyb.Pin.OUT_PP)
    tim2 = pyb.Timer (2, freq=100)
    ch1 = tim2.channel (1, pyb.Timer.PWM_INVERTED, pin=pinA0)
    return ch1

def led_brightness(ch1, brightness_percent):
    """! Control LED Brightness
        @param  ch1 This is the channel that we want to control the brightness on
        @param  brightness_percent This is a percent brightness for the LED   """ 
    ch1.pulse_width_percent (brightness_percent)

# The following code only runs if thus file is run as the main script;
if __name__ == "__main__":
    ch1 = led_setup()

    while True:
        for brightness_percent in range(101):
            led_brightness(ch1, brightness_percent)
            time.sleep(5/101)
    