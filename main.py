from glob import glob
import os
from picamera import PiCamera
from classes.sentinal import Sentinal

def main():
    image_path = './images/*.jpg'
    sentinal = Sentinal(PiCamera())

    for image in glob(image_path):
        os.remove(image)

    for x in range(3):
        sentinal.capture()

    images = [image for image in glob(image_path)]

    sentinal.compare(images)

if __name__== "__main__":
    main()
