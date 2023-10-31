from Config import AntConfig
from PicoControl.Robot.Component.LedPico import LedSetPico




class LegSensorsLedSet(LedSetPico):

    def __init__(self, protocol):
        AntConfig.FRONT_LEFT_LEG_LED["protocol"] = protocol
        AntConfig.FRONT_RIGHT_LEG_LED["protocol"] = protocol
        AntConfig.CENTER_LEFT_LEG_LED["protocol"] = protocol
        AntConfig.CENTER_RIGHT_LEG_LED["protocol"] = protocol
        AntConfig.BACK_LEFT_LEG_LED["protocol"] = protocol
        AntConfig.BACK_RIGHT_LEG_LED["protocol"] = protocol

        actor_list = [
            AntConfig.FRONT_LEFT_LEG_LED,
            AntConfig.FRONT_RIGHT_LEG_LED,
            AntConfig.CENTER_LEFT_LEG_LED,
            AntConfig.CENTER_RIGHT_LEG_LED,
            AntConfig.BACK_LEFT_LEG_LED,
            AntConfig.BACK_RIGHT_LEG_LED
        ]
        
        pinlist =[18,19,20,21,22,23]
        
        super().__init__(actor_list, pinlist, protocol)


