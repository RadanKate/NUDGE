from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver: WebDriver, tenant: str):
        self.driver: WebDriver = driver
        self.tenant = tenant

    def navigate_to(self, url: str):
        self.driver.get(self.tenant + url)

    def is_element_displayed(self, css_locator, timeout=3) -> bool:
        try:
            element: WebElement = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, css_locator)))
            if not element.is_displayed():
                return False
            return True
        except:
            return False

    def get_element(self, css_locator, timeout=3) -> WebElement:
        if self.is_element_displayed(css_locator, timeout):
            return self.driver.find_element_by_css_selector(css_locator)
        else:
            raise Exception("Failed to find element " + css_locator)
