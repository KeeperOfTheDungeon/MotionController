from Config import AntComponents
from RoboControl.Robot.Component.Actor.Led import LedSet




class LegSensorsLedSet(LedSet):

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

    def get_command_processors(self):
        command_list = super().get_command_processors()
        return command_list

    def get_message_processors(self):
        msg_list = super().get_message_processors()
        return msg_list

    def get_stream_processors(self):
        stream_list = super().get_stream_processors()
        return stream_list
