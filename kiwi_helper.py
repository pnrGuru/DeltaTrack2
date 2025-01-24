import requests
import json
from datetime import datetime
from config import KIWI_URL, USERNAME, PASSWORD, MANAGER_ID


class KiwiHelper:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})
        self.authenticated = False

    def login(self):
        """Log in to Kiwi TCMS and establish a session."""
        payload = {
            "jsonrpc": "2.0",
            "method": "Auth.login",
            "params": {"username": USERNAME, "password": PASSWORD},
            "id": 1,
        }
        response = self.session.post(KIWI_URL, data=json.dumps(payload))
        response_data = response.json()

        if "result" in response_data:
            self.authenticated = True
            print(f"[INFO] Successfully logged into Kiwi TCMS as {USERNAME}")
        else:
            raise Exception(f"Login failed: {response_data.get('error', {}).get('message', 'Unknown error')}")

    def create_test_run(self, plan_id, build_id):
        """Create a new test run dynamically."""
        if not self.authenticated:
            raise Exception("Not authenticated. Please log in first.")

        today = datetime.now().strftime("%Y-%m-%d")
        summary = f"Test Run - {today}"  # Dynamic summary with today's date

        payload = {
            "jsonrpc": "2.0",
            "method": "TestRun.create",
            "params": {
                "values": {
                    "summary": summary,
                    "plan": plan_id,
                    "build": build_id,
                    "manager": MANAGER_ID,
                    "environment": [],
                }
            },
            "id": 1,
        }
        response = self.session.post(KIWI_URL, data=json.dumps(payload))
        response_data = response.json()

        if "result" in response_data:
            run_id = response_data["result"]["id"]
            print(f"[INFO] Test Run '{summary}' created with ID: {run_id}")
            return run_id
        else:
            raise Exception(f"Failed to create test run: {response_data['error']['message']}")

    def add_test_case_to_run(self, run_id, case_ids):
        """Add test cases to the test run."""
        # Ensure case_ids is a list
        if not isinstance(case_ids, list):
            case_ids = [case_ids]

        payload = {
            "jsonrpc": "2.0",
            "method": "TestRun.add_case",
            "params": {
                "run_id": run_id,
                "case_ids": case_ids,  # Now always a list
            },
            "id": 1,
        }

        response = self.session.post(KIWI_URL, data=json.dumps(payload))
        response_data = response.json()

        if "result" in response_data:
            print(f"[INFO] Test cases {case_ids} added to test run {run_id}.")
        else:
            raise Exception(f"Failed to add test cases: {response_data['error']['message']}")

    def update_test_case_result(self, run_id, case_id, status, notes="Automated execution result"):
        """Update the result of a test case."""
        payload = {
            "jsonrpc": "2.0",
            "method": "TestExecution.update",
            "params": {
                "run_id": run_id,
                "case_id": case_id,
                "status": status,  # 1 for pass, 2 for fail, etc.
                "notes": notes,
            },
            "id": 1,
        }
        response = self.session.post(KIWI_URL, data=json.dumps(payload))
        response_data = response.json()

        if "result" in response_data:
            print(f"[INFO] Test case {case_id} result updated to status {status}.")
        else:
            raise Exception(f"Failed to update test case result: {response_data['error']['message']}")
