from RoboControl.Robot.Device.DeviceProtocol import DeviceProtocol

CMD_TMF882x_GET_DISTANCE = 0x20
CMD_TMF882x_GET_TEMPERATURE = 0x21
CMD_TMF882x_GET_VALUE = 0x0
CMD_TMF882x_SET_SETTINGS = 0x22
CMD_TMF882x_GET_SETTINGS = 0x23
CMD_TMF882x_SAVE_DEFAULTS = 0x24
CMD_TMF882x_LOAD_DEFAULTS = 0x25

MSG_TMF882x_DISTANCE = 0x20
MSG_TMF882x_TEMPERATURE = 0x21

STREAM_TMF882x_DISTANCE_VALUES = 0x20
STREAM_TMF882x_TEMPERATURE_VALUES = 0x21


class HeadSensorsProtocol(DeviceProtocol):

    def __init__(self, head_sensors):
        super().__init__(head_sensors)

    def get_tmf882x_protocol(self):
        return {
            "device_id": self._device_id,
            "cmd_getDistance": CMD_TMF882x_GET_DISTANCE,
            "cmd_getTemperature": CMD_TMF882x_GET_TEMPERATURE,
            "cmd_setSettings": CMD_TMF882x_SET_SETTINGS,
            "cmd_getSettings": CMD_TMF882x_GET_SETTINGS,
            "cmd_saveDefaults": CMD_TMF882x_SAVE_DEFAULTS,
            "cmd_loadDefaults": CMD_TMF882x_LOAD_DEFAULTS,
            "cmd_getValue": CMD_TMF882x_GET_VALUE,
            "msg_distance": MSG_TMF882x_DISTANCE,
            "msg_temperature": MSG_TMF882x_TEMPERATURE,
            "stream_distance": STREAM_TMF882x_DISTANCE_VALUES,
            "stream_temperature": STREAM_TMF882x_TEMPERATURE_VALUES
        }
