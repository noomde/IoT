from machine import Pin
import dht
import network
import time
import ujson
from umqtt.simple import MQTTClient

# Example CONFIG
# -------------------
WIFI_SSID = "Wokwi-GUEST"
WIFI_PASSWORD = ""

MQTT_BROKER = "broker.emqx.io"
STUDENT_ID = "your_student_id"

SENSOR_TOPIC = f"lnu/iot/{STUDENT_ID}/sensor"
LED_TOPIC = f"lnu/iot/{STUDENT_ID}/command/led"

# HARDWARE
# -------------------
sensor = dht.DHT22(Pin(33))
led = Pin(27, Pin.OUT)

# WIFI CONNECT
# -------------------
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(WIFI_SSID, WIFI_PASSWORD)

print("Connecting to WiFi...")

while not wifi.isconnected():
    print(".", end="")
    time.sleep(0.2)

print("\nConnected to WiFi!")

# MQTT CALLBACK
# -------------------
def on_message(topic, msg):
    print("Incoming:", topic, msg)

    try:
        data = ujson.loads(msg)

        print(data)

        if topic.decode() == LED_TOPIC:
            if data["state"] is True:
                led.on()
            else:
                led.off()

    except Exception as e:
        print("MQTT parse error:", e)

# MQTT CONNECT
# -------------------
client = MQTTClient(
    client_id=STUDENT_ID,
    server=MQTT_BROKER
)

client.set_callback(on_message)
client.connect()

print("Connected to MQTT broker!")

client.subscribe(LED_TOPIC)
print("Subscribed to:", LED_TOPIC)

# MAIN LOOP
# -------------------
while True:
    try:
        client.check_msg()

        sensor.measure()
        temp = sensor.temperature()

        payload = {
            "studentId": STUDENT_ID,
            "type": "temperature",
            "deviceId": "esp32-01",
            "unit": "C",
            "value": temp
        }

        json_payload = ujson.dumps(payload)
        client.publish(SENSOR_TOPIC, json_payload)

        print("Published:", json_payload)
    except Exception as e:
        print("Error:", e)

    time.sleep(2)
