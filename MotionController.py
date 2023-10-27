from time import sleep

from PicoControl.Com.PicoConnection import PicoConnection
from PicoControl.Robot.PicoDevice.PicoDevice import PicoDevice

from RoboControl.Com.RemoteData import RemoteData
from RoboControl.Com.RemoteDataPacket import RemoteDataPacket
from RoboControl.Robot.AbstractRobot.DeviceConfig import DeviceConfig

class MotionController(PicoDevice):
    def __init__(self):
        super().__init__(DeviceConfig(1, "MotionController"))
        #self.connect(PicoConnection())
        meta_data = dict()
        
        meta_data["rx_pin"]	= 1		#set receiver pin in meta data
        meta_data["tx_pin"] = 0		#set tranceiver pin in meta data
        meta_data["clock_pin"] = 2
        self._connection = PicoConnection(meta_data)
        self.connect(self._connection)
        self._received = False
        self._data_packet = None
        
        self.build_protocol()
    
        #commection gest output
        self.set_transmitter(self._connection)
    
    def build_protocol(self):
        print ("Dev : Build Protocol")
        super().build_protocol()
        
      #  self._remote_command_processor_list.append(
       #     RemoteProcessor(Cmd_ping(DeviceProtocol.CMD_PING), self.process_led_on_command))  +insert KED 

        
        
    def run(self):
        print("device - run")
        counter = 0
        while True:
            if (self._received == True):
                print("received : ",self._data_packet)
                super().parse_data_packet(self._data_packet)  ## add to queue convert from there
                self._received = False
                
            if (counter == 10):   
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
        self._received = True
        self._data_packet = data_packet

#print(remote_data)
