from temperature import DHT11
from LCD import LCD
import time

dht11 = DHT11(17)
LCD1602 = LCD(i2c_addr=0x27)
try:
    while True:
        humidity, temperature = dht11.read_data()
        #timestamp = time.time()
        #time_object = datetime.datetime.fromtimestamp(timestamp).strftime("%H:%M:%S")
        #print(f"{time_object}  temperature:{temperature}°C  humidity: {humidity}%")
        #with open("temperature.txt", mode="a") as file:
        #    timestamp = time.time()
        #    time_object = datetime.datetime.fromtimestamp(timestamp).strftime("%H:%M:%S")
        #    file.write(f"\n{time_object}  temperature:{temperature}°C  humidity: {humidity}%")
        LCD1602.message(f"Teplota: {temperature}˚C", 1)
        LCD1602.message(f"Vlhkost: {humidity}%", 2)
        time.sleep(2)
except KeyboardInterrupt:
    LCD1602.clear()
    LCD1602.message("Sensor stopped", 1)
    time.sleep(4)
    LCD1602.clear()