## Home Security with Raspberry Pi
#### By Lucas Anderson and Sean Raborg

## Summary
The purpose of this project is to create a home security system using a Raspberry Pi. The program captures three images and compares two sets of pairs, e.g. (img_one, img_two) and (img_two, img_three). The program uses scikit-image to compare the differences of each image and then gives them a score. Each image is grayscaled to reduce color and shading differences to increase the accuracy of their comparisons.  Each pair is scored on how closely related they are. The absolute value of the difference is returned. If the score difference is greater than 0.2% then movement is detected.

If there is movement detected the camera will start recording. At the same time an email will be sent to the building's owner to notify them there was movement. The camera will continue taking pictures at a 9 second interval to see if it still detects movement. Once the score difference becomes less than the 0.2% threshold, the camera will stop recording and then upload the video to an Amazon AWS S3 folder so the owner can view/store the recording. After that the program will continue to take pictures and comparing them.

After the comparison, the oldest picture in the images folder is deleted. This is done in order to keep the file size down. After that the next picture is taken and then  the next image is captured and the comparison is started again.  After the recording is uploaded to the S3 folder, the local copy is deleted.

## Setup

#### Linux libraries to install
```
sudo apt-get install build-essential
sudo apt-get cython3
sudo apt-get install python3-matplotlib
sudo apt-get install python3-numpy
sudo apt-get install python3-pil
sudo apt-get install python3-pip
sudo apt-get install python3-scipy
sudo apt-get install python3-tk
```

#### Python libraries to install
```
pip3 install --upgrade DateTime
pip3 install --upgrade glob3
pip3 install --upgrade opencv-python
pip3 install --upgrade picamera
pip3 install --upgrade scikit-image
```

#### Application.yml
Copy application.example.yml and rename it application.yml. Change the values in the yaml file with the correct emails, passwords, etc. to connect to your email provider and send your message.

###### Command Line Copy in Linux
```
cp config/application.example.yml config/application.yml
```
