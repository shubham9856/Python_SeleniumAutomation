from selenium.webdriver.common.by import By

from Utilities.BrowserUtilities import BrowserUtilities


class Homepage(BrowserUtilities):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    lc_top_menu_items = (By.XPATH, "//ul[@class='top-menu notmobile']/li")