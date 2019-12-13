from datetime import datetime
from time import sleep
import threading

class Watchmen:

    ##
    # Constructor
    #
    # @param path The base directory where video files should be saved
    #
    def __init__(self, camera, path="./videos/"):
        self._camera = camera
        self._stop_flag = False
        self._path = path

    ##
    # Starts Video capturing
    #
    def start_capture(self):

        self._stop_flag = False

        # Run Video Capture Thread
        thread1 = threading.Thread(target=self._capture_thread)
        thread1.start()

    ##
    # Code to start camera hardware recording
    #
    def _capture_thread(self):

        file_name = self._path + "video_%s.h264" % self.__seconds()
        try:
            print("Started Recording:" % datetime.now())
            self._camera.start_recording(file_name)
            while(self._stop_flag == False):
                sleep(1)
        finally:
            print("Stopped Recording:" % datetime.now())
            self._camera.stop_recording()

    ##
    # Stops Video Capture
    #
    # Sends flag to stop recording thread
    #
    def stop_capture(self):
        self._stop_flag = True


    ##
    # Helper function to create a unique timestamp
    #
    def __seconds(self):
        return (datetime.now() - datetime(2019, 1, 1)).seconds
