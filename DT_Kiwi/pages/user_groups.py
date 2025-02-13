from DT_Kiwi.utils.playwright_driver import PlaywrightDriver


class UserGroupPage:
    def __init__(self, driver: PlaywrightDriver):
        self.driver = driver
        self.networkusers_icon = '//div[@id="Network Users"]' # network users icon
        self.click_user_group="#user-groups"
        self.dashboard_user_groups = '//h2[contains(text(),"User Groups")]'
        self.user_search = '//input[@placeholder="Search"]'
        self.main_search="#navbar-org-select"
        self.user_group_name_td = "//div[contains(text(),'Name')]"
        self.user_groups_des_td = "//th//div[contains(text(),'Description')]"
        self.user_groups_users_td = "//th//div[contains(text(),'Total Users')]"
        self.user_groups_created_td = "//th//div[contains(text(),'Created At')]"

    def navigate_to_user_groups(self):
            self.driver.click_element(self.networkusers_icon)
            self.driver.click_element(self.click_user_group)
            # Validate that the User Groups dashboard is visible
            if not self.driver.is_element_visible(self.dashboard_user_groups):
                raise Exception("failed. Dashboard text not visible.")

    def verify_user_groups_elements(self) -> bool:
        """Verifies that all key elements are present on the User Groups dashboard."""
        elements = [
            self.dashboard_user_groups,  # Dashboard header
            self.user_search,  # Search input
            self.user_group_name_td,  # Name column
            self.user_groups_des_td,  # Description column
            self.user_groups_users_td,  # Total Users column
            self.user_groups_created_td  # Created At column
        ]

        return all(self.driver.is_element_visible(element) for element in elements)



