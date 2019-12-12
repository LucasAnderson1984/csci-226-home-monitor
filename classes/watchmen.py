import numpy as np
import threading
import cv2

class Watchmen(self):

    def __init__(self, camera):
        self.camera = camera
        self._stop_flag = False

    def start_capture(self):

        self._stop_flag = False

        # Run Video Capture Thread
        thread1 = threading.Thread(target=self._capture_thread)
        thread1.start()

    def _capture_thread(self, capture_object):

        capture_object = cv2.VideoCapture(0)

        while capture_object.isOpened():

            success, frame = capture_object.read()

            if success:
                cv2.imshow('Frame', frame)          # Show the thread - Need to change to saving to file

            if self._stop_flag:
                break

        capture_object.release()                # Release the video capture object
        cv2.destroyAllWindows()                 # Close Frames

    def stop_capture(self):
        self._stop_flag = True
