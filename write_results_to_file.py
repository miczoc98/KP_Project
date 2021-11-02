import csv
from sds011 import SDS011


port = "/dev/ttyUSB0"
timeout = 2
unit_of_measure = SDS011.UnitsOfMeasure.MassConcentrationEuropean

if __name__ == '__main__':
    sensor = SDS011(port, timeout=timeout, unit_of_measure=unit_of_measure)

    with open("results.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["PM2.5", "PM10"])
        for i in range(5):
            values = sensor.get_values()
            writer.writerow(values)