import pytest
from Pages.Login_page import LoginPage
from envparse import env
from appium import webdriver as appium_webdriver

env.read_envfile()
tenant = env("TENANT")
username = env("USER_NAME")
password = env("PASSWORD")
device_ID = env("DEVICE_ID")


# login once before all the tests, using credentials from .env file
@pytest.fixture
def login(driver):
    return LoginPage(driver, tenant, username, password)


ios_caps = [{
    'platformName': 'iOS',
    'platformVersion': '13.6.1',
    'deviceName': 'iPad',
    'udid': device_ID,
    'browserName': 'safari',
    'automationName': 'XCUITest',
    'deviceOrientation': 'portrait',
    'privateDevicesOnly': False,
    'phoneOnly': True,
    'acceptSslCerts': True,
    'appiumVersion': '1.17.0',
    'additionalWebviewBundleIds': ['process-SafariViewService'],
    "xcodeOrgId": "AUCWMQ5DFY",
    "xcodeSigningId": "iPhone Developer"
}]


@pytest.fixture(params=ios_caps)
def driver(request):
    caps = request.param
    test_name = request.node.name
    caps['name'] = test_name

    driver = appium_webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=caps)
    yield driver

    driver.quit()


@pytest.fixture
def dashboard(login):
    return login.login()
