import time

from sds011 import SDS011
import serial


usb_port = "/dev/ttyUSB0"
timeout = 1
unit_of_measure = SDS011.UnitsOfMeasure.MassConcentrationEuropean

sensor = SDS011(usb_port, timeout=timeout, unit_of_measure=unit_of_measure)

serial_port = '/dev/ttyACM0'


def get_values() -> dict:
    timestamp = time.time()

    PM = sensor.get_values()
    pressure_and_temp = _get_pressure_and_temp()

    return {"timestamp": timestamp, "PM2_5": PM[0], "PM10": PM[1], "pressure": pressure_and_temp[0], "temperature": pressure_and_temp[1]}


def _get_pressure_and_temp():
    ser = serial.Serial(serial_port, 9600, timeout=timeout)
    ser.flush()
    ser.write(b'0')

    start_time = time.time()
    current_time = 0
    while current_time < 10:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            values =  line.split(',')
            if len(values) != 2:
                print("invalid value read from serial: " + line)
                return 0, 0
            return float(values[0]), float(values[1])

        current_time = time.time() - start_time

    print("timeout while waiting for response from serial")
    return 0, 0