<<<<<<< HEAD
from datetime import datetime
=======
import os
>>>>>>> User May Capture Images From RaspberryPi Camera

class Sentinal:
    def __init__(self, camera):
        self.camera = camera

<<<<<<< HEAD
    def capture(self):
        self.camera.start_preview()
        self.camera.capture('./images/image_%s.jpg' % self.__seconds())
        self.camera.stop_preview()

    def __seconds(self):
        return (datetime.now() - datetime(2019, 1, 1)).seconds
=======
    def capture():
        self.camera.start_preview()
        self.camera.capture('./../images/image_%s.jpg', self.seconds())
        self.camera.stop_preview()

    def __seconds():
        (datetime.datetime.now() - datetime.datetime(2019, 1, 1)).seconds
>>>>>>> User May Capture Images From RaspberryPi Camera
