

import pytest

from DT_Kiwi.pages.network_admin_page import NetworkUserPage
from DT_Kiwi.pages.organizations_page import OrganizationPage
from DT_Kiwi.utils.browser_utils import BrowserManager
from DT_Kiwi.utils.env_utils import URL, USERNAME, PASSWORD
from DT_Kiwi.utils.kiwi_tcms_integration import KiwiTCMSIntegration
from DT_Kiwi.utils.playwright_driver import PlaywrightDriver


@pytest.mark.order(1)
class TestNetworkUsers:
    @classmethod
    def setup_class(cls):
        """Set up browser, initialize page objects, and create a test run in Kiwi TCMS."""
        cls.browser_manager = BrowserManager()
        cls.page = cls.browser_manager.launch_browser()
        cls.driver = PlaywrightDriver(cls.page)  # Initialize PlaywrightDriver
        cls.org_page = OrganizationPage(cls.driver)
        cls.ui_network_page=NetworkUserPage(cls.driver)


    @classmethod
    def teardown_class(cls):
        cls.browser_manager.close_browser()

    @pytest.mark.order(1)
    def test_login_with_valid_credentials(self):
        """Test valid login and update the result in Kiwi TCMS."""
        self.org_page.navigate(URL)
        self.org_page.login(USERNAME, PASSWORD)

    def test_navigate_to_network_users(self):
        self.ui_network_page.navigate_to_network_users()







