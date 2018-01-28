import collections

class Event:
	def __init__(self, timestamp, event_type, event_info, source_sensor):
		self.timestamp=timestamp
		self.event_type=event_type
		self.event_info=event_info
		self.source_sensor=source_sensor

	def __repr__(self):
		return "Event("+repr(self.timestamp)+", "+repr(self.event_type)+", "+repr(self.event_info)+", "+repr(self.source_sensor)+")"

class Sensor:
	def __init__(self, id, sensor_type, sensor_name):
		self.id=id
		self.sensor_type=sensor_type
		self.sensor_name=sensor_name
		self.data=[]
		self.associated_player=None

	def add_datapoint(self, timestamp, value):
		self.data.append((timestamp, value))

	def __repr__(self):
		return "Sensor("+str(self.id)+", "+repr(self.sensor_type)+", "+repr(self.sensor_name)+")"

class Player:
	def __init__(self, id, name, info):
		self.id=id
		self.name=name
		self.info=info
		self.events=[]
		self.sensors=[]

	def get_events(self, number=10):
		taken = []
		for event in self.events:
			if len(taken) < number:
				taken.append(event)
		return taken

	def associate_sensor(self, sensor):
		self.sensors.append(sensor)
		sensor.associated_player=self

	def add_event(self, event):
		self.events.append(event)

	def __repr__(self):
		return "Player("+str(self.id)+", "+repr(self.name)+", "+repr(self.info)+", events=["+", ".join(map(repr, self.events))+"])"
