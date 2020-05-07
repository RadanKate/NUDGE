import pytest
from Pages.Login_page import LoginPage
from envparse import env
# from selenium import webdriver
from appium import webdriver

env.read_envfile()
tenant = env("TENANT")
username = env("USER_NAME")
password = env("PASSWORD")
saucelabs_remote = env("REMOTE")
saucelabs_username = env("SAUCELABS_USER_NAME")
saucelabs_password = env("SAUCELABS_PASSWORD")


# saucelabs_api_key = env("API_KEY")


# login once before all the tests, using credentials from .env file
@pytest.fixture
def login(driver):
    return LoginPage(driver, tenant, username, password)


@pytest.fixture
def driver():
    if saucelabs_remote == "True":
        desired_cap = {
            "deviceName": "iPhone XR",
            "deviceIds": "iPhone_XR_free",
            "browserName": "Safari",
            "deviceOrientation": "portrait",
            "platformVersion": "13.3",
            "platformName": "iOS",
            "testobject_api_key": 'D4567FC495EE4E4CA94E24589D75BC5C'
        }
        SAUCELABS_URL = 'https://' + saucelabs_username + ':' + saucelabs_password + '@ondemand.saucelabs.com:443/wd/hub'
        driver = webdriver.Remote(command_executor=SAUCELABS_URL, desired_capabilities=desired_cap)
    else:
        desired_cap = {
            "browserName": "Chrome",
            "version": "*",
            "goog:chromeOptions": {
                "mobileEmulation": {
                    "deviceMetrics": {
                        "width": 360,
                        "height": 640,
                        "pixelRatio": 3
                    },
                    "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile/14E5239e Safari/602.1"}
            }
        }
        driver = webdriver.Chrome(desired_capabilities=desired_cap)
    yield driver
    driver.quit()


@pytest.fixture
def dashboard(login):
    return login.login()
