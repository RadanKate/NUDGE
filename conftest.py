import pytest
from selenium.common.exceptions import WebDriverException
from Pages.Login_page import LoginPage
from envparse import env
from appium import webdriver as appium_webdriver

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


def pytest_addoption(parser):
    parser.addoption("--dc", action="store", default='us', help="Set Sauce Labs Data Center (US or EU)")


@pytest.fixture
def data_center(request):
    return request.config.getoption('--dc')


ios_caps = [{
    'platformName': 'iOS',
    'deviceIds': 'iPhone_XR_free',
    "platformVersion": "13.3",
    'deviceOrientation': 'portrait',
    'privateDevicesOnly': False,
    'phoneOnly': True,
    'acceptSslCerts': True,
    'appiumVersion': '1.17.0',
    'additionalWebviewBundleIds': ['process-SafariViewService'],
    'safariInitialUrl': tenant
}]


@pytest.fixture(params=ios_caps)
def driver(request, data_center):
    caps = request.param

    caps['testobject_api_key'] = saucelabs_api_key
    test_name = request.node.name
    caps['name'] = test_name

    if data_center and data_center.lower() == 'eu':
        sauce_url = "https://appium.testobject.com/wd/hub"
    else:
        sauce_url = "https://us1.appium.testobject.com/wd/hub"

    driver = appium_webdriver.Remote(sauce_url, desired_capabilities=caps)

    # This is specifically for SauceLabs plugin.
    # In case test fails after selenium session creation having this here will help track it down.
    if driver:
        print("SauceOnDemandSessionID={} job-name={}\n".format(driver.session_id, test_name))
    else:
        raise WebDriverException("Never created!")
    yield driver

    driver.quit()


@pytest.fixture
def dashboard(login):
    return login.login()
