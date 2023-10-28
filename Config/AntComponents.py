from AntDeviceConfig import AntDeviceConfig


FRONT_LEFT_LEG_LED = {  # FRONT_LEFT_LEG_LED ("front left",1),
    "name": "front left",
    "local_id": 1,
    "global_id": 0,
    "device_id": AntDeviceConfig.LEG_SENSORS.get_id(),
}

FRONT_RIGHT_LEG_LED = {  # FRONT_RIGHT_LEG_LED ("front right",4),
    "name": "front right",
    "local_id": 4,
    "global_id": 0,
    "device_id": AntDeviceConfig.LEG_SENSORS.get_id(),
}

CENTER_LEFT_LEG_LED = {  # CENTER_LEFT_LEG_LED ("center left",0),
    "name": "center left",
    "local_id": 0,
    "global_id": 0,
    "device_id": AntDeviceConfig.LEG_SENSORS.get_id(),
}

CENTER_RIGHT_LEG_LED = {  # CENTER_RIGHT_LEG_LED ("center right",3),
    "name": "center right",
    "local_id": 3,
    "global_id": 0,
    "device_id": AntDeviceConfig.LEG_SENSORS.get_id(),
}

BACK_LEFT_LEG_LED = {  # BACK_LEFT_LEG_LED ("back left",2),
    "name": "back left",
    "local_id": 2,
    "global_id": 0,
    "device_id": AntDeviceConfig.LEG_SENSORS.get_id(),
}

BACK_RIGHT_LEG_LED = {  # BACK_RIGHT_LED ("cack right",5),
    "name": "back right",
    "local_id": 5,
    "global_id": 0,
    "device_id": AntDeviceConfig.LEG_SENSORS.get_id(),
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
