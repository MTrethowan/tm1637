'''
==============================================================================================
 main.py
 Project
 Version 1.00.00
 By Mike Trethowan
 MIT License
Copyright (c) 2025 Mike Trethowan

 Description:
    Demonstrate the use of a TM1637 as a clock display, using the RTC within the Seed Xiao 2040.

 Notes:    
    
==============================================================================================
XIAO Pin Assignment:

        		        -------- XIAO RP2040 --------
              GP26   1-|                             |-14   5V
              GP27   2-|                             |-13   GND
              GP28   3-|                             |-12   3V3
              GP29   4-|                             |-11   GP3 
    SDO       GP6    5-|                             |-10   GP4 
    SCl       GP7    6-|                             |- 9   GP2 
              GP0    7-| UART0 TX           UART0 RX |- 8   GP1
                        -----------------------------                          --
   
==============================================================================================
'''
import tm1637
from machine import Pin, RTC
from utime import sleep, sleep_us

# ============================================================================================
rtc = RTC()
SEG7 = tm1637.TM1637(clk=Pin(7), dio=Pin(6)) # Setup display driver

# Xiao has onboard RGB Leds.
LEDR = Pin(17, Pin.OUT, Pin.PULL_UP, value=1) # Turns off red LED
LEDG = Pin(16, Pin.OUT, Pin.PULL_UP, value=1) # Turns off green LED
LEDB = Pin(25, Pin.OUT, Pin.PULL_UP, value=1) # Turns off blue LED

# Main: ======================================================================================
print("Hello World")
  
def main():
    SEG7.clear() # New function added to original tm1637.py driver.
    sleep(1)
    SEG7.clock(88,88,True) # Display test: all segments turend on with with colon, no DPs.
    sleep(2)
    while True:
        dt = rtc.datetime() # Get date time tuplet from internal RTC.
        SEG7.clock(dt[4],dt[5],True) # Colon on.
        sleep_us(500000) # sleep_us is used here to show the difference between sleep and sleep_us.
        SEG7.clock(dt[4],dt[5],False) # Colon off.        
        print(str(dt[4])+ str(dt[5]))
        sleep(.5) # Leading zero is not needed.
       
# ============================================================================================
if __name__ == "__main__":
    main()
# ============================================================================================
