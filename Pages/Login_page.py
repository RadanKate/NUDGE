import time
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from Base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver: WebDriver, tenant: str, username: str, password: str):
        self.username: str = username
        self.password: str = password
        super().__init__(driver, tenant)

    def visit(self):
        super().navigate_to("")

    def login(self):
        self.visit()
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".loginEmail")))
        self.driver.find_element_by_css_selector(".loginEmail").send_keys(self.username)
        self.driver.find_element_by_css_selector(".loginPassword").send_keys(self.password)
        time.sleep(1)
        self.driver.find_element_by_css_selector("[type='submit']").click()
        time.sleep(1)

    def is_login_error_displayed(self) -> bool:
        try:
            popup_error: WebElement = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".modal-dialog")))
            if not popup_error.is_displayed():
                return False
            if not self.driver.find_element_by_css_selector(".modal-title").text == "Error":
                return False
            if not self.driver.find_element_by_css_selector(".modal-body").text == "Email or password is incorrect.":
                return False
            return True
        except:
            return False
