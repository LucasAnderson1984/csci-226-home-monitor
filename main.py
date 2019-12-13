from datetime import datetime
from classes.dispatcher import Dispatcher
from glob import glob
import os
from picamera import PiCamera
from select import select
from classes.sentinal import Sentinal
import sys
from time import sleep

# Home security program that compares 3 images to see if there is enough of a
# difference to be classified as movement. If there is movement detected, the
# camera starts recording and an email sends an email to the building's owner.
# Once movement stops, the camera stops recording and the video gets uploaded
# to an AWS S3 bucket. Another email is sent to owner about the video being
# stored online so they can view it.
def main():
    print('Start program:', datetime.now())
    image_path = './images/*.jpg' # Path to images folder

    # Delete any images in the images folder
    for image in glob(image_path):
        os.remove(image)

    print('Start sentinal:', datetime.now())
    # Initialize Sentinal with camera, dispatcher and watchmen instance
    sentinal = Sentinal(PiCamera(), Dispatcher())
    sentinal.on_duty() # Turn camera on

    # Take first three photos every 2 seconds
    print('Start capture:', datetime.now())
    for x in range(3):
        sentinal.capture()
        sleep(2)

    # Load images into List and make sure they're not reordered
    images = [image for image in glob(image_path)]
    images.sort(reverse=False)

    print(images)

    # Loop continuously to detect movement by taking pictures after each
    # comparison. Once the images are compared, the older image is deleted and
    # a new picture is taken and added to the List.
    print('Start compare:', datetime.now())
    while True:
        # Used to stop loop when enter key is pressed
        sleep(1)
        i,o,e = select([sys.stdin],[],[],0.0001)
        if i == [sys.stdin]: break

        # Compare and then capture new images
        print('Comparing:', datetime.now())
        sentinal.compare(images)
        old_image = images.pop(0)
        print('Deleting image:', old_image)
        os.remove(old_image)
        new_image = sentinal.capture()
        print('Storing new image:', new_image)
        images.append(new_image)

    print('Start Off Duty:', datetime.now())
    sentinal.off_duty() # Turn off camera
    print('End program:', datetime.now())

if __name__== "__main__":
    main()
