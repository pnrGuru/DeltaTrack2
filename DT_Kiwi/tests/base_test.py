from datetime import datetime

from DT_Kiwi.pages.ent_org_page import EntOrganizationPage
from DT_Kiwi.pages.organization_mypage import OrganizationnPage
from DT_Kiwi.tests.test_ent_org import TestEntOrganizations
from DT_Kiwi.utils.browser_utils import BrowserManager
from DT_Kiwi.utils.playwright_driver import PlaywrightDriver
from DT_Kiwi.utils.kiwi_tcms_integration import KiwiTCMSIntegration
from DT_Kiwi.utils.create_run_helper import create_test_run
from DT_Kiwi.pages.organizations_page import OrganizationPage

class BaseTest:
    @classmethod
    def setup_class(cls):
        """Common setup for all tests: browser, Playwright, Kiwi TCMS test run creation."""
        cls.browser_manager = BrowserManager()
        cls.page = cls.browser_manager.launch_browser()
        cls.driver = PlaywrightDriver(cls.page)
        cls.org_page = OrganizationnPage(cls.driver)
        cls.kiwi = KiwiTCMSIntegration()
        test_ent=TestEntOrganizations()

        # Define test run details (can be overridden in child classes)
        cls.product_name = "UBQ-UI-Testing"
        cls.version_name = "V1.1.0"
        cls.build_name = "UAT_Build"
        cls.plan_name = "UBQ Test"
        cls.case_ids = [26, 27, 28, 29, 30,4,5]

        # Create a reusable test run
        cls.test_run_id = create_test_run(
            cls.kiwi, cls.product_name, cls.version_name, cls.build_name, cls.plan_name, cls.case_ids
        )

    @classmethod
    def teardown_class(cls):
        """Common teardown for all tests: close the browser."""
        cls.browser_manager.close_browser()

    def update_test_result(self, test_case_id, status, notes):
        """Reusable function to update test results in Kiwi TCMS."""
        self.kiwi.update_test_case_result(
            test_run_id=self.test_run_id,
            test_case_id=test_case_id,
            status=status,
            notes=notes
        )
