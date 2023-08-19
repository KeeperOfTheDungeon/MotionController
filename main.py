from machine import Pin, PWM
from MotionController import MotionController


def main():
    # possible clock
    #pwm = PWM(Pin(2))
    #pwm.freq(1000)
    #pwm.duty_u16(32268)

    print("Start main()")
    device = MotionController()
    device.run()


main()
