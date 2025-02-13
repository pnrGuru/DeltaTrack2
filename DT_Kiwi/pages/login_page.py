import time

from DT_Kiwi.utils.playwright_driver import PlaywrightDriver


class LoginPage:
    def __init__(self, driver: PlaywrightDriver):
        self.driver = driver
        self.username_field = '//input[@id="username"]'
        self.continue_btn = '//button[contains(text(),"Continue")]'
        self.password_field = '//input[@id="password"]'
        self.dashboard_text = '//h2[contains(text(),"Network Admin")]'
        self.logout_button = "//li[contains(text(),'Log Out')]"  # Example logout button locator


    def navigate(self, url: str):
        """Navigate to the login page."""
        self.driver.navigate_to(url)

    def login(self, username: str, password: str):
        """Perform login action."""
        self.driver.fill_textbox(self.username_field, username)
        self.driver.click_element(self.continue_btn)
        self.driver.fill_textbox(self.password_field, password)
        self.driver.click_element(self.continue_btn)
        time.sleep(10)

        if not self.driver.is_element_visible(self.dashboard_text):
            raise Exception("Login failed. Dashboard text not visible.")

    def login_successful(self) -> bool:
        """Check if login was successful (e.g., based on a dashboard element)."""
        return self.driver.is_element_visible(self.dashboard_text)

    #def verify_uielements(self) -> bool:
       # """Checks Organization Lading page navigation successful."""
       # return self.driver.is_element_visible(self.org_header_txt)

    def create_organization(self, org_name: str, org_description: str):
        """Create an organization and validate its creation."""
        # Navigate to Organizations page
        self.driver.click_element(self.network_users_icon)

        # Click Add button and select Enterprise Organization
        self.driver.click_element(self.org_header_txt)

        self.driver.click_element(self.org_add)
        self.driver.click_element(self.add_enterprise_org)

        # Fill in organization details
        self.driver.fill_textbox(self.input_enterprise_org, org_name)
        self.driver.fill_textbox(self.input_description_org, org_description)
        self.driver.click_element(self.org_submit_btn)

        # Validate that the data is added in the table

        if not self.driver.is_element_visible(f"//table//td[text()='{org_name}']"):
            raise AssertionError(f"Organization name '{org_name}' not found in the table.")
        if not self.driver.is_element_visible(f"//table//td[text()='{org_description}']"):
            raise AssertionError(f"Organization description '{org_description}' not found in the table.")

    def delete_organization(self, org_name: str):
        """Delete an organization and validate its deletion."""
        # Navigate to Organizations page
        self.driver.click_element(self.network_users_icon)
        self.driver.click_element(self.org_header_txt)

        # Locate the organization in the table
        org_row_xpath = f"//table//td[text()='{org_name}']/.."


        if not self.driver.is_element_visible(org_row_xpath):
            raise AssertionError(f"Organization '{org_name}' not found in the table.")
        self.driver.click_element(org_row_xpath)
        # Click the Delete button for the located organization

        self.driver.click_element(self.confirm_delete_btn)

        self.driver.click_element(self.confirm_del_pop)
        time.sleep(30)
        # Validate that the organization is no longer in the table
        if self.driver.is_element_visible(f"//table//td[text()='{org_name}']"):
            raise AssertionError(f"Organization '{org_name}' was not deleted successfully.")

    def logout(self):
            """Perform logout action and validate."""
            # Click on the user profile or logout menu (if applicable)
            self.driver.click_element(self.user_profile_icon)  # Adjust if there's a profile dropdown
            self.driver.click_element(self.logout_button)

            # Validate that the user is logged out (e.g., redirected to the login page)
            if not self.driver.is_element_visible(self.username_field):
                raise AssertionError("Logout failed. Login page is not visible.")
