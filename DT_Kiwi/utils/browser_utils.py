import logging
from playwright.sync_api import sync_playwright

from DT_Kiwi.utils.env_utils import BROWSER, HEADLESS

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BrowserManager:
    def __init__(self, browser_name=None, headless=None, maximize=True ,viewport_width=1280, viewport_height=1280):
        # Use values from .env if parameters are not provided
        self.browser_name = browser_name or BROWSER
        self.headless = headless if headless is not None else HEADLESS
        self.maximize = maximize
        self.viewport_width = viewport_width
        self.viewport_height = viewport_height
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None

    def launch_browser(self):
        """Launch the browser, create a context, and return a page instance."""
        self.playwright = sync_playwright().start()

        # Resolve the browser type
        if self.browser_name == "chromium":
            browser_type = self.playwright.chromium
        elif self.browser_name == "firefox":
            browser_type = self.playwright.firefox
        elif self.browser_name == "webkit":
            browser_type = self.playwright.webkit
        else:
            raise ValueError(
                f"Unsupported browser: {self.browser_name}. Supported browsers are 'chromium', 'firefox', 'webkit'."
            )

        logger.info(f"Launching browser: {self.browser_name}, Headless: {self.headless}, Maximize: {self.maximize}")

        # Launch the browser
        self.browser = browser_type.launch(headless=self.headless)

        # Maximize window by using no_viewport=True
        if self.maximize:
            self.context = self.browser.new_context(no_viewport=True)
        else:
            self.context = self.browser.new_context(viewport={"width": 1280, "height": 1280})

        self.page = self.context.new_page()

        # Set zoom level to 100% (optional)
        self.page.evaluate("document.body.style.zoom = '100%'")

        return self.page

    def close_browser(self):
        """Close the page, context, and browser, and stop Playwright."""
        if self.page and not self.page.is_closed():
            self.page.close()
        if self.context:
            self.context.close()
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()
