from Base_page import BasePage


class DashboardPage(BasePage):

    def wait_until_loaded(self):
        self.is_element_displayed(".dashboard-grid", timeout=30)

    def is_dashboard_page_displayed_correctly(self) -> bool:
        return self.is_element_displayed("[data-test='tab-live-dashboard']") and \
               self.is_element_displayed("[data-test='tab-visit-reports']") and \
               self.is_element_displayed("[data-test='tab-reports']") and \
               self.is_element_displayed("[data-test='tab-client-intake']") and \
               self.is_element_displayed("[data-test='tab-data-exploration']") and \
               self.is_element_displayed("[data-test='tab-telehealth-dashboard']") and \
               self.is_element_displayed("[data-test='tab-tasks']")
