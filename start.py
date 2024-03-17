from Config.AntConfig import AntDeviceConfig
from HeadSensorController import HeadSensorController
from MotionController import MotionController

device_type = AntDeviceConfig.HEAD_SENSORS
device: MotionController


def main():
    global device
    print("Start main()")

    if device_type == AntDeviceConfig.HEAD_SENSORS:
        device = HeadSensorController(device_type)
    else:
        device = MotionController(device_type)

    device.run()


main()
