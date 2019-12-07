import os

class Sentinal:
    def __init__(self, camera):
        self.camera = camera

    def capture():
        self.camera.start_preview()
        self.camera.capture('./../images/image_%s.jpg', self.seconds())
        self.camera.stop_preview()

    def __seconds():
        (datetime.datetime.now() - datetime.datetime(2019, 1, 1)).seconds
