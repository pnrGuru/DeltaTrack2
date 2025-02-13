
from datetime import datetime

import pytest

from DT_Kiwi.pages.ent_org_page import EntOrganizationPage
from DT_Kiwi.utils.browser_utils import BrowserManager
from DT_Kiwi.utils.kiwi_tcms_integration import KiwiTCMSIntegration
from DT_Kiwi.utils.playwright_driver import PlaywrightDriver
from DT_Kiwi.utils.env_utils import URL, USERNAME, PASSWORD


@pytest.mark.order(1)
class TestEntOrganizations:
    @classmethod
    def setup_class(cls):
        """Set up browser, initialize page objects, and create a test run in Kiwi TCMS."""
        cls.browser_manager = BrowserManager()
        cls.page = cls.browser_manager.launch_browser()
        cls.driver = PlaywrightDriver(cls.page)  # Initialize PlaywrightDriver
        cls.ent_page=EntOrganizationPage(cls.driver)

    @classmethod
    def teardown_class(cls):
        cls.browser_manager.close_browser()


    @pytest.mark.order(1)
    def test_login_with_valid_credentials(self):
        """Test valid login and update the result in Kiwi TCMS."""

        self.ent_page.navigate(URL)
        self.ent_page.login(USERNAME, PASSWORD)

    @pytest.mark.order(2)
    def  test_navigation_to_organization(self):
        self.ent_page.navigate_to_organization()

    @pytest.mark.order(3)
    def test_mandatory_fields(self):
        assert self.ent_page.verify_mandatory_fields()

    @pytest.mark.order(4)
    def test_add_ent_org(self):

        assert self.ent_page.verify_add_organization("Test OrgAutomation", "Test Description"), "Organization creation failed!"

    @pytest.mark.order(5)
    def test_search_org(self):
        # Setup
        organization_name = "DEnt2 Org"

        # Execution
        self.ent_page.search_for_organization(organization_name)

        # Validation
        assert self.ent_page.is_organization_present_in_search_results(organization_name), f"'{organization_name}' not found in search results."

    @pytest.mark.order(6)
    def test_no_of_organizations(self):
        # Calculate the number of records
        num_of_records = self.ent_page.get_number_of_records()


        # Further validation if needed
        assert num_of_records > 0, "No records found in the search results table."

    @pytest.mark.order(7)
    def test_search_and_select_organization(self):
        """Search for an organization, select it, and verify selection."""

        org_name = "DEnt2 Org"

        # Search and select organization
        self.ent_page.search_and_select_organization(org_name)

        # ✅ Ensure UI has time to update before checking
        self.driver.page.wait_for_timeout(1000)  # 1-second wait

        # Verify that the selected organization is updated
        selected_org = self.ent_page.get_selected_organization_name()
        assert selected_org == org_name, f"Expected '{org_name}', but found '{selected_org}'"

    #def test_edit_organization(self):
        """Test Editing an Organization with a Unique Description"""
        org_name = "DEnt2 Org"

        # Generate a unique description using timestamp
        #new_description = f"Updated Description {int(time.time())}"

        # Call the edit organization function
        #self.ent_page.edit_organization(org_name, new_description)

    @pytest.mark.order(9)
    def test_validate_organization_table(self):
        """Test that organization table headers match expected values."""

        # Call the validation function from the page object
        assert self.ent_page.validate_organization_table(), "Organization table validation failed!"



    #Validate Organization

    @pytest.mark.order(10)
    def test_navigate_to_organization(self):
        self.ent_page.navigate_to_organization()


    def test_organization_mandatory_fields(self):
        self.ent_page.verify_add_organization_uielements()









