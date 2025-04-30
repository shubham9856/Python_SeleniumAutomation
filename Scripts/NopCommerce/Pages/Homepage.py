from collections import namedtuple
from Utilities.BrowserUtilities import BrowserUtilities


class Homepage(BrowserUtilities):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    lc_top_menu_items = namedtuple('lc_top_menu_items', ['xpath', 'loc_type'])(
        "//ul[@class='top-menu notmobile']//a[text()='{}']", "xpath")

    top_nav_elements = ["Computers ", "Electronics ", "Apparel ", "Digital downloads ", "Books ", "Jewelry ",
                        "Gift Cards "]

    lc_hero_image = namedtuple('lc_hero_image', ['xpath', 'loc_type'])('//div[@id="main"]//img[@class="slider-img"]',
                                                                       'xpath')
    lc_top_search_box = namedtuple('lc_top_search_box', ['xpath', 'loc_type'])('//form[@id="small-search-box-form"]',
                                                                               'xpath')
