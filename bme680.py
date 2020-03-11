import threading

import board
import busio
import adafruit_bme680 as bme680

import prometheus_client as prom

# Initialize sensor
bus = busio.I2C(board.SCL, board.SDA)
sensor = bme680.Adafruit_BME680_I2C(bus)

# Temperature metric
temperature = prom.Gauge(
    "bme680_temperature",
    "Temperature sensor of BME680 sensor"
)
temperature.set_function(lambda: sensor.temperature)

# Relative humidity metric
humidity = prom.Gauge(
    "bme680_humidity",
    "Relative humidity of BME680 sensor"
)
humidity.set_function(lambda: sensor.humidity)

# Atmospheric pressure metric
pressure = prom.Gauge(
    "bme680_pressure",
    "Atmospheric pressure of BME680 sensor"
)
pressure.set_function(lambda: sensor.pressure)

# Start metrics server
print("Starting prometheus metrics server on port 9000...")
prom.start_http_server(9000)

# Sleep forever (or until a keyboard interrupt)
event = threading.Event()
event.wait()
