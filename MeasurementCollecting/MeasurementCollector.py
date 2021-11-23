import time

from MeasurementCollecting import ConnectorsMock as Connectors
import Database

time_between_queries_in_s = 1

if __name__ == '__main__':
    Database.create_db()

    start_time = time.time()
    values = Connectors.get_values()
    Database.save_measurement(values)
