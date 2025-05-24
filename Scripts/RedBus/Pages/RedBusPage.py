from collections import namedtuple

from Utilities.BrowserUtilities import BrowserUtilities


class RedBusPage(BrowserUtilities):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    lc_red_bus_logo = namedtuple('lc_redbus_logo', ['locator', 'loc_type'])(
        '//div[@class="rb_header "]//img[contains(@src, "logo") and @title="redBus"]', 'xpath')

    lc_src_input_txt = namedtuple('lc_src_input_txt', ['locator', 'loc_type'])(
        '//div[@id="autoSuggestContainer"]//input[@id="src"]', 'xpath')

    lc_dest_input_txt = namedtuple('lc_dest_input_txt', ['locator', 'loc_type'])(
        '//div[@id="autoSuggestContainer"]//input[@id="dest"]', 'xpath')

    lc_calender_popup = namedtuple('lc_calender_popup', ['locator', 'loc_type'])(
        '//div[@id="onwardCal"]', 'xpath')

    lc_select_calender_date = namedtuple('lc_select_calender_date', ['locator', 'loc_type'])(
        '//div[@class="sc-jzJRlG hrJoeL"]//span[contains(@class, "DayTiles__CalendarDaysSpan") and text()="{}"]',
        'xpath')

    lc_search_btn = namedtuple('lc_search_btn', ['locator', 'xpath'])('//button[text()="SEARCH BUSES"]', 'xpath')
