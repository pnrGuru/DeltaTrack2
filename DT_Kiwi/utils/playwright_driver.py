import logging
from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class PlaywrightDriver:
    def __init__(self, page: Page):
        """Initialize the Playwright driver with a page instance."""
        self.page = page

    def navigate_to(self, url: str):
        """Navigate to the given URL."""
        try:
            logging.info(f"Navigating to URL: {url}")
            self.page.goto(url, timeout=30000)  # 30 seconds timeout
            logging.info(f"Successfully navigated to URL: {url}")
        except PlaywrightTimeoutError as e:
            logging.error(f"Timeout while navigating to URL: {url}")
            raise Exception(f"Timeout while navigating to URL: {url}") from e

    def click_element(self, selector: str):
        """Click an element identified by the selector."""
        try:
            logging.info(f"Clicking element with selector: {selector}")
            self.page.wait_for_selector(selector, state="visible", timeout=15000)
            self.page.click(selector)
            logging.info(f"Successfully clicked element with selector: {selector}")
        except PlaywrightTimeoutError as e:
            logging.error(f"Timeout waiting for element to be clickable: {selector}")
            raise Exception(f"Timeout waiting for element to be clickable: {selector}") from e

    def fill_textbox(self, selector: str, text: str):
        """Fill a textbox identified by the selector with the given text."""
        try:
            logging.info(f"Filling textbox {selector} with text: {text}")
            self.page.wait_for_selector(selector, state="visible", timeout=15000)
            self.page.fill(selector, text)
            logging.info(f"Successfully filled textbox {selector} with text: {text}")
        except PlaywrightTimeoutError as e:
            logging.error(f"Timeout waiting for textbox: {selector}")
            raise Exception(f"Timeout waiting for textbox: {selector}") from e

    def is_element_visible(self, selector: str) -> bool:
        """Check if an element identified by the selector is visible."""
        try:
            logging.info(f"Checking visibility of element {selector}")
            self.page.wait_for_selector(selector, state="visible", timeout=15000)
            logging.info(f"Element {selector} is visible.")
            return True
        except PlaywrightTimeoutError:
            logging.error(f"Timeout waiting for element to be visible: {selector}")
            return False

    def clear_textbox(self, selector: str):
        """
        Clear the content of a textbox identified by the selector.

        :param selector: The CSS/XPath selector for the textbox.
        """
        try:
            logging.info(f"Clearing textbox {selector}")

            # Wait for the textbox to be visible
            self.page.wait_for_selector(selector, state="visible", timeout=15000)

            # Clear the content of the textbox
            self.page.fill(selector, "")

            logging.info(f"Successfully cleared textbox {selector}")
        except PlaywrightTimeoutError as e:
            logging.error(f"Timeout waiting for textbox: {selector}")
            raise Exception(f"Timeout waiting for textbox: {selector}") from e

    def get_text(self, locator: str) -> str:
        """Returns the inner text of the specified element."""
        return self.page.locator(locator).inner_text().strip()

    def wait_for_table(self, table_selector: str, timeout: int = 15000):
        """
        Wait for the table to be visible and loaded.

        :param table_selector: The CSS or XPath selector for the table.
        :param timeout: The maximum time to wait for the table (in milliseconds).
        """
        try:
            logging.info(f"Waiting for table with selector: {table_selector}")
            self.page.wait_for_selector(table_selector, state="visible", timeout=timeout)
            logging.info(f"Table with selector {table_selector} is visible.")
        except PlaywrightTimeoutError:
            logging.error(f"Timeout waiting for table with selector: {table_selector}")
            raise Exception(f"Timeout waiting for table with selector: {table_selector}")

    def press_enter(self, selector: str):
        """
        Press the "Enter" key on the specified element.

        :param selector: The CSS or XPath selector for the element.
        """
        try:
            logging.info(f"Pressing Enter on element with selector: {selector}")
            self.page.press(selector, "Enter")
            logging.info(f"Pressed Enter on element with selector: {selector}")
        except Exception as e:
            logging.error(f"Failed to press Enter on element with selector: {selector}. Error: {str(e)}")
            raise e

    def check_checkbox(self, selector: str):
        """
        Check a checkbox identified by the selector.

        :param selector: The CSS or XPath selector for the checkbox.
        """
        try:
            logging.info(f"Checking checkbox with selector: {selector}")

            # Wait for the checkbox to be visible
            self.page.wait_for_selector(selector, state="visible", timeout=15000)

            # Check the checkbox
            self.page.check(selector)

            logging.info(f"Successfully checked checkbox with selector: {selector}")
        except PlaywrightTimeoutError as e:
            logging.error(f"Timeout waiting for checkbox with selector: {selector}")
            raise Exception(f"Timeout waiting for checkbox with selector: {selector}") from e
        except Exception as e:
            logging.error(f"Failed to check checkbox with selector: {selector}. Error: {str(e)}")
            raise e

    def get_element_text(self, selector: str) -> str:
        """
        Get the text content of an element.

        :param selector: The CSS or XPath selector of the element.
        :return: The text content of the element.
        """
        try:
            logging.info(f"Fetching text for element with selector: {selector}")

            # Wait for the element to be visible
            self.page.wait_for_selector(selector, state="visible", timeout=15000)

            # Get the text content
            element_text = self.page.text_content(selector)

            logging.info(f"Successfully fetched text: {element_text}")
            return element_text.strip() if element_text else ""

        except PlaywrightTimeoutError as e:
            logging.error(f"Timeout waiting for element with selector: {selector}")
            raise Exception(f"Timeout waiting for element with selector: {selector}") from e
        except Exception as e:
            logging.error(f"Failed to fetch text for selector: {selector}. Error: {str(e)}")
            raise e

    def scroll_to_element(self, selector: str):
        """Scroll to an element identified by the selector."""
        try:
            logging.info(f"Scrolling to element with selector: {selector}")
            element = self.page.locator(selector)
            element.scroll_into_view_if_needed(timeout=15000)
            logging.info(f"Successfully scrolled to element with selector: {selector}")
        except PlaywrightTimeoutError as e:
            logging.error(f"Timeout waiting for element to scroll into view: {selector}")
            raise Exception(f"Timeout waiting for element to scroll into view: {selector}") from e

    def scroll_to_bottom(self):
        """Scroll to the bottom of the page."""
        try:
            logging.info("Scrolling to the bottom of the page")
            self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            logging.info("Successfully scrolled to the bottom of the page")
        except Exception as e:
            logging.error("Failed to scroll to the bottom of the page")
            raise Exception("Failed to scroll to the bottom of the page") from e

    def hover_over_element(self, selector: str):
        """Hover over an element identified by the selector."""
        try:
            logging.info(f"Hovering over element with selector: {selector}")
            self.page.locator(selector).hover(timeout=15000)
            logging.info(f"Successfully hovered over element with selector: {selector}")
        except PlaywrightTimeoutError as e:
            logging.error(f"Timeout waiting to hover over element: {selector}")
            raise Exception(f"Timeout waiting to hover over element: {selector}") from e
        except Exception as e:
            logging.error(f"Failed to hover over element with selector: {selector}. Error: {str(e)}")
            raise e


