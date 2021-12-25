import os
import time

from controllers.outlook_controller import OutlookController

mail = os.getenv('OL_mail')
password = os.getenv('OL_pass')
outlook = OutlookController()

outlook.login(mail, password)

while outlook.are_emails_left():
    outlook.archive_mails()
    time.sleep(1)

outlook.close_page()
