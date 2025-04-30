import time

import pytest

from Scripts.NopCommerce.Pages.Catalog_page import CatalogPage
from Scripts.NopCommerce.Pages.Homepage import Homepage


@pytest.mark.usefixtures("driver_instance")
class TestComputerOrder:
    # def classSetup(self):
    #     self.home_page = Homepage(self.driver)
    #     self.catalog_page = CatalogPage(self.driver)

    def test_computer_search(self):
        home_page = Homepage(self.driver)
        catalog_page = CatalogPage(self.driver)

        home_page.getUrl("https://demo.nopcommerce.com/")

        # Select computer from top nav
        computers_menu_opt = home_page.waitForElement(home_page.lc_top_menu_items._replace(
            xpath=home_page.lc_top_menu_items.xpath.format("Computers ")))
        assert computers_menu_opt, "Top nav computers option is present"
        home_page.mouse_hover(computers_menu_opt)

        desktop_sub_opt = catalog_page.findElement(catalog_page.lc_menu_sub_options._replace(
            xpath=catalog_page.lc_menu_sub_options.xpath.format("Desktops ")))
        assert desktop_sub_opt, "Computers sub option is displayed"
        desktop_sub_opt.click()

        computer_card_add_cart_btn = catalog_page.findElement(catalog_page.lc_computer_card_add_cart_btn)
        assert computer_card_add_cart_btn, "computer cards are present on catalog page"
        computer_card_add_cart_btn.click()

    def test_computer_catalog(self):
        pass

    def test_computer_detail_page(self):
        pass

    def test_computer_cart_and_checkout(self):
        pass
