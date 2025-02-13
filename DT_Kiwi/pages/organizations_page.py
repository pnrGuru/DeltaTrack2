import logging

from DT_Kiwi.utils.playwright_driver import PlaywrightDriver


class OrganizationPage:
    def __init__(self, driver: PlaywrightDriver):
        self.driver = driver
       # self.networkusers_icon = '//div[@id="Network Users"]'
        self.org_navigation = '//li[@id="organizations"]'
        self.org_header_txt = '//h2[contains(text(),"Organizations")]'
        self.org_add = '//img[@alt="add"]'
        self.organization_option='//li[@id="organizations"]'
        self.add_enterprise_org = '//h5[contains(text(),"Enterprise Organization")]'
        self.input_enterprise_org = '#add-org-name'
        self.input_description_org = '//input[@id="add-org-description"]'
        self.org_submit_btn = '//button[@id="add-org-submit-button"]'
        self.name_require_txt = '//p[@id="add-org-name-helper-text" and contains(text(), "Name is required")]'
        self.error_message_org_txt = '//div[@id="notistack-snackbar" and text()="Error while creating organization!"]'
        #new
        self.error_msg_name='#add-org-name-helper-text'
        self.error_msg_des='#add-org-description-helper-text'

        self.create_org_success_message_txt = '//div[@id="notistack-snackbar" and contains(text(), "Organization is created successfully!")]'
        self.description_require_txt = '//p[contains(text(),"Description is required")]'
        self.username_field = '//input[@id="username"]'
        self.continue_btn = '//button[contains(text(),"Continue")]'
        self.password_field = '//input[@id="password"]'
        self.dashboard_text = '//h2[contains(text(),"Network Admin")]'
        self.confirm_delete_btn = "//button[@id='delete-org-button']"
        self.confirm_del_pop = "//button[contains(text(),'Delete')]"
        #self.network_users_icon = '//div[@aria-label="Network Users"]'
        # self.search_btn = '//input[@id=":r101:"]'
        self.search_btn = '//input[@placeholder="Search"]'
        self.select_btn = '//span[normalize-space()="Cognitivzen"]'
        self.logout_dropdown = '#user-menu'
        self.logout_user = '//li[text()="Log Out"]'
        #verify click on Network isers
        self.org_navigation = '//li[@id="organizations"]'  # organization
        self.ent_mtm = '//li[@id="user-mgmt"]'
        self.user_mtm_dashboard = '//h2[contains(text(),"Users")]'
        self.user_groups = '//li[@id="user-groups"]'
        self.user_groups_dashboard = '//h2[contains(text(),"Users")]'
        self.user_groups = '//li[@id="user-groups"]'
        self.network_users_icon = '//ul//li//div[@id="Network Users"]'

        #Add organization
        self.add_org = '//h5[contains(text(),"Organization")]'
        self.add_org_header = '//h2[contains(text(),"Add Organization")]'
        self.main_search = "#navbar-org-select"
        self.ent_mtm = '//li[@id="user-mgmt"]'
        self.user_mtm_dashboard = '//h2[contains(text(),"Users")]'
        self.user_groups = '//li[@id="user-groups"]'
        self.user_groups_dashboard = '//h2[contains(text(),"Users")]'
        self.user_groups = '//li[@id="user-groups"]'
        self.org_add = '//img[@alt="add"]'  # add button
        self.add_enterprise_org = '//h5[contains(text(),"Enterprise Organization")]'  # enterprise org
        self.add_org = '//h5[contains(text(),"Organization")]'
        self.org_header_txt = '//h2[contains(text(),"Organizations")]'
        self.username_field = '//input[@id="username"]'
        self.continue_btn = '//button[contains(text(),"Continue")]'
        self.password_field = '//input[@id="password"]'
        self.add_org_header = '//h2[contains(text(),"Add Organization")]'
        self.name_input = '#add-org-name'
        self.desc_input = '#add-org-description'
        self.app_dropdown = '#Organizations-applications-select'
        self.submit_button = '#add-org-submit-button'
        # self.close_button=
        self.name_error_msg = '#add-org-name-helper-text'
        self.desc_error_msg = '#add-org-description-helper-text'
        self.success_message = '#notistack-snackbar'
        self.search = '//input[@placeholder="Search"]'
        self.close_btn = '//div[@class="MuiBox-root css-v0jpdd"]'
        self.table_selector = '//table//tr'
        self.main_search = "#navbar-org-select"
        self.main_search_org_name = "//input[@value='DEnt2 Org']"
        self.option = '//input[@value="DEnt2 Org"]'
        self.edit_button_selector = '#edit-org-button'
        self.check_box = ""
        self.table_th_elements = "//table//tr//th"
        self.org_table_none = "//tr//th[1]"
        self.org_table_name = '//tr//th[2]'
        self.org_table_description = '//tr//th[3]'
        self.org_table_users = '//tr//th[4]'  # Total Users column
        self.org_table_created_at = '//tr//th[5]'  # Created At column
        self.org_table_actions = '//tr//th[6]'
        self.enable_sync_checkbox = '//div[contains(text(),"Enable sync")]'
        self.token_input = '#add-org-token'

        #User Management
        self.scroll_element = "//div[@id='SideNav']"

        self.adduser_mtm='//button[@id="add-user-button"]'
        self.user_add_org='//input//following::label[@id="selected-org-label"]'
        self.user_email='//input[@id="add-user-email"]'
        self.user_role_drop_down='#add-user-role'
        self.admin="//ul[@role='listbox']//li[1]"
        self.writer=""


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

        # TC-4#
    def click_user_icon_and_verify_menu(self) -> bool:
        """Clicks on the User Icon and verifies the presence of Organization, User Management, and User Group options."""

        self.driver.click_element(self.network_users_icon)  # Click User Icon

        # Check if menu options are visible
        org_present = self.driver.is_element_visible(self.org_navigation)
        management_present = self.driver.is_element_visible(self.ent_mtm)
        group_present = self.driver.is_element_visible(self.user_groups)

        return org_present and management_present and group_present
        #TC-5
    def navigate_to_user_management(self) -> bool:
        """Navigates to the User Management page and verifies successful navigation."""

        self.driver.click_element(self.network_users_icon)  # Click on "Network Users"
        self.driver.click_element(self.ent_mtm)  # Select "User Management"

        # Validate that the User Management page is displayed
        return self.driver.is_element_visible(self.user_mtm_dashboard)
    #tc-6
    def navigate_to_user_groups(self) -> bool:
        """Navigates to the User Management page and verifies successful navigation."""

        self.driver.click_element(self.network_users_icon)  # Click on "Network Users"
        self.driver.click_element(self.user_groups)  # Select "User Management"

        # Validate that the User Management page is displayed
        return self.driver.is_element_visible(self.user_groups_dashboard)
    #........................................................................#
    #tc-7
    def navigate_to_organizations(self) -> bool:
        """Navigates to the Organizations page and verifies successful navigation."""
        try:
            self.driver.click_element(self.network_users_icon)  # Click on "Network Users"
            self.driver.click_element(self.org_navigation)  # Select "Organizations"

            # Validate navigation by checking if "Organizations" header is visible
            return self.driver.is_element_visible(self.org_header_txt)
        except Exception as e:
            logging.error(f"Failed to navigate to Organizations: {e}")
            return False

    def navigate_suborganization(self):
        self.driver.click_element(self.network_users_icon)
        self.driver.click_element(self.org_navigation)
        # adding organization
        self.driver.click_element(self.org_add)
        # clicks Organization
        self.driver.click_element(self.add_org)

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

        param org_name: User logout application.
        """
        self.driver.click_element(self.logout_dropdown)
        self.driver.click_element(self.logout_user)

        # ....................................................................................
    def verify_mandatory_fields(self) -> bool:
            """Checks if Name and Description fields are mandatory in the 'Add Organization' popup."""

            # Click the Submit button without entering any data
            self.driver.click_element(self.submit_button)

            # Check if validation messages appear for the Name and Description fields
            name_error = self.driver.is_element_visible(self.name_error_msg)  # Error message for Name field
            desc_error = self.driver.is_element_visible(self.desc_error_msg)  # Error message for Description field
            self.driver.click_element(self.close_btn)
            return name_error and desc_error


    def verify_add_organization(self, uname, desc) -> bool:
            self.driver.click_element(self.org_add)
            self.driver.click_element(self.add_enterprise_org)
            self.driver.fill_textbox(self.name_input, uname)
            self.driver.fill_textbox(self.desc_input, desc)
            self.driver.click_element(self.submit_button)

            # Wait for success message to appear (if necessary)
            return self.driver.is_element_visible(self.success_message)

    def is_organization_present_in_table(self, name) -> bool:
            """Checks if the given organization name is present in the table."""
            org_xpath = f"//td[contains(text(), '{name}')]"  # Adjust based on your table structure
            return self.driver.is_element_visible(org_xpath)



    def search_for_organization(self, org_name: str):
            """Search for an organization by name."""
            self.driver.fill_textbox(self.search, org_name)
            # Simulate pressing "Enter" key
            self.driver.press_enter(self.search)

    def is_organization_present_in_search_results(self, name) -> bool:
            """Checks if the given organization name appears in the filtered table after search."""
            org_xpath = f"//td[contains(text(), '{name}')]"  # Adjust based on your table structure
            return self.driver.is_element_visible(org_xpath)


    def search_and_select_organization(self, org_name: str):
            """Search for an organization by name and select it from the dropdown."""

            dropdown_option = self.main_search_org_name  # Playwright allows 'text' selectors

            # Step 1: Click on the search box
            self.driver.click_element(self.main_search)

            # Step 2: Clear any existing text and enter the organization name
            self.driver.clear_textbox(self.main_search)
            self.driver.fill_textbox(self.main_search, org_name)

            # Step 3: Wait for the dropdown to appear and click on the correct option
            self.driver.click_element(dropdown_option)

    def get_selected_organization_name(self):
            """Get the currently selected organization text from the search box."""
            selected_text = self.driver.get_text(self.main_search)

            return selected_text

    def get_number_of_records(self) -> int:
            """
            Get the number of records in the table.

            :return: The number of records in the table.
            """
            rows = self.driver.page.locator(f"{self.table_selector}")
            num_of_records = rows.count()

            return num_of_records

        # edit organization
    def edit_organization(self, org_name: str, new_description: str):
            """Edit an organization, update description, and validate update."""
            logging.info(f"Editing organization: {org_name}")

            # Step 1: Search and Select Organization
            self.search_and_select_organization(org_name)

            # Step 2: Select First Checkbox
            first_check_box = "//tr[1]//input[@type='checkbox']"
            self.driver.click_element(first_check_box)
            logging.info("Selected first checkbox")
            self.driver.page.wait_for_timeout(1000)

            # Step 3: Click Edit Button
            self.driver.click_element(self.edit_button_selector)
            logging.info("Clicked Edit button")

             # Step 4: Validate Existing Organization Name
            existing_org_name = self.get_selected_organization_name()
            assert existing_org_name == org_name, f"Expected {org_name}, but found {existing_org_name}"

            # Step 5: Edit Description
            self.driver.clear_textbox(self.desc_input)
            self.driver.fill_textbox(self.desc_input, new_description)
            logging.info(f"Updated description to: {new_description}")

            # Step 6: Click Submit
            self.driver.page.wait_for_timeout(1000)
            self.driver.click_element(self.submit_button)
            logging.info("Clicked Submit button")

            # Step 7: Validate Success Message
            success_msg = self.driver.get_text(self.success_message).strip()
            assert "success" in success_msg.lower(), "Edit operation failed"
            logging.info(f"Success message: {success_msg}")

            # Step 8: Re-validate Description
            self.search_for_organization(org_name)
            updated_description = self.driver.get_text(self.desc_input).strip()
            assert updated_description == new_description, f"Expected '{new_description}', but found '{updated_description}'"

            logging.info("Organization edit verified successfully!")

    def validate_organization_table(self) -> bool:
            """Verifies that all key elements are present in the Organization table."""

            expected_texts = ["", "Name ", "Description ", "Total Users ", "Created At ", "Enterprise Organization "]

            elements = [
                self.org_table_none,  # Placeholder or empty value (None)
                self.org_table_name,  # Name column
                self.org_table_description,  # Description column
                self.org_table_users,  # Total Users column
                self.org_table_created_at,  # Created At column
                self.org_table_actions  # Actions column (Edit/Delete buttons)
            ]

            # Extract and clean text from each element
            actual_texts = []
            for elem in elements:
                if elem:
                    text = self.driver.get_text(elem).strip()
                    text = " ".join(text.split())  # Normalize spaces
                    text = ''.join([char for char in text if not char.isdigit()])  # Remove unexpected numbers
                else:
                    text = "None"

                actual_texts.append(text)

            # Validation
            assert len(actual_texts) == len(
                expected_texts), f"Expected {len(expected_texts)} elements, but found {len(actual_texts)}"

            for i in range(len(expected_texts)):
                assert actual_texts[i] == expected_texts[
                    i], f"Mismatch at index {i}: Expected '{expected_texts[i]}', but found '{actual_texts[i]}'"

            logging.info("✅ Organization table elements are correctly displayed.")
            return True

    #organization module

    def navigate_to_organization(self) -> bool:
            """Navigates to the Enterprise Organization page and validates that the organization popup appears."""

            self.driver.click_element(self.network_users_icon)
            self.driver.click_element(self.org_navigation)

            # Click to add organization
            self.driver.click_element(self.org_add)

            # Click Enterprise Organization
            self.driver.click_element(self.add_org)

            # Validation - Ensure the 'Add Organization' popup appears
            return self.driver.is_element_visible(self.add_org_header)  # Checks for "Add Organization" header

    def verify_add_organization_uielements(self) -> bool:
            """Checks if all required UI elements in the 'Add Organization' popup are visible."""
            return all([
                self.driver.is_element_visible(self.add_org_header),  # "Add Organization" header
                self.driver.is_element_visible(self.main_search),  # Organization dropdown
                self.driver.is_element_visible(self.name_input),  # Name input field
                self.driver.is_element_visible(self.desc_input),  # Description input field
                self.driver.is_element_visible(self.app_dropdown),  # Applications dropdown
                self.driver.is_element_visible(self.submit_button),  # Submit button
                self.driver.is_element_visible(self.enable_sync_checkbox),  # Enable Sync checkbox
                self.driver.is_element_visible(self.token_input),  # Token input field
                self.driver.is_element_visible(self.submit_button)
            ]) 

    def navigate_to_user_mtm(self) :
        self.driver.scroll_to_element(self.scroll_element)
        self.driver.scroll_to_bottom()
        self.driver.click_element(self.network_users_icon)
        self.driver.page.wait_for_timeout(1000)
        self.driver.click_element(self.ent_mtm)
        # Assertion to verify the dashboard is displayed

        self.driver.is_element_visible(self.dashboard_selector)

    def add_userr_management(self,email):
        self.driver.fill_textbox(self.user_email,email)
        self.driver.click_element(self.user_role_drop_down)
        # Verify the selection
        self.driver.click_element(self.admin)






