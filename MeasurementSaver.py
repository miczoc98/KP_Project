import time

import Connectors
import Database

time_between_queries_in_ms = 1000

if __name__ == '__main__':
    start_time = time.time()
    while True:
        if time.time() - start_time > time_between_queries_in_ms:
            values = Connectors.get_values()
            Database.save_measurement(values)
