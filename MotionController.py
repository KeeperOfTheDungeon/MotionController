from time import sleep

from Config.HeadSensorsProtocol import HeadSensorsProtocol
from Config.HeadSensorsTMF882xSet import HeadSensorsTMF882xSet
from PicoControl.com.PicoConnection import PicoConnection
from PicoControl.Robot.PicoDevice.PicoDevice import PicoDevice

import micropython

# for led test
from Config.LegSensorsLedSet import LegSensorsLedSet
from Config.LegSensorsLightSensorSet import LegSensorsLightSensorSet
from Config.LegSensorsProtocol import LegSensorsProtocol
from RoboControl.Com.RemoteDataPacket import RemoteDataPacket


class MotionController(PicoDevice):
    def __init__(self, device_meta_data):
        super().__init__(device_meta_data)
        # self.connect(PicoConnection())
        meta_data = dict()
        print("init motion")
        meta_data["rx_pin"] = 1  # set receiver pin in meta data
        meta_data["tx_pin"] = 0  # set transceiver pin in meta data
        meta_data["clock_pin"] = 2
        self._connection = PicoConnection(meta_data)
        self.connect(self._connection)
        self._received = False
        self._data_packet = None

        # connection gest output
        print(self._connection)
        self.set_transmitter(self._connection)

    def build(self):
        super().build()
        protocol = LegSensorsProtocol(self)

        # leds
        print("add led set")
        self._led_set = LegSensorsLedSet(protocol.get_led_protocol())
        self.add_component_set(self._led_set)
        print("self._light_sensor_set", self._led_set)

        # micropython.mem_info()
        self._light_sensor_set = LegSensorsLightSensorSet(protocol.get_light_sensor_protocol())
        self.add_component_set(self._light_sensor_set)
        # micropython.mem_info()
        # self.build_led_protocol()

        print("add tmf8821")
        self._tmf8821_set = HeadSensorsTMF882xSet(HeadSensorsProtocol(self).get_tmf882x_protocol())
        self.add_component_set(self._tmf8821_set)

        self.add_component_protocols()

    def add_component_protocols(self):
        print("Dev : Build Protocol")

        self.add_command_processor_list(self._led_set.get_command_processors())
        self.add_message_processor_list(self._led_set.get_message_processors())
        self.add_stream_processor_list(self._led_set.get_stream_processors())

        self.add_command_processor_list(self._light_sensor_set.get_command_processors())
        self.add_message_processor_list(self._light_sensor_set.get_message_processors())
        self.add_stream_processor_list(self._light_sensor_set.get_stream_processors())

        self.add_command_processor_list(self._tmf8821_set.get_command_processors())
        self.add_message_processor_list(self._tmf8821_set.get_message_processors())
        self.add_stream_processor_list(self._tmf8821_set.get_stream_processors())

    def run(self):
        print("device - run")
        counter = 0
        while True:
            if self._received == True:
                print("received : ", self._data_packet)
                super().parse_data_packet(self._data_packet)  ## add to queue convert from there
                self._received = False

            if counter == 10:
                if not self.is_connected():
                    super().remote_ping_device()
                    counter = 0

            counter += 1
            sleep(.5)
            # self.remote_ping_device()

    #            input("\nHit enter to send ping")
    #          data_packet.set_remote_data(RemoteData(300, 'The coolest', 'The coolest data'))
    #         self._connection._data_output.transmit(data_packet)

    def connect(self, connection: PicoConnection) -> None:
        print("connecting")
        self._connection = connection
        self._connection.connect(self)  # ToDo insert receiver here
        print("connected")

    def parse_data_packet(self, data_packet):

        print("received")
        ## ToDo put into Queue !
        if (data_packet.get_destination_address() == self._id):
            self._received = True
            self._data_packet = data_packet
            micropython.mem_info()
        else:
            print("not for me", self._id)
