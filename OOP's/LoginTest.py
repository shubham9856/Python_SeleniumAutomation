# Login test cases without using pytest

from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginTest:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def loginpagetest(self):
        driver = webdriver.Chrome()
        driver.get("https://practicetestautomation.com/practice-test-login/")

        try:
            username_field = driver.find_element(By.ID, 'username')
            password_field = driver.find_element(By.ID, 'password')
            submit_btn = driver.find_element(By.ID, 'submit')

            username_field.send_keys(self.username)
            password_field.send_keys(self.password)
            submit_btn.click()

            # Check for login result
            try:
                error_message = driver.find_element(By.ID, "error").text
                print(f"Login failed: {error_message}")
            except:
                success_header = driver.find_element(By.TAG_NAME, "h1").text
                print(f"Login success: {success_header}")

        except Exception as e:
            print(f"Test encountered an error: {e}")
        finally:
            driver.quit()


# Run both test scenarios
print("Running test with invalid credentials...")
obj = LoginTest("login", "pass")
obj.loginpagetest()

print("\nRunning test with valid credentials...")
obj1 = LoginTest("student", "Password123")
obj1.loginpagetest()
