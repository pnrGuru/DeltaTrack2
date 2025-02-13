import pytest


def run_tests():
    """
    Execute test classes in priority order.
    """
    # List test classes in order of priority
    test_classes = [
        # "tests/test_networkadmin.py::TestLogin",
       # "tests/test_organizations.py::TestOrganizations",
        "tests/test_ent_org.py::TestSubOrganizations"




    ]

    # Build pytest arguments dynamically
    pytest_args = [
                      "-v",  # Verbose output
                      "--tb=short",  # Short traceback format
                  ] + test_classes

    # Execute pytest with the arguments
    pytest.main(pytest_args)


if __name__ == "__main__":
    run_tests()
