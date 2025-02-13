from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Extract application-related variables from the environment
URL = os.getenv("URL")
BROWSER = os.getenv("BROWSER", "chromium").strip().lower()  # Default to Chromium if not specified
USERNAME = os.getenv("UBQUSERNAME")
PASSWORD = os.getenv("UBQPASSWORD")
HEADLESS = os.getenv("HEADLESS", "False").strip().lower() == "true"  # Convert to boolean

# Extract Kiwi TCMS-related variables from the environment
TCMS_API_USERNAME = os.getenv("TCMS_API_USERNAME")
TCMS_API_PASSWORD = os.getenv("TCMS_API_PASSWORD")
TCMS_API_URL = os.getenv("TCMS_API_URL")

# Extract logging and debugging-related variables
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").strip().upper()
