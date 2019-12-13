from skimage.metrics import structural_similarity
import cv2
from datetime import datetime
from time import sleep
import yaml

# Compares images to determine of there is any movement detected. Once detected
# it triggers the camera to start recording and sends a message to owner of
# movement being detected. Once there is no more movement detected, it sends
# another email about uploading a video to AWS S3 bucket.
class Sentinal:
    send_message = True

    # Inialize camera, watchmen and dispatcher. Rotates camera 180 degrees. Load
    # yaml file for application.
    def __init__(self, camera, dispatcher, watchmen):
        self.camera = camera
        self.camera.rotation = 180
        self.dispatcher = dispatcher
        self.watchmen = watchmen

        with open(r'./config/application.yml') as file:
            self.application = yaml.load(file, Loader=yaml.FullLoader)

    def capture(self):
        filename = './images/image_%s.jpg' % self.__seconds()
        self.camera.capture(filename)
        return filename

    # Used to compare a list of images to detect movement. If movement is found
    # then an email is sent and the camera is told to start recording
    def compare(self, images):
        # Convert images to grayscale
        img_one, img_two, img_three = self.__convert_images(images)

        # Score range [-1, 1] with a value of one being a “perfect match”.
        # Diff contains the actual image differences between the two input
        # images that we wish to visualize.
        (score1, diff1) = structural_similarity(img_one, img_two, full=True)
        (score2, diff2) = structural_similarity(img_two, img_three, full=True)

        # Prints the pair image score (img_one, img_two), (img_two, img_three)
        # and then displays the abs score difference between the two
        print(f'Score1: {score1}\tScore2: {score2}',
              f'\tDifference: {abs(score1 - score2)}')

        # Checks to see if score difference is over the threshold, which
        # indicates there is movement. Once True, then a message is sent and
        # the video will start recording and an email is sent.
        if abs(score1 - score2) > 0.002:
            if(self.send_message):
                print("Message Dispatched")
                self.dispatcher.send_message(self.__detection_message())
                self.watchmen.start_capture()
                self.send_message = False
            else:
                print("Movement")

        # If there is not longer any movement detected, then upload the
        # recording to AWS S3 bucket and reset message state.
        if abs(score1 - score2) < 0.002 and not self.send_message:
            print("Recording Uploaded")
            self.watchmen.stop_capture()
            sleep(1)
            self.dispatcher.store_video()
            self.send_message = True

    # Turns off camera
    def off_duty(self):
        self.camera.stop_preview()

    # Turns on camera
    def on_duty(self):
        self.camera.start_preview()
        sleep(3)

    # Returns grayscaled images
    def __convert_images(self, images):
        return self.__grayscale([cv2.imread(image) for image in images])

    # Detection message used for email
    def __detection_message(self):
        subject = self.application['MOVEMENT_SUBJECT']
        message = self.application['MOVEMENT_MESSAGE']
        return f'Subject: {subject}\r\n{message}'

    # Grayscales images
    def __grayscale(self, images):
        return [cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) for image in images]

    # Recorded message used for email
    def __recording_message(self):
        subject = self.application['RECORDING_SUBJECT']
        message = self.application['RECORDING_MESSAGE']
        return f'Subject: {subject}\r\n{message}'

    # Gets the current seconds from the beginning of the year to uniquely name
    # images.
    def __seconds(self):
        return (datetime.now() - datetime(2019, 1, 1)).seconds
