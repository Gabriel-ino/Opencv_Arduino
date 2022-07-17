from Led import LedControl
from cvzone.SerialModule import SerialObject


def main():
    arduino_board = SerialObject('/dev/ttyUSB0')
    led = LedControl()

    while True:
        arduino_board.sendData([1])
        led.turn_led_on(1000)
        arduino_board.sendData([0])
        led.turn_led_off(1000)


if __name__ == "__main__":
    main()
