from Base_page import BasePage


class DashboardPage(BasePage):

    def is_inside_dashboard_page(self) -> bool:
        return self.is_element_displayed("[data-test='tab-live-dashboard']") and \
               self.is_element_displayed("[data-test='tab-visit-reports']") and \
               self.is_element_displayed("[data-test='tab-reports']") and \
               self.is_element_displayed("[data-test='tab-client-intake']") and \
               self.is_element_displayed("[data-test='tab-data-exploration']") and \
               self.is_element_displayed("[data-test='tab-telehealth-dashboard']") and \
               self.is_element_displayed("[data-test=tab-tasks']")
