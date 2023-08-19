from time import sleep



from RoboControl.Com.Connection.PicoConnection import PicoConnection
from RoboControl.Com.Remote.RemoteData import RemoteData
from RoboControl.Com.Remote.RemoteDataPacket import RemoteDataPacket
from RoboControl.Robot.HardwareDevice.HardwareDevice import HardwareDevice
from RoboControl.Robot.AbstractRobot.Config.DeviceConfig import DeviceConfig


class MotionController(HardwareDevice):
    def __init__(self):
        super().__init__(DeviceConfig(1, "MotionController"))
        self.connect(PicoConnection())


    def run(self):
        print("device - run")
        while True:    
            input("\nHit enter to send ping")
            data_packet = RemoteDataPacket(11, 1, 3)
            data_packet.set_remote_data(RemoteData(300, 'The coolest', 'The coolest data'))
            self._connection._data_output.transmit(data_packet)

    def connect(self, connection: PicoConnection) -> None:
        self._connection = connection
        self._connection.connect()  #ToDo insert receiver here
        pass

