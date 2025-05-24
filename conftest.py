import os
import pytest

from datetime import datetime
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser option selection")


@pytest.fixture(scope="class")
def driver_instance(request):
    browser_name = request.config.getoption("browser")

    if browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--incognito")
        driver = webdriver.Chrome(options=chrome_options)

    elif browser_name == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument("--private")
        driver = webdriver.Firefox(options=firefox_options)

    else:
        raise ValueError(f"Unsupported browser name: {browser_name}")

    driver.maximize_window()
    driver.implicitly_wait(5)
    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()


# Define the directory to store screenshots
SCREENSHOT_DIR = r"D:\PythonLearning2025\Reports\screenshots"


# Ensure the directory exists
if not os.path.exists(SCREENSHOT_DIR):
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)


@pytest.hookimpl(hookwrapper=True)
def test_execution_reporter(item):
    """
    Extends the PyTest Plugin to take and embed a screenshot in the HTML report whenever a test fails.
    :param item: The test case item.
    """
    pytest_html = item.config.pluginmanager.getplugin('html')  # Get pytest-html plugin
    outcome = yield  # Execute the test and collect its outcome
    report = outcome.get_result()   # Get the test report
    extra = getattr(report, 'extra', [])  # Extract additional report information

    # Capture screenshot on test failure or setup failure
    if report.when == 'call' or report.when == "setup":
        # Check if the test was expected to fail (xfail)
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # Construct the screenshot file path inside the designated folder
            test_name = report.nodeid.split("::")[-1].replace("/", "_").replace("\\", "_").replace(":", "_")
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            file_name = os.path.join(SCREENSHOT_DIR, f"{timestamp}_{test_name}.png")
            # print("Screenshot saved at: " + file_name)
            driver = item.funcargs.get('driver_instance')
            # Capture and save the screenshot
            _capture_screenshot(driver, file_name)
            if os.path.exists(file_name):  # Ensure the file exists before referencing it
                # Use relative path for HTML embedding
                relative_path = os.path.relpath(file_name, os.getcwd())
                html = (
                    f'<div><img src="{relative_path}" alt="screenshot" '
                    f'style="width:304px;height:228px;" '
                    f'onclick="window.open(this.src)" align="right"/></div>'
                )
                extra.append(pytest_html.extras.html(html))
        report.extras = extra


def _capture_screenshot(driver, file_name):
    """
    Captures a screenshot using the WebDriver instance and saves it to the specified file path.
    :param file_name: The full path where the screenshot will be saved.
    """
    # Save the screenshot using Selenium WebDriver
    driver.get_screenshot_as_file(file_name)
