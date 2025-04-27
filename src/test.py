import machine
import time

adc = machine.ADC(26)

while True:
    val = adc.read_u16()
    print(val)
    time.sleep(0.25)