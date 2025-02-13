import logging
from tcms_api.xmlrpc import TCMSXmlrpc

from DT_Kiwi.utils.env_utils import TCMS_API_USERNAME, TCMS_API_PASSWORD, TCMS_API_URL


class KiwiTCMSIntegration:
    def __init__(self):
        """Initialize the Kiwi TCMS integration."""
        try:
            if not TCMS_API_USERNAME or not TCMS_API_PASSWORD or not TCMS_API_URL:
                raise ValueError("Kiwi TCMS credentials or API URL are missing in environment variables.")

            # Initialize the TCMS client
            self.client = TCMSXmlrpc(
                username=TCMS_API_USERNAME,
                password=TCMS_API_PASSWORD,
                url=TCMS_API_URL
            ).server

            logging.info("Successfully authenticated with Kiwi TCMS.")
        except ValueError as e:
            self.log_error_details(e)
            raise
        except Exception as e:
            self.log_error_details(e)
            raise

    @staticmethod
    def log_error_details(error):
        """Log error details for debugging."""
        logging.error(f"Error Type: {type(error)}")
        logging.error(f"Error Details: {error}")

    def get_id(self, object_name, filter_criteria):
        """Fetch an object ID from Kiwi TCMS based on filter criteria."""
        try:
            obj_list = getattr(self.client, object_name).filter(filter_criteria)
            if not obj_list:
                raise ValueError(f"No {object_name} found matching criteria: {filter_criteria}")
            return obj_list[0]['id']
        except Exception as e:
            self.log_error_details(e)
            raise

    def create_test_run(self, name, product_name, version_name, build_name, plan_name, case_ids,
                        summary="Automated Test Run"):
        """Create a new test run in Kiwi TCMS."""
        try:
            logging.info("Fetching Product ID...")
            product_id = self.get_id("Product", {"name": product_name})
            logging.info(f"Product ID: {product_id}")

            logging.info("Fetching Version ID...")
            version_id = self.get_id("Version", {"product": product_id, "value": version_name})
            logging.info(f"Version ID: {version_id}")

            logging.info("Fetching Build ID...")
            build_id = self.get_id("Build", {"version": version_id, "name": build_name})
            logging.info(f"Build ID: {build_id}")

            logging.info("Fetching Plan ID...")
            plan_id = self.get_id("TestPlan", {"product": product_id, "name": plan_name})
            logging.info(f"Plan ID: {plan_id}")

            logging.info("Creating Test Run...")
            test_run = self.client.TestRun.create({
                'name': name,
                'plan': plan_id,
                'build': build_id,
                'case_list': case_ids,
                'manager': TCMS_API_USERNAME,
                'summary': summary,
            })
            logging.info(f"Test Run created: {test_run}")
            return test_run
        except Exception as e:
            self.log_error_details(e)
            raise

    def ensure_test_execution(self, test_run_id, test_case_id):
        """Ensure a TestExecution exists for a test case in a test run."""
        try:
            # Check if TestExecution exists
            executions = self.client.TestExecution.filter({'run': test_run_id, 'case': test_case_id})
            if executions:
                logging.info(f"Found execution for test case {test_case_id} in test run {test_run_id}.")
                return executions[0]['id']

            # Add the test case to the test run
            logging.info(f"Adding test case {test_case_id} to test run {test_run_id}.")
            # Pass the case ID as an integer (not a list)
            self.client.TestRun.add_case(test_run_id, test_case_id)

            # Recheck for executions after adding the case
            executions = self.client.TestExecution.filter({'run': test_run_id, 'case': test_case_id})
            if executions:
                logging.info(
                    f"Execution created for test case {test_case_id} in test run {test_run_id} after adding the case.")
                return executions[0]['id']

            # Log an error if TestExecution is still not created
            logging.error(f"Failed to create TestExecution for test case {test_case_id} in test run {test_run_id}.")
            raise RuntimeError(f"TestExecution not created for test case {test_case_id} in test run {test_run_id}.")
        except Exception as e:
            self.log_error_details(e)
            raise

    def update_test_case_result(self, test_run_id, test_case_id, status, notes=None):
        """Update the result of a test case in a test run."""
        try:
            # Ensure TestExecution exists
            execution_id = self.ensure_test_execution(test_run_id, test_case_id)

            # Update the execution if it exists
            self.client.TestExecution.update(
                execution_id,
                {
                    'status': status,
                    'notes': notes or ""
                }
            )
            logging.info(
                f"Updated execution for test case {test_case_id} in test run {test_run_id} with status {status}.")
        except Exception as e:
            self.log_error_details(e)
            raise

    def get_test_execution_methods(self):
        """Log available methods for TestExecution."""
        try:
            methods = dir(self.client.TestExecution)
            logging.info(f"Available methods for TestExecution: {methods}")
            return methods
        except Exception as e:
            self.log_error_details(e)
            raise

    def list_methods(self):
        """List all available methods on the server."""
        try:
            methods = self.client.system.listMethods()
            logging.info(f"Available methods: {methods}")
            return methods
        except Exception as e:
            self.log_error_details(e)
            raise

    def get_available_methods(self):
        """Fetch and log all available methods from the Kiwi TCMS server."""
        try:
            logging.info("Fetching available methods from the server.")
            methods = dir(self.client)
            logging.info(f"Available methods: {methods}")
            return methods
        except Exception as e:
            self.log_error_details(e)
            raise
