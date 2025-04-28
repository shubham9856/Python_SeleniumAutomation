import pytest

from Scripts.NopCommerce.Pages.Homepage import Homepage


@pytest.mark.usefixtures("driver_instance")
class TestHomePageContent:

    def test_top_nav_content(self):
        driver = self.driver
        home_page = Homepage(self.driver)

        driver.get("https://demo.nopcommerce.com/")

        print("Homepage Title :\n", home_page.get_title())

        menu_items = driver.find_elements(*home_page.lc_top_menu_items)
        for item in menu_items:
            print(item.text)
