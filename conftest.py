import pytest
from kiwi_helper import KiwiHelper
from config import TEST_PLAN_ID, BUILD_ID, TEST_CASE_IDS


@pytest.fixture(scope="session", autouse=True)
def kiwi_setup():
    """Set up Kiwi TCMS connection and test run."""
    kiwi = KiwiHelper()

    # Log in to Kiwi TCMS
    kiwi.login()

    # Create a new test run
    run_id = kiwi.create_test_run(TEST_PLAN_ID, BUILD_ID)

    # Add test cases to the test run
    kiwi.add_test_case_to_run(run_id, TEST_CASE_IDS)

    # Yield kiwi instance and run ID for tests
    yield kiwi, run_id