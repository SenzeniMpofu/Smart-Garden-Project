import threading

import board
import busio
import adafruit_seesaw.seesaw as seesaw

import prometheus_client as prom

# Initialize sensor
bus = busio.I2C(board.SCL, board.SDA)
sensor = seesaw.Seesaw(bus, addr=0x36)

# Connect moisture read to moisture metric
moisture = prom.Gauge("soil_moisture", "Soil Moisture reading from STEMMA capacative sensor")
moisture.set_function(sensor.moisture_read)

# Connect temperature read to metric
temperature = prom.Gauge("temperature", "Ambiant temperature reading from STEMMA capacative sensor")
temperature.set_function(sensor.get_temp)

# Start metrics server
print("Starting prometheus metrics server on port 9000...")
prom.start_http_server(9000)

# Sleep forever (or until a keyboard interrupt)
event = threading.Event()
event.wait()
