from DT_Kiwi.utils.playwright_driver import PlaywrightDriver


class NetworkUserPage:
    def __init__(self, driver: PlaywrightDriver):
        self.driver = driver
        self.networkusers_icon = '//div[@id="Network Users"]'
        self.org_navigation = '//li[@id="organizations"]'
        self.org_user_groups='//li[@id="user-groups"]'
        self.org_userManagement='//li[@id="user-mgmt"]'
        self.org_header_txt = '//h2[contains(text(),"Organizations")]'
        self.org_add = '//img[@alt="add"]'
        self.add_enterprise_org = '//h5[contains(text(),"Enterprise Organization")]'
        self.input_enterprise_org = '//input[@id="add-org-name"]'
        self.input_description_org = '//input[@id="add-org-description"]'
        self.org_submit_btn = '//button[@id="add-org-submit-button"]'
        self.name_require_txt = '//p[@id="add-org-name-helper-text" and contains(text(), "Name is required")]'
        self.error_message_org_txt = '//div[@id="notistack-snackbar" and text()="Error while creating organization!"]'
        self.create_org_success_message_txt = '//div[@id="notistack-snackbar" and contains(text(), "Organization is created successfully!")]'
        self.description_require_txt = '//p[contains(text(),"Description is required")]'
        self.username_field = '//input[@id="username"]'
        self.continue_btn = '//button[contains(text(),"Continue")]'
        self.password_field = '//input[@id="password"]'
        self.dashboard_text = '//h2[contains(text(),"Network Admin")]'
        self.confirm_delete_btn = "//button[@id='delete-org-button']"
        self.confirm_del_pop = "//button[contains(text(),'Delete')]"
        self.network_users_icon = '//div[@aria-label="Network Users"]'
        # self.search_btn = '//input[@id=":r101:"]'
        self.search_btn = '//input[@placeholder="Search"]'
        self.select_btn = '//span[normalize-space()="Cognitivzen"]'
        self.logout_dropdown = '//img[@alt="Arrow Dropdown"]'
        self.logout_user = '//li[text()="Log Out"]'

    def navigate(self, url: str):
        """Navigate to the login page."""
        self.driver.navigate_to(url)

    def login(self, username: str, password: str):
        """Perform login action."""
        self.driver.fill_textbox(self.username_field, username)
        self.driver.click_element(self.continue_btn)
        self.driver.fill_textbox(self.password_field, password)
        self.driver.click_element(self.continue_btn)
        if not self.driver.is_element_visible(self.dashboard_text):
            raise Exception("Login failed. Dashboard text not visible.")

    def login_successful(self) -> bool:
        """Check if login was successful (e.g., based on a dashboard element)."""
        return self.driver.is_element_visible(self.dashboard_text)

    def navigate_to_network_users(self):
        """Navigate to Network Users page and validate the options."""
        self.driver.click_element(self.network_users_icon)
        if not self.driver.is_element_visible('//h2[contains(text(),"Network Users")]'):
            raise Exception("Navigation to Network Users failed.")

        # Validate visibility of the options after navigating to Network Users
        if not self.driver.is_element_visible(self.org_userManagement):
            raise Exception("User Management option is not visible.")
        if not self.driver.is_element_visible(self.org_user_groups):
            raise Exception("User Groups option is not visible.")
        if not self.driver.is_element_visible(self.org_navigation):
            raise Exception("Organizations option is not visible.")


