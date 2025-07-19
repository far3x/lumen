#made with ai btw :3 (just need to see if the basics work)

import os
import sys
import textwrap

# Add the project root to the path to allow importing 'lum'
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from lum.data import sanitize_code

# --- Test Data Embedded in Code ---
# This string contains multiple types of secrets and PII
# to test the sanitization process thoroughly.
original_code_with_secrets = textwrap.dedent("""
    # Test plan written by test_user@my-company.com
    # For support, call the dev team at 800-555-0199.
    
    import requests
    
    # 1. Test a realistic (but fake) AWS key in code.
    #    This should be redacted.
    aws_access_key = "AKIAQWERTYUIOPASDFGH"
    
    class ApiClient:
        def __init__(self):
            # 2. Test a secret inside a comment. This line will be removed
            #    by the comment stripper before the scanner sees it.
            #    API_TOKEN = "ghp_aBcDeFgHiJkLmNoPqRsTuVwXyZaBcDeFgHiJkL"
            self.base_url = "https://api.internal.service:9200"
            self.server_ip = "192.168.1.101"
            
        def get_data(self):
            # 3. Test a high-entropy password in a default argument.
            response = requests.get(self.base_url, auth=("admin", "Str0ngP@ssw0rd!"))
            return response.json()

    if __name__ == "__main__":
        print("Running services...")
""")

if __name__ == "__main__":
    print("="*80)
    print("--- Running Full Sanitization Test ---")
    print("="*80)

    print("\n--- ORIGINAL CONTENT ---\n")
    print(original_code_with_secrets)
    
    print("\n" + "="*80)
    print("--- SANITIZING NOW ---")
    print("="*80 + "\n")

    # The core of the test: run the sanitization function
    # The 'filename' argument is no longer needed.
    sanitized_content = sanitize_code(original_code_with_secrets)

    print("\n--- SANITIZED CONTENT ---\n")
    print(sanitized_content)

    print("\n" + "="*80)
    print("--- VERIFICATION ---")
    print("="*80)
    
    # Assertions to programmatically check if redaction was successful
    # PII Checks
    assert "test_user@my-company.com" not in sanitized_content, "PII (email in comment) was not removed!"
    assert "800-555-0199" not in sanitized_content, "PII (phone number in comment) was not removed!"
    assert "192.168.1.101" not in sanitized_content, "PII (IP address) was not removed!"
    print("✅ PII Redaction: PASSED")

    # Secret Checks
    assert "AKIAQWERTYUIOPASDFGH" not in sanitized_content, "Secret (AWS Key) was not removed!"
    assert "ghp_aBcDeFgHiJkLmNoPqRsTuVwXyZaBcDeFgHiJkL" not in sanitized_content, "Secret (GitHub token in comment) was not removed!"
    assert "Str0ngP@ssw0rd!" not in sanitized_content, "Secret (Hardcoded password) was not removed!"
    print("✅ Secret Redaction: PASSED")
    
    print("\nSUCCESS: All sensitive data appears to be correctly redacted.")