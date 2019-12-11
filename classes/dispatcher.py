import smtplib
import ssl
import yaml

class Dispatcher:
    def __init__(self):
        self.context = ssl.create_default_context()

        with open(r'./config/application.yml') as file:
            self.application = yaml.load(file, Loader=yaml.FullLoader)

    def send_message(self, message)
        with smtplib.SMTP(
            self.application['SMTP_SERVER'],
            self.application['PORT']
        ) as server:
            server.starttls(context=self.context)
            server.login(
                self.application['SENDER_EMAIL'],
                self.application['PASSWORD']
            )
            server.sendmail(
                self.application['SENDER_EMAIL'],
                self.application['RECEIVER_EMAIL'],
                message
            )
