from skimage.measure import compare_ssim
import cv2
from datetime import datetime

class Sentinal:
    def __init__(self, camera):
        self.camera = camera

    def capture(self):
        self.camera.start_preview()
        self.camera.capture('./images/image_%s.jpg' % self.__seconds())
        self.camera.stop_preview()

    def compare(self, images):
        img_one, img_two, img_three = self.__convert_images(images)
        (score, diff) = compare_ssim(img_one, img_two, full=True)
        print(score)

    def __convert_images(self, images):
        return self.__grayscale([cv2.imread(image) for image in images])

    def __grayscale(self, images):
        return [cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) for image in images]

    def __seconds(self):
        return (datetime.now() - datetime(2019, 1, 1)).seconds
