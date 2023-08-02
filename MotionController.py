from time import sleep



from RoboControl.Com.Connection.PicoConnection import PicoConnection
from RoboControl.Robot.HardwareDevice.HardwareDevice import HardwareDevice



class MotionController(HardwareDevice):
	def __init__(self):
		super().__init__("MotionController")



	def run(self):
		while True:
#			self._data_hub.remote_ping_device()
			sleep(1)

def connect(self, connection: PicoConnection) -> None:
		self._connection = connection
		#super().connect(connection)

"""
	def run(self):
		while True:
			self._data_hub.remote_ping_device()
			sleep(1)


		self.add_devices()

	def add_devices(self):
		self._data_hub = DataHub(AntDeviceConfig.MAIN_DATA_HUB)
		self._device_list.append(self._data_hub)
		self._data_hub.set_transmitter(self._connection)

		self._head_sensors = HeadSensors(AntDeviceConfig.HEAD_SENSORS)
		self._device_list.append(self._head_sensors)
		self._head_sensors.set_transmitter(self._connection)

		self._leg_sensors = LegSensors(AntDeviceConfig.LEG_SENSORS)
		self._device_list.append(self._leg_sensors)
		self._leg_sensors.set_transmitter(self._connection)

		self._leg_controller = LegController(AntDeviceConfig.LEG_CONTROLLER)
		self._device_list.append(self._leg_controller)
		self._leg_controller.set_transmitter(self._connection)

	def get_head_sensors(self):
		return self._head_sensors

	def get_leg_sensors(self):
		return self._leg_sensors

	def get_leg_controller(self):
		return self._leg_controller

	def get_data_hub(self):
		return self._data_hub

"""