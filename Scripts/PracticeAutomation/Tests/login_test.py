import pytest
import json
import time

from Scripts.PracticeAutomation.Pages.LoginPage import LoginPage


@pytest.mark.usefixtures("driver_instance")
class TestLoginPage:
    data_path = "D:/PythonLearning2025/MockData/LoginData.json"

    with open(data_path) as f:
        test_data = json.load(f)  # Loads json data
        test_data_list = test_data["Users"]  # Returns the Users list (list of user dictionaries)

    @pytest.mark.parametrize("test_data_items", test_data_list)
    def test_valid_login(self, test_data_items):
        self.driver.get("https://practicetestautomation.com/practice-test-login/")

        # Created LoginPage object to use BrowserUtilities methods via page object
        login_page_obj = LoginPage(self.driver)

        print("Page Url Title: ", login_page_obj.getTitle())

        login_header = self.driver.find_element(*login_page_obj.lc_login_header)
        assert "Test login" == login_header.text

        username_field = self.driver.find_element(*login_page_obj.lc_username_input)
        username_field.send_keys(test_data_items["Username"])

        password_field = self.driver.find_element(*login_page_obj.lc_password_input)
        password_field.send_keys(test_data_items["Password"])

        submit_btn = self.driver.find_element(*login_page_obj.lc_submit_btn)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
        submit_btn.click()
        time.sleep(2)

        login_success_msg = self.driver.find_element(*login_page_obj.lc_login_successful_msg)
        assert login_success_msg.text == "Logged In Successfully", "Check User is logged in"
