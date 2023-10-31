from Config.AntConfig import AntDeviceConfig
from MotionController import MotionController

MOTION_CONTROLLER_ID = 13

def main():
    # possible clock
    #pwm = PWM(Pin(2))
    #pwm.freq(1000)
    #pwm.duty_u16(32268)

    print("Start main()")

    device = MotionController(AntDeviceConfig.LEG_SENSORS)
    device.run()

main()
