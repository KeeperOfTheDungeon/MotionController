from Config.AntConfig import AntDeviceConfig
from MotionController import MotionController


def main():
    print("Start main()")

    device = MotionController(AntDeviceConfig.HEAD_SENSORS)
    device.run()


main()
