import time

from controllers.base_controller import BaseController
from controllers.outlook_pages import OutlookPages


class OutlookController(BaseController):

    outlook_url = "https://outlook.live.com/owa/?nlp=1"

    def __init__(self):
        super().__init__()
        self.robot_driver.driver.get(self.outlook_url)

    def login(self, email: str, password: str):        
        OutlookPages.Login().field_email().send_keys(email)
        OutlookPages.Login().button_confirm().click()
        OutlookPages.Login().field_password().send_keys(password)
        OutlookPages.Login().button_confirm().click()
        OutlookPages.Login().button_dont_remember_account().click()

    def archive_mails(self):
        unselected_mails = OutlookPages.Inbox().list_unselected_mails()

        for mail in unselected_mails:
            mail.click()

        OutlookPages.Inbox().button_archive_mails().click()
        time.sleep(0.5)
        self.refresh_page()

    def are_emails_left(self) -> bool:
        return self.robot_driver.is_element_present(OutlookPages.Inbox().list_unselected_mails()[0], timeout=60)

    def refresh_page(self):
        self.robot_driver.driver.refresh()

    def close_page(self):
        self.robot_driver.close_driver()
