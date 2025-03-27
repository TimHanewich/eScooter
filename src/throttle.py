import machine

class Throttle:

    def __init__(self, adc_gpio:int):
        """Supply the GP# of the pin, not the pin number (i.e. Raspberry Pi Pico has ADC pins GP26-GP28)"""
        
        # public settings
        self.alpha:float = 0.9 # how sharp the throttle response is. A higher alpha is smoother, but less throttle response. A lower value has a higher throttle response, but can become jerky
        
        # private settings
        # ADC min + max, determined by 5V or 3.3V source... adjust these to also build in deadzones as needed
        self._throttle_min:int = 20150 # modify this to build in a dead zone, if needed (it should be at absolute 0% when not depressed at all)
        self._throttle_max:int = 50000 # modify this to build in a dead zone, if needed

        # internal variables
        self._adc = machine.ADC(adc_gpio)
        self._reading_smoothed:float = float(self._throttle_min) # for smoothing

    def read(self) -> float:
        """Read the current smoothed throttle input, as a percentage (between 0.0 and 1.0). Pole this at a regular interval to maintain how 'quick' the smoothing filter is."""

        # read raw and smooth
        reading:int = self._adc.read_u16()
        self._reading_smoothed = int((reading * (1.0 - self.alpha)) + (self._reading_smoothed * self.alpha))

        # check to ensure if they throttled DOWN, there is no slow waiting to average out... cut power immediately according to what they are setting, don't make them wait for throttle to average down (for safety purposes)
        if reading < self._reading_smoothed:
            self._reading_smoothed = reading

        # convert to percentage
        p:float = min(max((self._reading_smoothed - self._throttle_min) / (self._throttle_max - self._throttle_min), 0.0), 1.0)

        return p