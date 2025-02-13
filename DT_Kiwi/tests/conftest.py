import pytest

from DT_Kiwi.utils.browser_utils import BrowserManager
from DT_Kiwi.utils.env_utils import BROWSER, HEADLESS


@pytest.fixture(scope="class")  # Use 'class' scope to share across all tests in a class
#@pytest.fixture(scope="session")
def browser_manager():
    """Launch the browser session-wide."""
    manager = BrowserManager(BROWSER, HEADLESS)
    browser = manager.launch_browser()
    yield browser
    manager.close_browser()  # Ensure cleanup is done at the end of the session


@pytest.fixture(scope="function")
def page(browser_manager):
    """Create a new browser context and page for each test."""
    context = browser_manager.new_context()
    page = context.new_page()
    yield page
    page.close()  # Close the page after the test
    context.close()  # Close the context after the test
