import pytest
from Pages.Login_page import LoginPage
# from Pages.Dashboard_page import DashboardPage
from envparse import env
from selenium import webdriver

# login once before all the tests, using credentials from .env file
env.read_envfile()
tenant = env("TENANT")
username = env("USER_NAME")
password = env("PASSWORD")
saucelabs_remote = env("REMOTE")
saucelabs_username = env("SAUCELABS_USER_NAME")
saucelabs_password = env("SAUCELABS_PASSWORD")


@pytest.fixture
def login(driver):
    return LoginPage(driver, tenant, username, password)


@pytest.fixture
def driver():
    if saucelabs_remote == "True":
        SAUCELABS_URL = 'https://' + saucelabs_username + ':' + saucelabs_password + '@ondemand.saucelabs.com:443/wd/hub'
        desired_cap = {

            'os': 'OS X',
            'os_version': 'Catalina',
            'browser': 'Chrome',
            'browser_version': '81',
            'name': "First Test"

        }
        driver = webdriver.Remote(command_executor=SAUCELABS_URL, desired_capabilities=desired_cap)
    else:
        driver = webdriver.Chrome()
    yield driver
    driver.quit()

# @pytest.fixture
# def dashboard(driver):
#     return DashboardPage(driver)
