import time
import pytest

from datetime import datetime, timedelta
from Scripts.RedBus.Pages.BusResultPage import BusResultPage
from Scripts.RedBus.Pages.RedBusPage import RedBusPage

"""
Usage:
pytest -s -v Scripts/RedBus/Tests/SearchRedbusTrip_test.py --browser=chrome 
"""


@pytest.mark.usefixtures("driver_instance")
class TestRedBusHomepage:
    booking_date = (datetime.now() + timedelta(days=1)).day

    def test_select_root(self):
        red_bus = RedBusPage(self.driver)
        bus_result = BusResultPage(self.driver)

        red_bus.getUrl("https://www.redbus.in/new")

        red_bus_logo = red_bus.waitForElement(red_bus.lc_red_bus_logo)
        assert red_bus_logo, "site logo is displayed"

        time.sleep(2)

        input_from_txt = red_bus.findElement(red_bus.lc_src_input_txt)
        assert input_from_txt, "Input text box is present"
        input_from_txt.send_keys("Pune")

        to_input_text = red_bus.findElement(red_bus.lc_dest_input_txt)
        assert to_input_text, "Input destination to is present"
        to_input_text.send_keys("Kolhapur")

        select_date_options = red_bus.findElement(red_bus.lc_calender_popup)
        assert select_date_options, "calender pop up is displayed"
        red_bus.element_click(select_date_options)

        """here the replace method uses one argument which is locator in the names-tuple"""
        desired_date = red_bus.waitForElement(red_bus.lc_select_calender_date._replace(
            locator=red_bus.lc_select_calender_date.locator.format(self.booking_date)))
        assert desired_date, "Date selections are present"
        # Click on the desired date
        red_bus.element_click(desired_date)

        # Click on search button
        search_button = red_bus.findElement(red_bus.lc_search_btn)
        assert search_button, "Search button is present"
        red_bus.element_click(search_button)

        bus_results = bus_result.wait_for_visible(bus_result.lc_bus_results)
        assert bus_results, "Bus results are displayed successfully"

        time.sleep(2)
        print("Test Execution Completed.....")
