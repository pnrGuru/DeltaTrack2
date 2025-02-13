import pytest
from datetime import datetime, time

from DT_Kiwi.pages.organizations_page import OrganizationPage
from DT_Kiwi.pages.user_groups import UserGroupPage

from DT_Kiwi.utils.browser_utils import BrowserManager
from DT_Kiwi.utils.env_utils import URL, USERNAME, PASSWORD

from DT_Kiwi.utils.kiwi_tcms_integration import KiwiTCMSIntegration
from DT_Kiwi.utils.playwright_driver import PlaywrightDriver


@pytest.mark.order(1)
class TestOrganizations:
    @classmethod
    def setup_class(cls):
        """Set up browser, initialize page objects, and create a test run in Kiwi TCMS."""
        cls.browser_manager = BrowserManager()
        cls.page = cls.browser_manager.launch_browser()
        cls.driver = PlaywrightDriver(cls.page)  # Initialize PlaywrightDriver
        cls.org_page = OrganizationPage(cls.driver)

        cls.user_groups=UserGroupPage(cls.driver)

        #Initialize Kiwi TCMS integration
        cls.kiwi = KiwiTCMSIntegration()

        # Test details for Kiwi TCMS
        cls.product_name = "UBQ-UI-Testing"
        cls.version_name = "V1.1.0"
        cls.build_name = "UAT_Build"
        cls.plan_name = "UBQ Test"
        cls.case_ids = [26, 27, 28, 29, 30,42]  # test case IDs

        # Get current date and time dynamically
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Create a test run in Kiwi TCMS
        cls.test_run = cls.kiwi.create_test_run(
        name="Automated Test Run",
        product_name=cls.product_name,
        version_name=cls.version_name,
        build_name=cls.build_name,
        plan_name=cls.plan_name,
        case_ids=cls.case_ids,
        summary=f"Automated test run for organization on {current_datetime}")
        cls.test_run_id = cls.test_run["id"]

    @classmethod
    def teardown_class(cls):
        cls.browser_manager.close_browser()



    @pytest.mark.order(1)
    def test_login_with_valid_credentials(self):
        """Test valid login and update the result in Kiwi TCMS."""
        #try:
        self.org_page.navigate(URL)
        self.org_page.login(USERNAME, PASSWORD)

            # Update test case result as Passed
           # self.kiwi.update_test_case_result(
               # test_run_id=self.test_run_id,
               # test_case_id=1,  # Test case ID for this test
               # status=4,  # 4 = Passed
               # notes="Login with valid credentials succeeded."
           # )
        #except Exception as e:
            # Update test case result as Failed
           # self.kiwi.update_test_case_result(
               # test_run_id=self.test_run_id,
              #  test_case_id=1,
               # status=5,  # 5 = Failed
               # notes=f"Login with valid credentials failed: {e}"
            #)
           # raise
    def test_navigation_to_user_mtm(self):
        self.org_page.navigate_to_user_mtm()

    def test_add_userr_management(self):
        self.org_page.adduser_mtm(self,"anusha@gmail.com")


'''  def test_verify_dashboard(self):
        """Verify Dashboard text and update the result in Kiwi TCMS."""
        #try:
        assert self.org_page.login_successful(), "Login failed!"
        # Update test case result as Passed
            self.kiwi.update_test_case_result(
                test_run_id=self.test_run_id,
                test_case_id=3,  # Test case ID for this test
                status=4,  # 4 = Passed
                notes="Dashboard verification succeeded."
            )
        except Exception as e:
            # Update test case result as Failed
            self.kiwi.update_test_case_result(
                test_run_id=self.test_run_id,
                test_case_id=3,
                status=5,  # 5 = Failed
                notes=f"Dashboard verification failed: {e}"
            )
            raise



    def test_verify_user_menu_options(self):
        """Click on the User Icon and verify the presence of Organization, User Management, and User Group options."""
        #try:
        assert self.org_page.click_user_icon_and_verify_menu(), "One or more user menu options are missing!"
        # Update test case result as Passed
        self.kiwi.update_test_case_result(
                test_run_id=self.test_run_id,
                test_case_id=4,  # Test case ID for this test
                status=4,  # 4 = Passed
                notes="Network users icon verification succeeded."
            )
        except Exception as e:
            # Update test case result as Failed
            self.kiwi.update_test_case_result(
                test_run_id=self.test_run_id,
                test_case_id=4,
                status=5,  # 5 = Failed
                notes=f"Network users icon verification failed: {e}"
            )
            raise

        #Verify Navigation to User Management tc-5#

    @pytest.mark.order(4)
    def test_navigation_to_user_management(self):
        """Test navigation to the User Management page."""
        #try:
        assert self.org_page.navigate_to_user_management(), "Failed to navigate to the User Management page!"

        # Update test case result as Passed
        self.kiwi.update_test_case_result(
                test_run_id=self.test_run_id,
                test_case_id=5,  # Test case ID for this test
                status=4,  # 4 = Passed
                notes="Test navigation to the User Management page succeeded."
            )

        except Exception as e:
            # Update test case result as Failed
            self.kiwi.update_test_case_result(
                test_run_id=self.test_run_id,
                test_case_id=5,
                status=5,  # 5 = Failed
                notes=f"Test navigation to the User Management page failed: {e}"
            )

            raise  # ✅ Re-raise the caught exception correctly

    @pytest.mark.order(4)
    def test_navigation_to_user_groups(self):
        """Test navigation to the User Management page."""
        #try:
        assert self.org_page.navigate_to_user_groups(), "Failed to navigate to the User Management page!"
        # Update test case result as Passed
            #self.kiwi.update_test_case_result(
             #   test_run_id=self.test_run_id,
              #  test_case_id=6,  # Test case ID for this test
               # status=4,  # 4 = Passed
              #  notes="Test navigation to the User Management page succeeded."
            #)
        #except Exception as e:
            # Update test case result as Failed
            #self.kiwi.update_test_case_result(
              #  test_run_id=self.test_run_id,
               # test_case_id=6,
               # status=5,  # 5 = Failed
               # notes=f"Test navigation to the User Management page failed: {e}"
           # )
        #raise
#................................................................................................#
    #tc-8
    @pytest.mark.order(4)
    def test_navigation_to_organizations(self):
        """Test navigation to the User Management page."""
        try:
            assert self.org_page.navigate_to_organizations(), "Failed to navigate to the Organizations page!"
            # Update test case result as Passed
            self.kiwi.update_test_case_result(
                test_run_id=self.test_run_id,
                test_case_id=8,  # Test case ID for this test
                status=4,  # 4 = Passed
                notes="Test navigation to the User organization page. succeeded."
            )
        except Exception as e:
            # Update test case result as Failed
            self.kiwi.update_test_case_result(
                test_run_id=self.test_run_id,
                test_case_id=8,
                status=5,  # 5 = Failed
                notes=f"Test navigation to the User organization page: {e}"
            )
        raise
   #...................................................................................#

    def test_organization_mandatory_fields(self):
        try:
            assert self.org_page.verify_add_organization_uielements(), "UI elements verification failed"
            # Update test case result as Passed
            self.kiwi.update_test_case_result(
            test_run_id=self.test_run_id,
            test_case_id=9,  # Test case ID for this test
                status=4,  # 4 = Passed
                notes="Test navigation to the User Organization page succeeded."
            )
        except Exception as e:
            # Update test case result as Failed
            self.kiwi.update_test_case_result(
                test_run_id=self.test_run_id,
                test_case_id=9,
                status=5,  # 5 = Failed
                notes=f"Test navigation to the User Organization page failed: {str(e)}"
            )
            raise e  # Only re-raise the actual error if it occurs



    @pytest.mark.order(8)
    def test_mandatory_fields(self):

        try:

            assert self.org_page.verify_mandatory_fields()

            # Update test case result as Passed
            self.kiwi.update_test_case_result(
                test_run_id=self.test_run_id,
                test_case_id=10,  # Test case ID for organization deletion
                status=4,  # 4 = Passed
                notes="verified all Mandatory fields is successful."
            )
        except Exception as e:
            # Update test case result as Failed
            self.kiwi.update_test_case_result(
                test_run_id=self.test_run_id,
                test_case_id=10,
                status=5,  # 5 = Failed
                notes=f"all fields are Mandatory: {e}"
            )
            raise

    @pytest.mark.order(9)
    def test_add_ent_org(self):
        
       try:

           assert self.org_page.verify_add_organization(f"Test OrgAutomationfriday",
                                                        "Test Descriptionn"), "Organization creation failed!"

           # Update test case result as Passed
           self.kiwi.update_test_case_result(
               test_run_id=self.test_run_id,
               test_case_id=10,  # Test case ID for organization deletion
               status=4,  # 4 = Passed
               notes="verified all Mandatory fields is successful."
           )
       except Exception as e:
           # Update test case result as Failed
           self.kiwi.update_test_case_result(
               test_run_id=self.test_run_id,
               test_case_id=10,
               status=5,  # 5 = Failed
               notes=f"all fields are Mandatory: {e}"
           )
           raise
    @pytest.mark.order(10)
    def test_search_org(self):

        #try:

            organization_name = "Test OrgAutomationTesting team"
            organization_desc = "Description for Test OrgAutomation"
            assert self.org_page.verify_add_organization(organization_name,
                                                         organization_desc), "Failed to add organization."
            assert self.org_page.search_for_organization(organization_name)
            # Step 5: Verify if the organization appears in the search results
            assert self.org_page.is_organization_present_in_search_results(
                organization_name), f"Organization '{organization_name}' not found in search results."

             self.kiwi.update_test_case_result(
                test_run_id=self.test_run_id,
                test_case_id=45,  # Test case ID for organization deletion
                status=4,  # 4 = Passed
                notes="Search operation successful"
            )
        except Exception as e:
            # Update test case result as Failed
            self.kiwi.update_test_case_result(
                test_run_id=self.test_run_id,
                test_case_id=45,
                status=5,  # 5 = Failed
                notes=f"not found in search results: {e}"
            )
            raise

# user groups
    @pytest.mark.order(11)
    def test_verify_user_groups_elements(self):
       # try:
        assert self.user_groups.verify_user_groups_elements(), "Some User Groups elements are missing"

    self.kiwi.update_test_case_result(
                test_run_id=self.test_run_id,
                test_case_id=46,  # Test case ID for organization deletion
                status=4,  # 4 = Passed
                notes="all elements are present"
            )
        except Exception as e:
            # Update test case result as Failed
            self.kiwi.update_test_case_result(
                test_run_id=self.test_run_id,
                test_case_id=46,
                status=5,  # 5 = Failed
                notes=f"not found in search results: {e}"
            )
            raise
            


    @pytest.mark.order(12)
    def test_logout(self):
        #try:
            # Delete the organization
            self.org_page.user_logout()
            
            # Update test case result as Passed
            self.kiwi.update_test_case_result(
                test_run_id=self.test_run_id,
                test_case_id=30,  # Test case ID for log out user
                status=4,  # 4 = Passed
                notes="User Log out successfully."
            )
        except Exception as e:
            # Update test case result as Failed
                self.kiwi.update_test_case_result(
                test_run_id=self.test_run_id,
                test_case_id=30,
                status=5,  # 5 = Failed
                notes=f"User Log out failed with error: {e}"
                )
                raise
            
    @pytest.mark.order(3)
    def test_mandatory_fields(self):
        assert self.org_page.verify_mandatory_fields()

    @pytest.mark.order(4)
    def test_add_ent_org(self):

        assert self.org_page.verify_add_organization("Test OrgAutomation",
                                                     "Test Description"), "Organization creation failed!"

    @pytest.mark.order(5)
    def test_search_org(self):
        # Setup
        organization_name = "DEnt2 Org"

        # Execution
        self.org_page.search_for_organization(organization_name)

        # Validation
        assert self.org_page.is_organization_present_in_search_results(
            organization_name), f"'{organization_name}' not found in search results."

    @pytest.mark.order(6)
    def test_no_of_organizations(self):
        # Calculate the number of records
        num_of_records = self.org_page.get_number_of_records()

        # Further validation if needed
        assert num_of_records > 0, "No records found in the search results table."

    @pytest.mark.order(7)
    def test_search_and_select_organization(self):
        """Search for an organization, select it, and verify selection."""

        org_name = "DEnt2 Org"

        # Search and select organization
        self.org_page.search_and_select_organization(org_name)


        # ✅ Ensure UI has time to update before checking
        self.driver.page.wait_for_timeout(1000)  # 1-second wait

        # Verify that the selected organization is updated
        selected_org = self.org_page.get_selected_organization_name()
        assert selected_org == org_name, f"Expected '{org_name}', but found '{selected_org}'"

    def test_edit_organization(self):
        """Test Editing an Organization with a Unique Description"""
        org_name = "DEnt2 Org"
        new_description="new updated"
        self.org_page.edit_organization(org_name, new_description)

    @pytest.mark.order(9)
    def test_validate_organization_table(self):
        """Test that organization table headers match expected values.

        # Call the validation function from the page object
        assert self.org_page.validate_organization_table(), "Organization table validation failed!"

    # Validate Organization

    @pytest.mark.order(10)
    def test_navigate_to_organization(self):
    self.org_page.navigate_to_organization()'''







