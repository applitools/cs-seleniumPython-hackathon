import os
import pytest

from selenium import webdriver
from applitools.selenium import Eyes, Target, BatchInfo, ClassicRunner
from webdriver_manager.chrome import ChromeDriverManager

errorLocator = ".alert.alert-warning"


@pytest.fixture(scope="module")
def batch_info():
    """
    Use one BatchInfo for all tests inside module
    """
    return BatchInfo("Visual AI Suite")


@pytest.fixture(name="driver", scope="function")
def driver_setup(params):
    """
    New browser instance per test and quite.
    """
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(params['url'])
    yield driver
    # Close the browser.
    driver.quit()


@pytest.fixture(name="runner", scope="session")
def runner_setup():
    """
    One test runner for all tests. Print test results in the end of execution.
    """
    runner = ClassicRunner()
    yield runner
    all_test_results = runner.get_all_test_results(False)
    print(all_test_results)


@pytest.fixture(name="eyes", scope="function")
def eyes_setup(runner, batch_info, request, driver):
    """
    Basic Eyes setup. It'll abort test if wasn't closed properly.
    """
    eyes = Eyes(runner)
    # Initialize the eyes SDK and set your private API key.
    eyes.api_key = os.environ["APPLITOOLS_API_KEY"]
    eyes.configure.batch = batch_info

    eyes.open(driver, "Hackathon", request.node.name, {"width": 800, "height": 600})
    yield eyes
    try:
        # End the test
        eyes.close(False)
    finally:
        # If the test was aborted before eyes.close was called, ends the test as aborted.
        eyes.abort()


def test_ui_elements(eyes, driver):
    # Visual checkpoint



def submit_form(driver):
    driver.find_element_by_css_selector("#log-in").click()


# Both Username and Password must be present
def test_username_and_password_must_present(eyes, driver):
    submit_form(driver)

    # Visual checkpoint



# Password must be present
def test_username_must_present(eyes, driver):
    driver.find_element_by_css_selector("#username").send_keys("MyUserName")
    submit_form(driver)

    # Visual checkpoint



# Username must be present
def test_password_must_present(eyes, driver):
    driver.find_element_by_css_selector("#password").send_keys("MyPassword")
    submit_form(driver)

    # Visual checkpoint




# Successful login
def test_successful_login(eyes, driver):
    driver.find_element_by_css_selector("#username").send_keys("MyUserName")
    driver.find_element_by_css_selector("#password").send_keys("MyPassword")
    submit_form(driver)

    # Visual checkpoint #1.







