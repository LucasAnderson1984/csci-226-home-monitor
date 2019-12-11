from picamera import PiCamera
from classes.sentinal import Sentinal
from time import sleep

def main():
    camera = PiCamera()
    camera.rotation = 180

    sentinal = Sentinal(camera)
    sentinal.capture()

if __name__== "__main__":
    main()
