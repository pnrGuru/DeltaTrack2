from datetime import datetime


def create_test_run(kiwi, product_name, version_name, build_name, plan_name, case_ids):
    """Reusable function to create a test run and return its ID."""
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    test_run = kiwi.create_test_run(
        name="Automated Test Run",
        product_name=product_name,
        version_name=version_name,
        build_name=build_name,
        plan_name=plan_name,
        case_ids=case_ids,
        summary=f"Automated test run on {current_datetime}"
    )
    return test_run["id"]
