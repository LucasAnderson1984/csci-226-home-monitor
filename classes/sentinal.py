from skimage.metrics import structural_similarity
import cv2
from datetime import datetime
from time import sleep
import yaml

class Sentinal:
    send_message = True

    def __init__(self, camera, dispatcher):
        self.camera = camera
        self.camera.rotation = 180
        self.dispatcher = dispatcher

        with open(r'./config/application.yml') as file:
            self.application = yaml.load(file, Loader=yaml.FullLoader)

    def capture(self):
        filename = './images/image_%s.jpg' % self.__seconds()
        self.camera.capture(filename)
        return filename

# Score range [-1, 1] with a value of one being a “perfect match”.
# Diff contains the actual image differences between the two input images that
# we wish to visualize.
    def compare(self, images):
        img_one, img_two, img_three = self.__convert_images(images)

        (score1, diff1) = structural_similarity(img_one, img_two, full=True)
        (score2, diff2) = structural_similarity(img_two, img_three, full=True)

        print(f'Score1: {score1}\tScore2: {score2}',
              f'\tDifference: {abs(score1 - score2)}')

        if(abs(score1 - score2) > 0.002):
            if(send_message):
                print("Message Dispatched")
                dispatcher.send_message(self.__detection_message())
                send_message = False
            else:
                print("Movement")

    def off_duty(self):
        self.camera.stop_preview()

    def on_duty(self):
        self.camera.start_preview()
        sleep(3)

    def __convert_images(self, images):
        return self.__grayscale([cv2.imread(image) for image in images])

    def __detection_message(self):
        subject = self.application['MOVEMENT_SUBJECT']
        message = self.application['MOVEMENT_MESSAGE']
        return f'Subject: {subject}\r\n{message}'

    def __grayscale(self, images):
        return [cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) for image in images]

    def __recording_message(self):
        subject = self.application['RECORDING_SUBJECT']
        message = self.application['RECORDING_MESSAGE']
        return f'Subject: {subject}\r\n{message}'

    def __seconds(self):
        return (datetime.now() - datetime(2019, 1, 1)).seconds
