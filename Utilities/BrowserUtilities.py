# This class stores the common methods of framework
import os
from datetime import datetime
from typing import NamedTuple

from selenium.common.exceptions import NoSuchElementException, ElementNotSelectableException, ElementNotVisibleException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait


class BrowserUtilities:
    # when object is created the driver is passed to the instance
    def __init__(self, driver):
        self.driver = driver

    def getTitle(self):
        return self.driver.title

    def getUrl(self, url):
        return self.driver.get(url)

    def findElementList(self, locator: NamedTuple):
        """
        :param locator: accepts locator name-tuple
        :return: returns the web-element
        """
        try:
            element = self.driver.find_elements(locator[1], locator[0])
            return element
        except:
            return None

    def findElement(self, locator: NamedTuple):
        """
        :param locator: accepts locator name-tuple
        :return: returns the web-element
        """
        try:
            element = self.driver.find_element(locator[1], locator[0])
            return element
        except:
            return None

    def isElementDisplayed(self, locator: NamedTuple):
        """
        :param locator: accepts locator name-tuple
        :return: returns the web-element
        """
        try:
            element = self.driver.find_element(locator[1], locator[0])
            if element:
                is_displayed = element.is_displayed()
                return is_displayed  # returns boolean value
        except:
            self.screenShot(f"Element is present -{locator}")
            # return None

    def waitForElement(self, locator: NamedTuple, timeout=30, poll_frequency=3):
        try:
            loc_type = locator[1]
            element = locator[0]
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((loc_type, element)))
            return element
        except:
            self.screenShot(f"Element not present- {locator}")
            return

    def wait_for_visible(self, locator: NamedTuple, timeout=30, poll_frequency=3):
        try:
            loc_type = locator[1]
            element = locator[0]
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.visibility_of_element_located((loc_type, element)))
            return element
        except:
            self.screenShot(f"Element not located-{locator}")
            return

    def element_click(self, element):
        try:
            element.click()
        except:
            print("Element is not clickable")
            return
    def mouse_hover(self, element: WebElement):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def screenShot(self, result_message):
        """
        Takes screenshot of the current open web page
        """
        file_name = f'{datetime.now().strftime("%y%m%d-%H%M%S")}-{result_message}.png'
        screenshot_directory = "../Reports/screenshots/"
        relative_file_name = f'{screenshot_directory}{file_name}'
        current_directory = os.path.dirname(__file__)
        destination_file = os.path.join(current_directory, relative_file_name)
        destination_directory = os.path.join(current_directory, screenshot_directory)

        if not os.path.exists(destination_directory):
            os.makedirs(destination_directory)
            self.driver.save_screenshot(destination_file)
            print("Screenshot taken")
