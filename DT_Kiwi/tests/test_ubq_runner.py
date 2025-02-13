import pytest
import os


def run_tests():
    """
    Dynamically discover and execute all tests in the 'tests' folder.
    """
    # Define the base test folder dynamically
    test_folder = os.path.join(os.getcwd(), "tests")

    # Ensure the test folder exists
    if not os.path.exists(test_folder):
        print(f"Test folder not found: {test_folder}")
        return

    # Pytest arguments for dynamic test discovery and reporting
    pytest_args = [
        test_folder,  # Discover tests in the 'tests' folder
        "-v",  # Verbose output
        "--tb=short",  # Short traceback format
        "--junitxml=reports/ubq_test_results.xml",  # Generate JUnit XML report
        "--maxfail=3",  # Stop after 3 failures (optional)
    ]

    print(f"Running tests dynamically from folder: {test_folder}")

    # Execute pytest with the defined arguments
    pytest.main(pytest_args)


if __name__ == "__main__":
    run_tests()
