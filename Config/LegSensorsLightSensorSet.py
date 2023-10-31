from Config import AntConfig
from PicoControl.Robot.Component.LightSensorPico import LightSensorSetPico




class LegSensorsLightSensorSet(LightSensorSetPico):

    def __init__(self, protocol):
        AntConfig.LEFT_LIGHT_SENSOR["protocol"] = protocol
        AntConfig.CENTER_LIGHT_SENSOR["protocol"] = protocol
        AntConfig.RIGHT_LIGHT_SENSOR["protocol"] = protocol


        sensor_list = [
            AntConfig.LEFT_LIGHT_SENSOR,
            AntConfig.CENTER_LIGHT_SENSOR,
            AntConfig.RIGHT_LIGHT_SENSOR,
        ]
        
        adc_channel_list =[26,27,28]
        
        super().__init__(sensor_list, adc_channel_list, protocol)