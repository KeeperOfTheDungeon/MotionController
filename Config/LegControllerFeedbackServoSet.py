from Config import AntConfig
from PicoControl.Robot.Component.FeedbackServoPico import FeedbackServoSetPico


class LegControllerFeedbackServoSet(FeedbackServoSetPico):
    def __init__(self, protocol):
        
        AntConfig.TEST_FEEDBACK_SERVO["protocol"] = protocol

        servo_list = [
            AntConfig.TEST_FEEDBACK_SERVO
        ]
        
        pwm_pin_list = [7]
        adc_pin_list = [27]

        super().__init__(servo_list, pwm_pin_list, adc_pin_list, protocol)
