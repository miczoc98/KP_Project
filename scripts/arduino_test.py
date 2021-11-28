import time
import serial

time_between_queries_in_s = 1

def get_values():
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=2)
    ser.flush()
    ser.write(b'00000')
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            return line

if __name__ == '__main__':
    wait_start_time = time.time()
    current_wait_time = 0

    while True:
        while current_wait_time < time_between_queries_in_s:
            current_wait_time = time.time() - wait_start_time

        values = get_values()
        # Database.save_measurement(values)
        print(values)

        current_wait_time = 0
        wait_start_time = time.time()

