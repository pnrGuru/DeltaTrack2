from datetime import datetime

import pytest
from pages.organizations_page import OrganizationPage
from utils.browser_utils import BrowserManager
from utils.playwright_driver import PlaywrightDriver
from utils.env_utils import URL, USERNAME, PASSWORD
from utils.kiwi_tcms_integration import KiwiTCMSIntegration


@pytest.mark.order(1)
class TestOrganizations:
    @classmethod
    def setup_class(cls):
        """Set up browser, initialize page objects, and create a test run in Kiwi TCMS."""
        cls.browser_manager = BrowserManager()
        cls.page = cls.browser_manager.launch_browser()
        cls.driver = PlaywrightDriver(cls.page)  # Initialize PlaywrightDriver
        cls.org_page = OrganizationPage(cls.driver)  # Pass PlaywrightDriver instance

        # Initialize Kiwi TCMS integration
        cls.kiwi = KiwiTCMSIntegration()

        # Test details for Kiwi TCMS
        cls.product_name = "UBQ-UI-Testing"
        cls.version_name = "V1.1.0"
        cls.build_name = "UAT_Build"
        cls.plan_name = "Delta Track Automation Project"
        cls.case_ids = [1, 4, 5, 26, 27, 28, 29, 30, 31, 32]  # test case IDs

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
            summary=f"Automated test run for organization on {current_datetime}"
        )
        cls.test_run_id = cls.test_run["id"]

    @classmethod
    def teardown_class(cls):
        """Close the browser after all tests."""
        cls.browser_manager.close_browser()

    @pytest.mark.order(1)
    def test_login_with_valid_credentials(self):
        """Test valid login and update the result in Kiwi TCMS."""
        try:
            self.org_page.navigate(URL)
            self.org_page.login(USERNAME, PASSWORD)

            # Update test case result as Passed
            self.kiwi.update_test_case_result(
                test_run_id=self.test_run_id,
                test_case_id=1,  # Test case ID for this test
                status=4,  # 4 = Passed
                notes="Login with valid credentials succeeded."
            )
        except Exception as e:
            # Update test case result as Failed
            self.kiwi.update_test_case_result(
                test_run_id=self.test_run_id,
                test_case_id=1,
                status=5,  # 5 = Failed
                notes=f"Login with valid credentials failed: {e}"
            )
            raise

    # @pytest.mark.order(2)
    def test_verify_dashboard(self):
        """Verify Dashboard text and update the result in Kiwi TCMS."""
        try:
            assert self.org_page.login_successful(), "Login failed!"
            # Update test case result as Passed
            self.kiwi.update_test_case_result(
                test_run_id=self.test_run_id,
                test_case_id=26,  # Test case ID for this test
                status=4,  # 4 = Passed
                notes="Dashboard verification succeeded."
            )
        except Exception as e:
            # Update test case result as Failed
            self.kiwi.update_test_case_result(
                test_run_id=self.test_run_id,
                test_case_id=26,
                status=5,  # 5 = Failed
                notes=f"Dashboard verification failed: {e}"
            )
            raise

    # @pytest.mark.order(3)
    def test_negative_create_organization1(self):
        """Verify Mandatory fields while creating organization."""
        try:
            self.org_page.navigate_to_organization()
            self.org_page.add_organization(name=" ", description="test")
            assert self.org_page.get_name_required_error(), "Error message for 'Name is required' not displayed."

            # Update test case result as Passed
            self.kiwi.update_test_case_result(
                test_run_id=self.test_run_id,
                test_case_id=31,  # Test case ID for this test
                status=4,  # 4 = Passed
                notes="Name is required Message displayed"
            )
        except Exception as e:
            # Update test case result as Failed
            self.kiwi.update_test_case_result(
                test_run_id=self.test_run_id,
                test_case_id=31,
                status=5,  # 5 = Failed
                notes=f"Error message failed: {e}"
            )
            raise

    # @pytest.mark.order(4)
    def test_negative_create_organization2(self):
        """Verify with special characters while creating organization."""
        try:
            self.org_page.add_organization(name="%^&**#$%%", description="test")
            assert self.org_page.get_error_message_org(), "Error while creating organization Message displayed."

            # Update test case result as Passed
            self.kiwi.update_test_case_result(
                test_run_id=self.test_run_id,
                test_case_id=32,  # Test case ID for this test
                status=4,  # 4 = Passed
                notes="while creating organization Error Message Displayed."
            )
        except Exception as e:
            # Update test case result as Failed
            self.kiwi.update_test_case_result(
                test_run_id=self.test_run_id,
                test_case_id=32,
                status=5,  # 5 = Failed
                notes=f"Error message failed: {e}"
            )
            raise

    # @pytest.mark.order(5)
    def test_create_organization(self):
        """Verify with valid test data for creating organization."""
        try:
            self.org_page.create_org(name="Cognitivzen Tester", description="QA")
            assert self.org_page.create_org_success_message(), "Organization is created successfully Message displayed."

            # Update test case result as Passed
            self.kiwi.update_test_case_result(
                test_run_id=self.test_run_id,
                test_case_id=27,  # Test case ID for this test
                status=4,  # 4 = Passed
                notes="Organization is created successfully Message Displayed."
            )
        except Exception as e:
            # Update test case result as Failed
            self.kiwi.update_test_case_result(
                test_run_id=self.test_run_id,
                test_case_id=27,
                status=5,  # 5 = Failed
                notes=f"Error message: {e}"
            )
            raise

    # @pytest.mark.order(6)
    def test_delete_organization(self):
        """
        Delete an organization and validate its deletion.
        """
        try:
            # Delete the organization
            self.org_page.delete_organization(org_name="Cognitivzen Tester")

            # Update test case result as Passed
            self.kiwi.update_test_case_result(
                test_run_id=self.test_run_id,
                test_case_id=29,  # Test case ID for organization deletion
                status=4,  # 4 = Passed
                notes="Organization deleted successfully."
            )
        except Exception as e:
            # Update test case result as Failed
            self.kiwi.update_test_case_result(
                test_run_id=self.test_run_id,
                test_case_id=29,
                status=5,  # 5 = Failed
                notes=f"Organization deletion failed with error: {e}"
            )
            raise

    # @pytest.mark.order(7)
    def test_logout(self):
        """
        User logout the application.
        """
        try:
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
