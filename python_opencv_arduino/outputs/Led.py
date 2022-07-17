import cv2
from typing import Final
import sys


class LedControl:
    def __init__(self):
        self.LedOff: Final = cv2.imread("../resources/Pin13Off.jpg")
        self.LedOn: Final = cv2.imread("../resources/Pin13On.jpg")
        self.key = None

    def turn_led_on(self, delay: int):
        """
        Turns LED on with a specific delay
        :param delay: Integer (Microseconds)
        :return:
        """
        cv2.imshow("On", self.LedOn)
        self.key = cv2.waitKey(delay)
        self.check_close_app()
        cv2.destroyWindow('On')

    def turn_led_off(self, delay: int):
        """
        Turns LED off with a specific delay
        :param delay: Integer (Microseconds)
        :return:
        """
        cv2.imshow("Off", self.LedOff)
        self.key = cv2.waitKey(delay)
        self.check_close_app()
        cv2.destroyWindow('Off')

    def check_close_app(self):
        if self.key == ord('q'):
            sys.exit(0)



