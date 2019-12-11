from skimage.measure import compare_ssim
import cv2
from datetime import datetime
from time import sleep

class Sentinal:
    def __init__(self, camera):
        self.camera = camera
        self.camera.rotation = 180

    def capture(self):
        sleep(2)
        self.camera.capture('./images/image_%s.jpg' % self.__seconds())

# Score range [-1, 1] with a value of one being a “perfect match”.
# Diff contains the actual image differences between the two input images that
# we wish to visualize.
    def compare(self, images):
        img_one, img_two, img_three = self.__convert_images(images)
        (score1, diff1) = compare_ssim(img_one, img_two, full=True)
        (score2, diff2) = compare_ssim(img_two, img_three, full=True)
        print(f'Score1: {score1}\tScore2: {score2}')

    def off_duty(self):
        self.camera.stop_preview()

    def on_duty(self):
        self.camera.start_preview()
        sleep(5)

    def __convert_images(self, images):
        return self.__grayscale([cv2.imread(image) for image in images])

    def __grayscale(self, images):
        return [cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) for image in images]

    def __seconds(self):
        return (datetime.now() - datetime(2019, 1, 1)).seconds
