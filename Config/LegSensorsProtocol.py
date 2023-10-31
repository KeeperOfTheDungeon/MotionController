from RoboControl.Robot.Device.DeviceProtocol import DeviceProtocol

CMD_LED_SET_BRIGHTNESS = 0x30
CMD_LED_GET_BRIGHTNESS = 0x31

MSG_LED_BRIGHTNESS = 0x25  # TODO not implemented?

STREAM_LED_BRIGHTNESS = 0x22  # TODO not implemented?

CMD_VCNL4020_SET_SETTINGS = 0x20
CMD_VCNL4020_GET_SETTINGS = 0x21
CMD_VCNL4020_SAVE_DEFAULTS = 0x22
CMD_VCNL4020_LOAD_DEFAULTS = 0x23
CMD_VCNL4020_GET_LUX = 0x24
CMD_VCNL4020_GET_DISTANCE = 0x25
CMD_VCNL4020_GET_RAW_PROXIMITY = 0x26
CMD_VCNL4020_SET_DISTANCE_TABLE = 0x27
CMD_VCNL4020_GET_DISTANCE_TABLE = 0x28
CMD_VCNL4020_GET_VALUE = 0x0

MSG_VCNL4020_SETTINGS = 0x20
MSG_VCNL4020_DISTANCE = 0x21
MSG_VCNL4020_DISTANCE_TABLE = 0x22
MSG_VCNL4020_LUX = 0x23
MSG_VCNL4020_RAW_PROXIMITY = 0x24

STREAM_VCNL4000LUX_VALUES = 0x20
STREAM_VCNL4000DISTANCE_VALUES = 0x21

# TODO ?
CMD_LED_SET_SETTINGS = 0
CMD_LED_GET_SETTINGS = 0
CMD_LED_SAVE_DEFAULTS = 0
CMD_LED_LOAD_DEFAULTS = 0
CMD_LED_GET_VALUE = 0

MSG_LED_SETTINGS = 0  # TODO ?


class LegSensorsProtocol(DeviceProtocol):

    def __init__(self, leg_sensors):
        super().__init__(leg_sensors)

    def get_vcnl4000_protocol(self):
        protocol = {
            "device_id": self._device_id,
            "cmd_setSettings": CMD_VCNL4020_SET_SETTINGS,
            "cmd_getSettings": CMD_VCNL4020_GET_SETTINGS,
            "cmd_saveDefaults": CMD_VCNL4020_SAVE_DEFAULTS,
            "cmd_loadDefaults": CMD_VCNL4020_LOAD_DEFAULTS,
            "cmd_getValue": CMD_VCNL4020_GET_VALUE,
            "msg_settings": MSG_VCNL4020_SETTINGS,
            "cmd_getLux": CMD_VCNL4020_GET_LUX,
            "msg_lux": MSG_VCNL4020_LUX,
            "stream_lux": STREAM_VCNL4000LUX_VALUES,
            "cmd_getDistance": CMD_VCNL4020_GET_DISTANCE,
            "msg_distance": MSG_VCNL4020_DISTANCE,
            "stream_distance": STREAM_VCNL4000DISTANCE_VALUES,
            "cmd_getRawProximity": CMD_VCNL4020_GET_RAW_PROXIMITY,
            "msg_rawProximity": MSG_VCNL4020_RAW_PROXIMITY,
            "cmd_setDistanceTable": CMD_VCNL4020_SET_DISTANCE_TABLE,
            "cmd_getDistanceTable": CMD_VCNL4020_GET_DISTANCE_TABLE,
            "msg_distanceTable": MSG_VCNL4020_DISTANCE_TABLE
        }

        return protocol

    def get_led_protocol(self):
        protocol = {
            "device_id": self._device_id,
            "cmd_setSettings": CMD_LED_SET_SETTINGS,
            "cmd_getSettings": CMD_LED_GET_SETTINGS,
            "cmd_saveDefaults": CMD_LED_SAVE_DEFAULTS,
            "cmd_loadDefaults": CMD_LED_LOAD_DEFAULTS,
            "cmd_getValue": CMD_LED_GET_VALUE,
            "msg_settings": MSG_LED_SETTINGS,
            "cmd_setBrightness": CMD_LED_SET_BRIGHTNESS,
            "cmd_getBrightness": CMD_LED_GET_BRIGHTNESS,
            "msg_brightness": MSG_LED_BRIGHTNESS,
            "stream_brightness": STREAM_LED_BRIGHTNESS
        }

        return protocol


    def get_light_sensor_protocol(self):
        protocol = {
            "device_id": self._device_id,
            "cmd_setSettings": CMD_LED_SET_SETTINGS,
            "cmd_getSettings": CMD_LED_GET_SETTINGS,
            "cmd_saveDefaults": CMD_LED_SAVE_DEFAULTS,
            "cmd_loadDefaults": CMD_LED_LOAD_DEFAULTS,
            "cmd_getValue": CMD_LED_GET_VALUE,
            "msg_settings": MSG_LED_SETTINGS,
            "cmd_setBrightness": CMD_LED_SET_BRIGHTNESS,
            "cmd_getBrightness": CMD_LED_GET_BRIGHTNESS,
            "msg_brightness": MSG_LED_BRIGHTNESS,
            "stream_brightness": STREAM_LED_BRIGHTNESS
        }

        return protocol


