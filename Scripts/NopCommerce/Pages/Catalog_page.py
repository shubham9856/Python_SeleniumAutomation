from collections import namedtuple

from Utilities.BrowserUtilities import BrowserUtilities


class CatalogPage(BrowserUtilities):
    def __init__(self, driver):
        super().__init__(self)
        self.driver = driver

    # Written locators for computer order end to end flow
    lc_menu_sub_options = namedtuple('lc_menu_sub_options', ['xpath', 'loc_type'])(
        '//ul[@class="sublist first-level"]//a[@href and text()="{}"]', 'xpath')

    lc_computer_card_add_cart_btn = namedtuple('lc_computer_card_add_cart_btn', ['xpath', 'loc_type'])(
        '(//div[@class="item-box"]//button[text()="Add to cart"])[1]', 'xpath')
