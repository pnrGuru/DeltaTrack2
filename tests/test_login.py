def test_login_functionality(kiwi_setup):

    kiwi, run_id = kiwi_setup
    case_id = 26  # Replace with your test case ID

    # Example test logic
    try:
        assert True  # Simulating a successful test
        status = 1  # Pass
    except AssertionError:
        status = 2  # Fail

    # Update test result in Kiwi TCMS
    kiwi.update_test_case_result(run_id, case_id, status)



