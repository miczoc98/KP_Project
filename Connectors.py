import time

from sds011 import SDS011
import serial


port = "/dev/ttyUSB0"
timeout = 2
unit_of_measure = SDS011.UnitsOfMeasure.MassConcentrationEuropean

sensor = SDS011(port, timeout=timeout, unit_of_measure=unit_of_measure)


def get_values() -> dict:
    timestamp = time.time()

    PM = sensor.get_values()
    pressure_and_temp = _get_pressure_and_temp()

    return {"timestamp": timestamp, "PM2.5": PM[0], "PM10": PM[1], "pressure": pressure_and_temp[0], "temp": pressure_and_temp[1]}


def _get_pressure_and_temp():
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.flush()
    while True:
        if ser.in_waiting > 0:
            return ser.readline().decode('utf-8').rstrip().split(",")
