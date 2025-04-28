# This class stores the common methods of framework
class BrowserUtilities:
    # when object is created the driver is passed to the instance
    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title
