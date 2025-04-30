# This class stores the common methods of framework
from typing import NamedTuple


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
            return None
