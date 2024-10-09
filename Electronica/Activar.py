import gpiod
import time
#Definición del pin de salida
LED_PIN = 23 

with gpiod.request_lines(
    "/dev/gpiochip0",
    consumer="blink-example",
    config={
        LINE: gpiod.LineSettings(
            direction=Direction.OUTPUT, output_value=Value.ACTIVE
        )
    },
) as request:
    while True:
        request.set_value(LINE, Value.ACTIVE)
        time.sleep(1)
        request.set_value(LINE, Value.INACTIVE)
        time.sleep(1)


