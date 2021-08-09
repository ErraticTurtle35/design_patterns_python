from abc import ABC, abstractmethod

# Abstract class
from random import randint


class SensorObserver(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def do_something(self, sensor_value):
        pass


class LightSensorObserver(SensorObserver):
    def do_something(self, sensor_value):
        if sensor_value > 50:
            print("TURN ON LIGHTS FOR SENSOR VALUE: {} IN {}".format(sensor_value, self.name))


class HornSensorObserver(SensorObserver):
    def do_something(self, sensor_value):
        if sensor_value > 80:
            print("BEEP BEEP BEEP! FOR SENSOR VALUE: {} IN {}".format(sensor_value, self.name))


class SensorSystem:
    def __init__(self):
        self.sensors = []

    def assign_sensor(self, sensor):
        self.sensors.append(sensor)

    def pop_last_sensor(self):
        self.sensors.pop()

    def notify_sensor_observers(self, sensor_value):
        for sensor in self.sensors:
            sensor.do_something(sensor_value)


if __name__ == '__main__':
    sensor_value_capture = randint(0, 100)

    bed_room_light_sensor = LightSensorObserver('Bedroom Light:')
    bathroom_light_sensor = LightSensorObserver('Bathroom Light:')
    bathroom_horn_sensor = HornSensorObserver('Bathroom Light:')
    kitchen_light_sensor = LightSensorObserver('Kitchen Light:')

    sensor_system = SensorSystem()
    sensor_system.assign_sensor(bed_room_light_sensor)
    sensor_system.assign_sensor(bathroom_light_sensor)
    sensor_system.assign_sensor(bathroom_horn_sensor)
    sensor_system.assign_sensor(kitchen_light_sensor)
    while sensor_value_capture > 0:
        sensor_system.notify_sensor_observers(sensor_value_capture)
        sensor_value_capture = randint(0, 100)
