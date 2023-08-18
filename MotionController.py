from time import sleep



from RoboControl.Com.Connection.PicoConnection import PicoConnection
from RoboControl.Robot.HardwareDevice.HardwareDevice import HardwareDevice
from RoboControl.Robot.AbstractRobot.Config.DeviceConfig import DeviceConfig


class MotionController(HardwareDevice):
    def __init__(self):
        super().__init__(DeviceConfig(1, "MotionController"))
        self.connect(PicoConnection())


    def run(self):
        print("device - run")
        while True:
            sleep(1)

    def connect(self, connection: PicoConnection) -> None:
        self._connection = connection
        self._connection.connect()  #ToDo insert receiver here
        pass

