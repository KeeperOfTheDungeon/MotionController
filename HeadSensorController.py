from Config.HeadSensorsProtocol import HeadSensorsProtocol
from Config.HeadSensorsTMF882xSet import HeadSensorsTMF882xSet
from MotionController import MotionController


class HeadSensorController(MotionController):

    def __init__(self, device_meta_data):
        super().__init__(device_meta_data)
        self._tmf8821_set = None

    def build(self):
        protocol = HeadSensorsProtocol(self)

        print("add tmf8821")
        self._tmf8821_set = HeadSensorsTMF882xSet(protocol.get_tmf882x_protocol())
        self.add_component_set(self._tmf8821_set)

    def add_component_protocols(self):
        self.add_command_processor_list(self._tmf8821_set.get_command_processors())
        self.add_message_processor_list(self._tmf8821_set.get_message_processors())
        self.add_stream_processor_list(self._tmf8821_set.get_stream_processors())
