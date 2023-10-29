from time import sleep

from PicoControl.Com.PicoConnection import PicoConnection
from PicoControl.Robot.PicoDevice.PicoDevice import PicoDevice

from RoboControl.Com.RemoteData import RemoteData
from RoboControl.Com.RemoteDataPacket import RemoteDataPacket
from RoboControl.Robot.AbstractRobot.DeviceConfig import DeviceConfig


MOTION_CONTROLLER_ID = 13

import micropython

#for led test
from Config.LegSensorsLedSet import LegSensorsLedSet
from RoboControl.Robot.Component.Actor.LedProtocol import Cmd_getLedBrightness, Cmd_setLedBrightness
from Config.LegSensorsProtocol import LegSensorsProtocol

class MotionController(PicoDevice):
    def __init__(self):
        super().__init__(DeviceConfig(MOTION_CONTROLLER_ID, "MotionController"))
        #self.connect(PicoConnection())
        meta_data = dict()
        print("init motion")
        meta_data["rx_pin"]	= 1		#set receiver pin in meta data
        meta_data["tx_pin"] = 0		#set tranceiver pin in meta data
        meta_data["clock_pin"] = 2
        self._connection = PicoConnection(meta_data)
        self.connect(self._connection)
        self._received = False
        self._data_packet = None
        
        #commection gest output
        self.set_transmitter(self._connection)
        
    def build(self):    
        super().build()
        # leds
        print("add led set")
        self._protocol = LegSensorsProtocol(self)
        self._led_set = LegSensorsLedSet(self._protocol.get_led_protocol())
        self.add_component_set(self._led_set)
    #leds
        self.build_led_protocol()
    

    
    def build_led_protocol(self):
        print ("Dev : Build Protocol")
       
        self.add_command_processor_list(self._led_set.get_command_processors())
        self.add_message_processor_list(self._led_set.get_message_processors())
        self.add_stream_processor_list(self._led_set.get_stream_processors())

     
        
    def run(self):
        print("device - run")
        counter = 0
        while True:
            if (self._received == True):
                print("received : ",self._data_packet)
                super().parse_data_packet(self._data_packet)  ## add to queue convert from there
                self._received = False
                
            if (counter == 10):
                if not self.is_connected():
                    super().remote_ping_device()
                    counter = 0
            
            counter +=1
            sleep(.5)
            #self.remote_ping_device()
#            input("\nHit enter to send ping")
 #           data_packet = RemoteDataPacket(11, 1, 3)
  #          data_packet.set_remote_data(RemoteData(300, 'The coolest', 'The coolest data'))
   #         self._connection._data_output.transmit(data_packet)

    def connect(self, connection: PicoConnection) -> None:
        print("connecting")
        self._connection = connection
        self._connection.connect(self)  #ToDo insert receiver here
        print("connected")
        
        

    def parse_data_packet(self,data_packet):
  
        print("received")
        ## ToDo put into Queue !
        if (data_packet.get_destination_address() == self._id):
            self._received = True
            self._data_packet = data_packet
            micropython.mem_info()
        else:
            print("not for me", self._id )

