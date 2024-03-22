from Config.AntConfig import AntDeviceConfig
from HeadSensorController import HeadSensorController
from MotionController import MotionController

device_type = AntDeviceConfig.HEAD_SENSORS

def main():
    print("Start main()")

    device = HeadSensorController(AntDeviceConfig.HEAD_SENSORS)
    device.run()


main()
