import pytest
from pages.networkadmin_page import LoginPage
from utils.browser_utils import BrowserManager
from utils.playwright_driver import PlaywrightDriver
from utils.env_utils import URL, USERNAME, PASSWORD
from utils.kiwi_tcms_integration import KiwiTCMSIntegration


@pytest.mark.order(2)
class TestLogin:
    @classmethod
    @pytest.fixture(autouse=True)
    def setup_class(cls):
        """Set up browser, initialize page objects, and create a test run in Kiwi TCMS."""
        cls.browser_manager = BrowserManager()
        cls.page = cls.browser_manager.launch_browser()
        cls.driver = PlaywrightDriver(cls.page)  # Initialize PlaywrightDriver
        cls.login_page = LoginPage(cls.driver)  # Pass PlaywrightDriver instance

        # Initialize Kiwi TCMS integration
        cls.kiwi = KiwiTCMSIntegration()

        # Test details for Kiwi TCMS
        cls.product_name = "UBQ-UI-Testing"
        cls.version_name = "V1.1.0"
        cls.build_name = "UAT_Build"
        cls.plan_name = "UBQ Test"
        cls.case_ids = [4, 5]  # test case IDs

        # Create a test run in Kiwi TCMS
        cls.test_run = cls.kiwi.create_test_run(
            name="Automated Test Run",
            product_name=cls.product_name,
            version_name=cls.version_name,
            build_name=cls.build_name,
            plan_name=cls.plan_name,
            case_ids=cls.case_ids,
            summary="Automated test run created via integration."
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
            self.login_page.navigate(URL)
            self.login_page.login(USERNAME, PASSWORD)

            # Update test case result as Passed
            self.kiwi.update_test_case_result(
                test_run_id=self.test_run_id,
                test_case_id=4,  # Test case ID for this test
                status=4,  # 1 = Passed
                notes="Login with valid credentials succeeded."
            )
        except Exception as e:
            # Update test case result as Failed
            self.kiwi.update_test_case_result(
                test_run_id=self.test_run_id,
                test_case_id=4,
                status=5,  # 2 = Failed
                notes=f"Login with valid credentials failed: {e}"
            )
            raise

    @pytest.mark.order(2)
    def test_verify_dashboard(self):
        """Verify Dashboard text and update the result in Kiwi TCMS."""
        try:
            assert self.login_page.login_successful(), "Login failed!"

            # Update test case result as Passed
            self.kiwi.update_test_case_result(
                test_run_id=self.test_run_id,
                test_case_id=26,  # Test case ID for this test
                status=4,  # 1 = Passed
                notes="Dashboard verification succeeded."
            )
        except Exception as e:
            # Update test case result as Failed
            self.kiwi.update_test_case_result(
                test_run_id=self.test_run_id,
                test_case_id=26,
                status=5,  # 2 = Failed
                notes=f"Dashboard verification failed: {e}"
            )
            raise
