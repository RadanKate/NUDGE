import pytest
from Pages.Login_page import LoginPage
from envparse import env
from selenium import webdriver

env.read_envfile()
tenant = env("TENANT")
username = env("USER_NAME")
password = env("PASSWORD")
saucelabs_remote = env("REMOTE")
saucelabs_username = env("SAUCELABS_USER_NAME")
saucelabs_password = env("SAUCELABS_PASSWORD")


# login once before all the tests, using credentials from .env file
@pytest.fixture
def login(driver):
    return LoginPage(driver, tenant, username, password)


@pytest.fixture
def driver():
    if saucelabs_remote == "True":
        SAUCELABS_URL = 'https://' + saucelabs_username + ':' + saucelabs_password + '@ondemand.saucelabs.com:443/wd/hub'
        desktop_browsers = {
            "platform": "OS X 10.14",
            "browserName": "chrome",
            "version": "latest",
            "sauce:options": {
                "extendedDebugging": True

            }
        }
        driver = webdriver.Remote(command_executor=SAUCELABS_URL, desired_capabilities=desktop_browsers)
    else:
        driver = webdriver.Chrome()
    yield driver
    driver.quit() \
 \
    @ pytest.fixture


def dashboard(login):
    return login.login()
