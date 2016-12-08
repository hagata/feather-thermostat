import sensor

DEVICE = sensor.Si7021()
print("RUNNING! %s", DEVICE)


while True:
    current_temp = DEVICE.readTemp()
    current_humidity = DEVICE.readRH()

    print("temp: %d\xb0C, humidity: %d%%" % (current_temp, current_humidity))

