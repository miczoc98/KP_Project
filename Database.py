import sqlite3
import time

db = "db.db"
table = "measurements"

def create_db():
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute('''CREATE TABLE {}
                   (timestamp real, PM2_5 real, PM10 real, pressure real, temperature real)'''.format(table))
    con.commit()
    con.close()

def save_measurement(measurement: dict) -> None:
    con = sqlite3.connect(db)
    cur = con.cursor()

    statement = '''insert into {} (timestamp, PM2_5, PM10, pressure, temperature) values {}, {}, {}, {}, {}'''.format(
        table,
        measurement["timestamp"],
        measurement["PM2.5"],
        measurement["PM10"],
        measurement["pressure"],
        measurement["temperature"]
    )

    cur.execute()
