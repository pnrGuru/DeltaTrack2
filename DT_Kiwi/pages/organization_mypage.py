from DT_Kiwi.utils.playwright_driver import PlaywrightDriver


class OrganizationnPage:
    def __init__(self, driver: PlaywrightDriver):
        self.driver = driver
        self.networkusers_icon = '//img[@src="/assets/images/icons/Setup-Icon.svg"]'
        self.org_navigation = '//li[@id="organizations"]'
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

    def verify_uielements(self) -> bool:
        """Checks Organization Lading page navigation successful."""
        return self.driver.is_element_visible(self.org_header_txt)

    def navigate_to_organization(self):
        self.driver.click_element(self.networkusers_icon)
        self.driver.click_element(self.org_navigation)
        # adding organization
        self.driver.click_element(self.org_add)
        # clicks Enterprise Organization
        self.driver.click_element(self.add_enterprise_org)

    def add_organization(self, name: str, description: str):
        # self.driver.click_element(self.org_add)
        # self.driver.click_element(self.add_enterprise_org)
        self.driver.clear_textbox(self.input_enterprise_org)
        self.driver.fill_textbox(self.input_enterprise_org, name)
        self.driver.fill_textbox(self.input_description_org, description)
        self.driver.click_element(self.org_submit_btn)

    def create_org(self, name: str, description: str):
        self.driver.click_element(self.org_add)
        self.driver.click_element(self.add_enterprise_org)
        self.driver.clear_textbox(self.input_enterprise_org)
        self.driver.fill_textbox(self.input_enterprise_org, name)
        self.driver.fill_textbox(self.input_description_org, description)
        self.driver.click_element(self.org_submit_btn)

    def get_name_required_error(self) -> bool:
        return self.driver.is_element_visible(self.name_require_txt)

    def get_error_message_org(self) -> bool:
        return self.driver.is_element_visible(self.error_message_org_txt)

    # def create_org_success_message(self) -> bool:
    #     return self.driver.is_element_visible(self.create_org_success_message_txt)

    def create_org_success_message(self) -> bool:
        """Validates if the success message is displayed after creating an organization."""
        return self.driver.is_element_visible(self.create_org_success_message_txt)

    def delete_organization(self, org_name: str):
        """
        Delete an organization and validate its deletion.

        :param org_name: Name of the organization to delete.
        """
        self.driver.fill_textbox(self.search_btn, org_name)
        self.driver.click_element(self.select_btn)
        self.driver.click_element(self.confirm_delete_btn)
        self.driver.click_element(self.confirm_del_pop)

    def user_logout(self):
        """
        User logout the application.

        :param org_name: User logout application.
        """
        self.driver.click_element(self.logout_dropdown)
        self.driver.click_element(self.logout_user)

