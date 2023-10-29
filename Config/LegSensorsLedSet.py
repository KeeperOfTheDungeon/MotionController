from Config import AntComponents
from PicoControl.Robot.Component.LedPico import LedSetPico




class LegSensorsLedSet(LedSetPico):

    def __init__(self, protocol):
        AntComponents.FRONT_LEFT_LEG_LED["protocol"] = protocol
        AntComponents.FRONT_RIGHT_LEG_LED["protocol"] = protocol
        AntComponents.CENTER_LEFT_LEG_LED["protocol"] = protocol
        AntComponents.CENTER_RIGHT_LEG_LED["protocol"] = protocol
        AntComponents.BACK_LEFT_LEG_LED["protocol"] = protocol
        AntComponents.BACK_RIGHT_LEG_LED["protocol"] = protocol

        actor_list = [
            AntComponents.FRONT_LEFT_LEG_LED,
            AntComponents.FRONT_RIGHT_LEG_LED,
            AntComponents.CENTER_LEFT_LEG_LED,
            AntComponents.CENTER_RIGHT_LEG_LED,
            AntComponents.BACK_LEFT_LEG_LED,
            AntComponents.BACK_RIGHT_LEG_LED
        ]

        super().__init__(actor_list, protocol)


