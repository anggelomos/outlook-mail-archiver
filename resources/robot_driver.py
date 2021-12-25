from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from resources.exceptions import ElementNotFoundException
from resources.expected_conditions import any_element_with_locators_is_visible


class RobotDriver():
    driver_options = Options()
    driver_options.headless = False
    # driver_options.add_argument("--incognito")
    driver_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=driver_options)
    element_timeout = 10

    def get_element(self, element_locator, timeout:int = 0, dynamic_element:bool = False, multiple_elements:bool = False) -> WebElement:

        if timeout == 0:
            timeout = self.element_timeout

        try:
            if dynamic_element:
                return element_locator
            else:
                return WebDriverWait(self.driver, timeout).until(
                    any_element_with_locators_is_visible(element_locator, multiple_elements)
                )
        except TimeoutException:
            raise ElementNotFoundException(f"Element(s) '{element_locator}' not found")


    def get_dynamic_element(self, element, *dynamic_value, timeout:int = 0, multiple_elements:bool = False) -> WebElement:
        by_type, locator = element
        locator = locator.format(*dynamic_value)

        return self.get_element((by_type, locator), timeout, multiple_elements)

    def is_element_present(self, element, *values, timeout:int = 1):

        try:
            if not values:
                return element.is_displayed()
            else:
                self.get_dynamic_element(element, *values, timeout=timeout, multiple_elements=False)
            return True
        except ElementNotFoundException:
            return False

    def get_driver(self):
        return self.driver

    def close_driver(self):
        return self.driver.quit()