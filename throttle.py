import machine
import time

adc = machine.ADC(26)

# settings
alpha:float = 0.9 # how sharp the throttle response is. A higher alpha is smoother, but less throttle response. A lower value has a higher throttle response, but can become jerky
throttle_min:int = 20000 # modify this to build in a dead zone, if needed (it should be at absolute 0% when not depressed at all)
throttle_max:int = 50000 # modify this to build in a dead zone, if needed

reading_smoothed:float = throttle_min
while True:

    # read and smooth (pass through smoothing filter)
    reading:int = adc.read_u16()
    reading_smoothed = int((reading * (1.0 - alpha)) + (reading_smoothed * alpha))

    # check to ensure if they throttled DOWN, there is no slow waiting to average out... it just goes down
    if reading < reading_smoothed:
        reading_smoothed = reading

    # convert to percentage
    p:float = min(max((reading_smoothed - throttle_min) / (throttle_max - throttle_min), 0.0), 1.0)

    print("Percent: " + str(p))

    time.sleep(0.25)