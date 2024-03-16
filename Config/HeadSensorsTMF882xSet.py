from Config import AntConfig
from PicoControl.Robot.Component.TMF882xPico import TMF882xPicoSet


class HeadSensorsTMF882xSet(TMF882xPicoSet):

    def __init__(self, protocol):
        AntConfig.HeadSensors.FRONT_TMF882x_SENSOR["protocol"] = protocol

        super().__init__(
            AntConfig.HeadSensors.actor_list,
            [component["i2c_addr"] for component in AntConfig.HeadSensors.actor_list],
            protocol
        )
