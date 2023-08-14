
from MotionController import MotionController


def main():
    print("hallo")
    print("hallo")
    device = MotionController()
    
    """available_ports = SerialConnection.get_ports()
    port = SerialConnection.port if SerialConnection.port in available_ports else available_ports[0].name
    connection = SerialConnection().set_port(port)
    ant.connect(connection)"""

    device.run()


main()