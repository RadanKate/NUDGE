from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:

    def __init__(self, driver: WebDriver, tenant: str):
        self.driver: WebDriver = driver
        self.tenant = tenant
        # self.wait =

    def navigate_to(self, url: str):
        self.driver.get(self.tenant + url)
