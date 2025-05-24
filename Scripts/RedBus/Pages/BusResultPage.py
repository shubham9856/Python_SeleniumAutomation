from collections import namedtuple

from Utilities.BrowserUtilities import BrowserUtilities


class BusResultPage(BrowserUtilities):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    lc_bus_results = namedtuple('lc_bus_result', ['locator', 'loc_type'])(
        '//div[@id="result-section"]//ul[@class="bus-items"]//li[@class="row-sec clearfix"]', 'xpath')
