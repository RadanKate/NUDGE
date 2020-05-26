import pytest
from Pages.Login_page import LoginPage
from envparse import env
from appium import webdriver as appium_webdriver

env.read_envfile()
tenant = env("TENANT")
username = env("USER_NAME")
password = env("PASSWORD")
device_ID = env("device_ID")


# login once before all the tests, using credentials from .env file
@pytest.fixture
def login(driver):
    return LoginPage(driver, tenant, username, password)


android_caps = [{
    'platformName': 'Android',
    'deviceIds': device_ID,
    "platformVersion": '9',
    'deviceName': 'Galaxy_S8',
    'browserName': 'chrome',
    'deviceOrientation': 'portrait',
    'privateDevicesOnly': False,
    'phoneOnly': True,
    'acceptSslCerts': True,
    'appiumVersion': '1.17.0',
    'additionalWebviewBundleIds': ['process-ChromeViewService'],
    'chromeInitialUrl': tenant
}]


@pytest.fixture(params=android_caps)
def driver(request):
    caps = request.param
    test_name = request.node.name
    caps['name'] = test_name

    driver = appium_webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_capabilities=caps)
    yield driver

    driver.quit()


@pytest.fixture
def dashboard(login):
    return login.login()
