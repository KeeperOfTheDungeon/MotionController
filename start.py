from machine import Pin, PWM
from MotionController import MotionController

MOTION_CONTROLLER_ID = 13

def main():
    # possible clock
    #pwm = PWM(Pin(2))
    #pwm.freq(1000)
    #pwm.duty_u16(32268)

    print("Start main()")
    
    meta_data = dict()
    meta_data["DeviceId"] = MOTION_CONTROLLER_ID
    meta_data["DeviceName"] = "Motion Controller"
    device = MotionController(meta_data)
    device.run()

main()
