from time import sleep



from RoboControl.Com.Connection.PicoConnection import PicoConnection
from RoboControl.Com.Remote.RemoteData import RemoteData
from RoboControl.Com.Remote.RemoteDataPacket import RemoteDataPacket
from RoboControl.Robot.AbstractRobot.Config.DeviceConfig import DeviceConfig
from PicoControl.Robot.PicoDevice.PicoDevice import PicoDevice

class MotionController(PicoDevice):
    def __init__(self):
        super().__init__(DeviceConfig(1, "MotionController"))
        #self.connect(PicoConnection())
        meta_data = dict()
        meta_data["Cherry"] = 1
        meta_data["Cherry"] = 10
        
        meta_data["rx_pin"]	= 0		#set receiver pin in meta data
        meta_data["tx_pin"] = 1		#set tranceiver pin in meta data
        
        self.connect(PicoConnection(meta_data))
        self._received = False
        self._data_packet = None
        
        self.build_protocol()
        
        
    def run(self):
        print("device - run")
        while True:
            if (self._received == True):
                print(self._data_packet)
                super().parse_data_packet(self._data_packet)  ## add to queue convert from there
                self._received = False
                
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
