import traceback
import pytest
from DT_Kiwi.utils.env_utils import URL, USERNAME, PASSWORD
from DT_Kiwi.tests.base_test import BaseTest  # Importing the base class


@pytest.mark.order(1)
class TestSubOrganizationsW(BaseTest):
    @pytest.mark.order(1)
    def test_login_with_valid_credentials(self):
        """Test valid login and update the result in Kiwi TCMS with failure details."""
        try:
            self.org_page.navigate(URL)
            self.org_page.login(USERNAME, PASSWORD)

            # Mark as Passed in Kiwi TCMS
            self.update_test_result(test_case_id=5, status=4, notes="Login successful.")
        except Exception as e:
            error_message = str(e)  # Capture error message
            stack_trace = traceback.format_exc()  # Get full stack trace

            # Mark as Failed in Kiwi TCMS with error details
            self.update_test_result(
                test_case_id=5,
                status=5,  # 5 = Failed
                notes=f"Login failed!\nError: {error_message}\nStack Trace:\n{stack_trace}"
            )
            raise  # Re-raise for debugging

    @pytest.mark.order(2)
    def test_verify_dashboard(self):
        """Verify Dashboard text and update the result in Kiwi TCMS with failure details."""
        try:
            assert self.org_page.login_successful(), "Login failed!"

            # Mark as Passed in Kiwi TCMS
            self.update_test_result(test_case_id=4, status=4, notes="Dashboard verification successful.")
        except Exception as e:
            error_message = str(e)
            stack_trace = traceback.format_exc()

            # Mark as Failed in Kiwi TCMS with full details
            self.update_test_result(
                test_case_id=4,
                status=5,
                notes=f"Dashboard verification failed!\nError: {error_message}\nStack Trace:\n{stack_trace}"
            )
            raise
    def test_navigate(self):
        try:
            assert self.test

            # Mark as Passed in Kiwi TCMS
            self.update_test_result(test_case_id=4, status=4, notes="Dashboard verification successful.")
        except Exception as e:
            error_message = str(e)
            stack_trace = traceback.format_exc()

            # Mark as Failed in Kiwi TCMS with full details
            self.update_test_result(
                test_case_id=4,
                status=5,
                notes=f"Dashboard verification failed!\nError: {error_message}\nStack Trace:\n{stack_trace}"
            )
            raise

