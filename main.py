from datetime import datetime
from glob import glob
import os
from picamera import PiCamera
from classes.sentinal import Sentinal
from time import sleep

def main():
    print('Start program:', datetime.now())
    image_path = './images/*.jpg'

    for image in glob(image_path):
        os.remove(image)

    print('Start sentinal:', datetime.now())
    sentinal = Sentinal(PiCamera())
    sentinal.on_duty()

    print('Start capture:', datetime.now())
    for x in range(3):
        sentinal.capture()
        sleep(2)

    images = [image for image in glob(image_path)]
    images.sort(reverse=False)

    print(images)

    print('Start compare:', datetime.now())
    for x in range(20):
        print('Comparing:', datetime.now())
        sentinal.compare(images)
        os.remove(images.pop(0))
        images.append(sentinal.capture())

    print('Start Off Duty:', datetime.now())
    sentinal.off_duty()
    print('End program:', datetime.now())

if __name__== "__main__":
    main()
