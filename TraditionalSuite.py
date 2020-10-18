import os
import pytest
from selenium import webdriver
from applitools.selenium import Eyes, Target, ClassicRunner
from webdriver_manager.chrome import ChromeDriverManager

original_test_url = "https://demo.applitools.com/hackathon.html"
new_test_url = "https://demo.applitools.com/hackathonV2.html"
errorLocator = ".alert.alert-warning"


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


def test_validate_labels(driver):
    # Assert Text of Login Form
    assert "Login Form" == driver.find_element_by_css_selector(".auth-header").text

    # Assert Text of UserName Label
    assert "Username" == driver.find_element_by_css_selector("form > div:nth-child(1) > label").text

    # Assert Text of UserName Element
    assert "Enter your username" == driver.find_element_by_css_selector("#username").get_attribute("placeholder")

    # Assert Text of Password Label
    assert "Password" == driver.find_element_by_css_selector("form > div:nth-child(2) > label").text

    # Assert Text of Password Element
    assert "Enter your password" == driver.find_element_by_css_selector("#password").get_attribute("placeholder")

    # Assert Text of Login Element
    assert "Log In" == driver.find_element_by_css_selector("#log-in").text

    # Assert Text of Remember Me Element
    assert "Remember Me" == driver.find_element_by_css_selector(".form-check-label").text


def test_validate_images(driver):

    # Assert Logo Icon is Visible
    assert driver.find_element_by_css_selector(".logo-w>a>img").is_displayed()

    # Assert User Icon is Visible
    assert driver.find_element_by_css_selector(".pre-icon.os-icon.os-icon-user-male-circle").is_displayed()

    # Assert User Fingerprint is Visible
    assert driver.find_element_by_css_selector(".pre-icon.os-icon.os-icon-fingerprint").is_displayed()

    # Assert User Twitter is Visible
    assert driver.find_element_by_css_selector("a:nth-child(1) > img").is_displayed()

    # Assert User Facebook is Visible
    assert driver.find_element_by_css_selector("a:nth-child(2) > img").is_displayed()

    # Assert User Linkdin is Visible
    assert driver.find_element_by_css_selector("a:nth-child(3) > img").is_displayed()


def test_validate_checkbox(driver):

    # Assert Logo Icon is Visible
    assert not driver.find_element_by_css_selector(".form-check-input").is_selected()


def submit_form(driver):
    driver.find_element_by_css_selector("#log-in").click()


# Both Username and Password must be present
def test_username_and_passwrod_must_present(driver):
    submit_form(driver)
    assert driver.find_element_by_css_selector(errorLocator).is_displayed()
    assert driver.find_element_by_css_selector(errorLocator).text == "Both Username and Password must be present"


# Password must be present
def test_username_must_present(driver):
    driver.find_element_by_css_selector("#username").send_keys("MyUserName")
    submit_form(driver)
    assert driver.find_element_by_css_selector(errorLocator).is_displayed()
    assert driver.find_element_by_css_selector(errorLocator).text == "Password must be present"


# Username must be present
def test_password_must_present(driver):
    driver.find_element_by_css_selector("#password").send_keys("MyPassword")
    submit_form(driver)
    assert driver.find_element_by_css_selector(errorLocator).is_displayed()
    assert driver.find_element_by_css_selector(errorLocator).text == "Username must be present"


# Successful login
def test_successful_login(driver):
    driver.find_element_by_css_selector("#username").send_keys("MyUserName")
    driver.find_element_by_css_selector("#password").send_keys("MyPassword")
    submit_form(driver)
    assert driver.title=="ACME demo app"





