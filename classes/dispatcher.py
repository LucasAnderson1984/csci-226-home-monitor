import boto3
from botocore.exceptions import NoCredentialsError
from glob import glob
import os
import smtplib
import ssl
import yaml

# Used to send emails and store videos to AWS S3 bucket
class Dispatcher:
    # initialize and load yaml file to application
    def __init__(self):
        with open(r'./config/application.yml') as file:
            self.application = yaml.load(file, Loader=yaml.FullLoader)

    # Sends an email to building owner
    def send_message(self, message):
        context = ssl.create_default_context()
        # Set up email server and port
        with smtplib.SMTP(
            self.application['SMTP_SERVER'],
            self.application['PORT']
        ) as server:
            # Login with credentials
            server.starttls(context=context)
            server.login(
                self.application['USERNAME'],
                self.application['PASSWORD']
            )
            # Send email to user from sender with message
            server.sendmail(
                self.application['SENDER_EMAIL'],
                self.application['RECEIVER_EMAIL'],
                message
            )

    # Uploads video to AWS S3 bucket
    def store_video(self):
        # Get video file in videos folder
        file = glob('videos/*.h264')[0]

        # Load S3 credentials
        s3 = boto3.client(
            's3',
            aws_access_key_id=self.application['S3_ACCESS_KEY'],
            aws_secret_access_key=self.application['S3_SECRET_KEY']
        )

        # Try to upload video to S3
        try:
            s3.upload_file(
                file,
                self.application['S3_BUCKET'],
                file
            )
            print("Upload Successful")
            return True
        except FileNotFoundError:
            print("The file was not found")
            return False
        except NoCredentialsError:
            print("Credentials not available")
            return False
