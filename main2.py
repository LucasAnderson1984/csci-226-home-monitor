from picamera import PiCamera
from time import sleep
from classes.watchmen import Watchmen
import subprocess


watchmen = Watchmen()
print("attempting to record")
watchmen.start_capture()

sleep(10)

print("sending flag to stop")
watchmen.stop_capture()



# os_user = subprocess.call("whoami", shell=True)
# camera = PiCamera()
# path = "/home/sean/video.h264"
# camera.start_preview()
# camera.start_recording(path)
# sleep(10)
# camera.stop_recording()
# camera.stop_preview()