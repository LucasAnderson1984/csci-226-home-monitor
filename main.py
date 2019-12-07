from picamera import PiCamera
from time import sleep

def main():
    camera = PiCamera()
    camera.rotation = 180

if __name__== "__main__":
    main()
