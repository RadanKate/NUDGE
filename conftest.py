import pytest
from selenium.common.exceptions import WebDriverException

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
saucelabs_api_key = env("API_KEY")


# login once before all the tests, using credentials from .env file
@pytest.fixture
def login(driver):
    return LoginPage(driver, tenant, username, password)


######################################
import pytest
import os
import requests
import json
import re


def pytest_addoption(parser):
    parser.addoption("--dc", action="store", default='us', help="Set Sauce Labs Data Center (US or EU)")


@pytest.fixture
def data_center(request):
    return request.config.getoption('--dc')


ios_caps = [{
    'platformName': 'iOS',
    'deviceOrientation': 'portrait',
    'privateDevicesOnly': False,
    'phoneOnly': True
}]


@pytest.fixture(params=ios_caps)
def ios_driver(request, data_center):
    caps = request.param

    saucelabs_api_key = os.environ['TESTOBJECT_SAMPLE_IOS']
    caps['testobject_api_key'] = saucelabs_api_key
    test_name = request.node.name
    caps['name'] = test_name

    if data_center and data_center.lower() == 'eu':
        sauce_url = "https://appium.testobject.com/wd/hub"
    else:
        sauce_url = "https://us1.appium.testobject.com/wd/hub"

    driver = webdriver.Remote(sauce_url, desired_capabilities=caps)

    # This is specifically for SauceLabs plugin.
    # In case test fails after selenium session creation having this here will help track it down.
    # creates one file per test non ideal but xdist is awful
    if driver:
        print("SauceOnDemandSessionID={} job-name={}\n".format(driver.session_id, test_name))
    else:
        raise WebDriverException("Never created!")

    yield driver

    driver.quit()


######################################
# @pytest.fixture
# def driver():
#     if saucelabs_remote == "True":
#         desired_cap = {
#         'platformName':     'iOS',
#         'deviceOrientation':'portrait',
#         'privateDevicesOnly': False,
#         'phoneOnly': True
# }
#         SAUCELABS_URL = 'https://' + saucelabs_username + ':' + saucelabs_password + '@ondemand.saucelabs.com:443/wd/hub'
#         driver = webdriver.Remote(command_executor=SAUCELABS_URL, desired_capabilities=desired_cap)
#     else:
#         desired_cap = {
#             "browserName": "Chrome",
#             "version": "*",
#             "goog:chromeOptions": {
#                 "mobileEmulation": {
#                     "deviceMetrics": {
#                         "width": 360,
#                         "height": 640,
#                         "pixelRatio": 3
#                     },
#                     "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile/14E5239e Safari/602.1"}
#             }
#         }
#         driver = webdriver.Chrome(desired_capabilities=desired_cap)
#     yield driver
#     driver.quit()


@pytest.fixture
def dashboard(login):
    return login.login()
