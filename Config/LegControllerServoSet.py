from Config import AntConfig
from PicoControl.Robot.Component.ServoPico import ServoSetPico


class LegControllerServoSet(ServoSetPico):
    def __init__(self, protocol):
        
        AntConfig.TEST_SERVO["protocol"] = protocol

        servo_list = [
            AntConfig.TEST_SERVO
        ]
        
        pwm_pin_list = [7]

        super().__init__(servo_list, pwm_pin_list, protocol)
