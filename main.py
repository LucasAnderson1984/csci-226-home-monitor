from glob import glob
from picamera import PiCamera
from classes.sentinal import Sentinal
from time import sleep

def main():
    camera = PiCamera()
    camera.rotation = 180

    sentinal = Sentinal(camera)

    images = [image for image in glob('./images/*.jpg')]

    while len(images) < 3:
        sentinal.capture()

    sentinal.compare(images)

if __name__== "__main__":
    main()
