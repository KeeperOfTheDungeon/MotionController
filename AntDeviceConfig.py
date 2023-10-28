from RoboControl.Robot.AbstractRobot.DeviceConfig import DeviceConfig


class AntDeviceConfig(DeviceConfig):
    MAIN_DATA_HUB = DeviceConfig(0, "main data hub")
    LEG_CONTROLLER = DeviceConfig(10, "leg controller")
    HEAD_SENSORS = DeviceConfig(11, "head sensors")
    TAIL_BOARD = DeviceConfig(12, "tail board")
    LEG_SENSORS = DeviceConfig(13, "leg sensors")
    IR_COM = DeviceConfig(14, "ir com")
    PIXY_CONTROLLER = DeviceConfig(42, "pixy controller")
