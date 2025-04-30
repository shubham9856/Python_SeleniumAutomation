import pytest

from Scripts.NopCommerce.Pages.Homepage import Homepage


@pytest.mark.usefixtures("driver_instance")
class TestHomePageContent:
    def test_top_nav_content(self):
        home_page = Homepage(self.driver)

        home_page.getUrl("https://demo.nopcommerce.com/")

        hero_image = home_page.isElementDisplayed(home_page.lc_hero_image)
        assert hero_image, "Hero Image is present on homepage"

        print(f"Homepage Title: '{home_page.getTitle()}'")
        for item in home_page.top_nav_elements:
            menu_item = home_page.findElement(home_page.lc_top_menu_items._replace(
                xpath=home_page.lc_top_menu_items.xpath.format(item)))
            assert menu_item.text == item.strip(), f"Top navigation option is present-{item}"

        search_box = home_page.isElementDisplayed(home_page.lc_top_search_box)
        assert search_box, "Top nav search section is present"


