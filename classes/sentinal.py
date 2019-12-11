from datetime import datetime

class Sentinal:
    def __init__(self, camera):
        self.camera = camera

    def capture(self):
        self.camera.start_preview()
        self.camera.capture('./images/image_%s.jpg' % self.__seconds())
        self.camera.stop_preview()

    def __seconds(self):
        return (datetime.now() - datetime(2019, 1, 1)).seconds
