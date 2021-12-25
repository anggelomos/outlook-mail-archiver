from controllers.base_controller import BaseController
from resources.custom_locator import Locator
from selenium.webdriver.common.by import By


class OutlookPages:

    class Login(BaseController):
        def field_email(self):
            locators_list = [Locator(by=By.XPATH, value="//input[@type='email']")]
            return self.robot_driver.get_element(locators_list, timeout=60)

        def field_password(self):
            locators_list = [Locator(by=By.XPATH, value="//input[@type='password']")]
            return self.robot_driver.get_element(locators_list)

        def button_confirm(self):
            locators_list = [Locator(by=By.XPATH, value="//input[@type='submit']")]
            return self.robot_driver.get_element(locators_list)

        def button_dont_remember_account(self):
            locators_list = [Locator(by=By.XPATH, value="//input[@type='button' and @value='No']")]
            return self.robot_driver.get_element(locators_list)

    class Inbox(BaseController):
        def list_unselected_mails(self):
            locators_list = [Locator(by=By.XPATH, value="//div[@aria-label='Selecciona un mensaje' and @aria-checked='false']")]
            return self.robot_driver.get_element(locators_list, multiple_elements=True, timeout=60)

        def button_archive_mails(self):
            locators_list = [Locator(by=By.XPATH, value="//button[@name='Archivo']")]
            return self.robot_driver.get_element(locators_list)
