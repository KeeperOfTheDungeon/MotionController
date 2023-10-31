
MAIN_DATA_HUB_ID = 0
MOTION_CONTROLLER_ID = 13

class AntDeviceConfig:
    MAIN_DATA_HUB = {"DeviceId" : MAIN_DATA_HUB_ID,
                     "DeviceName" : "Main Data Hub"}

    LEG_CONTROLLER = {"DeviceId" : MOTION_CONTROLLER_ID,
                     "DeviceName" : "Motion Controller"}

    #LEG_CONTROLLER = DeviceConfig(10, "leg controller")
    #HEAD_SENSORS = DeviceConfig(11, "head sensors")
    #TAIL_BOARD = DeviceConfig(12, "tail board")
    #LEG_SENSORS = DeviceConfig(13, "leg sensors")
    #IR_COM = DeviceConfig(14, "ir com")
    #PIXY_CONTROLLER = DeviceConfig(42, "pixy controller")
