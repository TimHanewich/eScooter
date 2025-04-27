# turn on light to indicate it is on
import machine
led = machine.Pin(25, machine.Pin.OUT)
led.high()

try: # place entire program in try bracket to catch any error

    # set up SSD-1306 and show loading sign first
    import ssd1306
    i2c = machine.I2C(0, sda=machine.Pin(16), scl=machine.Pin(17))
    print("I2C devices: " + str(i2c.scan()))
    oled = None
    if 60 in i2c.scan():
        oled = ssd1306.SSD1306_I2C(128, 64, i2c)
        oled.fill(0)
        oled.text("Loading...", 0, 0)
        oled.show()

    import throttle
    import time

    # set up throttle
    t = throttle.Throttle(26)

    # set up motor PWM output
    pwm = machine.PWM(machine.Pin(0))
    pwm.freq(50)
    pwm.duty_u16(0) # start at 0

    while True:

        # read input from throttle
        throttle_percent:float = t.read()

        # apply a governor to the throttle
        governor:float = 0.25 # cut to X% power
        throttle_percent_governed:float = throttle_percent * governor

        # calcualte what duty cycle to enact, in nanoseconds
        # the standards for PWM motor input:
        # 1,000,000 nanoseconds = 1ms = the minimum throttle
        # 2,000,000 nanoseconds = 2ms = the maximum throttle
        duty_ns:int = 1000000 + int(throttle_percent_governed * 1000000)
        duty_ns = min(max(duty_ns, 1000000), 2000000) # min/max just to be sure we are not passing an invalid value to the motor

        # print?
        print(str(time.ticks_ms()) + ": Throttle Input = " + str(int(throttle_percent * 100)) + "%, Throttle Input After Governor = " + str(int(throttle_percent_governed * 100)) + "% duty in nanoseconds = " + str(duty_ns))

        # show on OLED display
        if oled != None:
            oled.fill(0)
            oled.text("TI: " + str(int(throttle_percent * 100)) + "%", 0, 0)
            oled.text("TG: " + str(int(throttle_percent_governed * 100)) + "%", 0, 12)
            oled.text("GOV: " + str(int(governor * 100)) + "%", 0, 56)
            oled.show()

        # apply
        pwm.duty_ns(duty_ns)

        # wait
        time.sleep(0.1)

except Exception as ex: # FATAL FAILURE

    # log the error
    msg:str = "Fatal failure at " + str(time.ticks_ms()) + " ms: " + str(ex)
    print(msg)
    f = open("errors.txt", "a")
    f.write(msg)
    f.close()

    # led pulse
    while True:
        led.on()
        time.sleep(1.0)
        led.off()
        time.sleep(1.0)