import pytest

from DT_Kiwi.pages.ent_org_page import EntOrganizationPage
from DT_Kiwi.utils.browser_utils import BrowserManager
from DT_Kiwi.utils.kiwi_tcms_integration import KiwiTCMSIntegration
from DT_Kiwi.utils.playwright_driver import PlaywrightDriver
from DT_Kiwi.utils.env_utils import URL, USERNAME, PASSWORD


@pytest.mark.order(1)
class UserGroups:
    @classmethod
    def setup_class(cls):
        """Set up browser, initialize page objects, and create a test run in Kiwi TCMS."""
        cls.browser_manager = BrowserManager()
        cls.page = cls.browser_manager.launch_browser()
        cls.driver = PlaywrightDriver(cls.page)  # Initialize PlaywrightDriver
        cls.ent_page=EntOrganizationPage(cls.driver)


    @classmethod
    #commit
    def teardown_class(cls):
        cls.browser_manager.close_browser()

