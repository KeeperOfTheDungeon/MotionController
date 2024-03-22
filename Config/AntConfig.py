MAIN_DATA_HUB_ID = 0
LEG_CONTROLLER_ID = 10
HEAD_SENSORS_ID = 11
TAIL_BOARD_ID = 12
LEG_SENSORS_ID = 13


class AntDeviceConfig:
    MAIN_DATA_HUB = {"DeviceId": MAIN_DATA_HUB_ID,
                     "DeviceName": "Main Data Hub"}

    HEAD_SENSORS = {"DeviceId": HEAD_SENSORS_ID,
                    "DeviceName": "head sensors"}

    LEG_CONTROLLER = {"DeviceId": LEG_CONTROLLER_ID,
                      "DeviceName": "Motion Controller"}

    LEG_SENSORS = {"DeviceId": LEG_SENSORS_ID,
                   "DeviceName": "leg sensors"}


class HeadSensors:
    FRONT_TMF882x_SENSOR = {
        "name": "front",
        "local_id": 1,
        "global_id": 0,
        "i2c_addr": 0x41
    }

    sensor_list = [
        FRONT_TMF882x_SENSOR
    ]


FRONT_LEFT_LEG_LED = {  # FRONT_LEFT_LEG_LED ("front left",1),
    "name": "front left",
    "local_id": 1,
    "global_id": 0,
    "device_id": LEG_SENSORS_ID
}

FRONT_RIGHT_LEG_LED = {  # FRONT_RIGHT_LEG_LED ("front right",4),
    "name": "front right",
    "local_id": 4,
    "global_id": 0,
    "device_id": LEG_SENSORS_ID
}

CENTER_LEFT_LEG_LED = {  # CENTER_LEFT_LEG_LED ("center left",0),
    "name": "center left",
    "local_id": 0,
    "global_id": 0,
    "device_id": LEG_SENSORS_ID
}

CENTER_RIGHT_LEG_LED = {  # CENTER_RIGHT_LEG_LED ("center right",3),
    "name": "center right",
    "local_id": 3,
    "global_id": 0,
    "device_id": LEG_SENSORS_ID
}

BACK_LEFT_LEG_LED = {  # BACK_LEFT_LEG_LED ("back left",2),
    "name": "back left",
    "local_id": 2,
    "global_id": 0,
    "device_id": LEG_SENSORS_ID
}

BACK_RIGHT_LEG_LED = {  # BACK_RIGHT_LED ("cack right",5),
    "name": "back right",
    "local_id": 5,
    "global_id": 0,
    "device_id": LEG_SENSORS_ID
}

LEFT_LIGHT_SENSOR = {  # BACK_RIGHT_LED ("cack right",5),
    "name": "back right",
    "local_id": 0,
    "global_id": 0,
    "device_id": LEG_SENSORS_ID
}

CENTER_LIGHT_SENSOR = {  # BACK_RIGHT_LED ("cack right",5),
    "name": "back right",
    "local_id": 1,
    "global_id": 0,
    "device_id": LEG_SENSORS_ID
}

RIGHT_LIGHT_SENSOR = {  # BACK_RIGHT_LED ("cack right",5),
    "name": "back right",
    "local_id": 2,
    "global_id": 0,
    "device_id": LEG_SENSORS_ID
}


MOTION_CONTROLLER = {
    "name": "motion controller",
    "local_id": 0,
    "global_id": 0,
    "device_id": LEG_CONTROLLER_ID
}

TEST_SERVO = {
    "name": "test servo",
    "local_id": 1,
    "global_id": 0,
    "device_id": LEG_CONTROLLER_ID
}

TEST_FEEDBACK_SERVO = {
    "name": "test feedback servo",
    "local_id": 1,
    "global_id": 0,
    "device_id": LEG_CONTROLLER_ID
}


class AntComponents:
    def __init__(self):
        pass


class AntComponent:
    def __init__(self, data: dict):
        self._data = data

    @property
    def local_id(self) -> int:
        return self._data["local_id"]

    @property
    def name(self) -> int:
        return self._data["name"]

    @property
    def device_id(self) -> int:
        return self._data["device_id"]

    @property
    def global_id(self) -> int:
        return self._data["global_id"]
