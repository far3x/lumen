import re
import os
import tempfile
from pygments import lex
from pygments.lexers import get_lexer_for_filename, guess_lexer
from pygments.token import Comment
from pygments.util import ClassNotFound
from detect_secrets.core.secrets_collection import SecretsCollection
# --- FIX: Import the settings context manager from the documentation ---
from detect_secrets.settings import default_settings

def remove_comments(content: str, filename: str) -> str:
    """Removes comments from code using the pygments library."""
    try:
        lexer = get_lexer_for_filename(filename, stripall=True)
    except ClassNotFound:
        try:
            lexer = guess_lexer(content, stripall=True)
        except ClassNotFound:
            return content
    tokens = lex(content, lexer)
    return "".join(token[1] for token in tokens if not token[0] in Comment)

def remove_secrets_and_pii(content: str, filename: str) -> str:
    """
    Scans content for secrets using detect_secrets and redacts them.
    Also removes common PII patterns like emails and IP addresses.
    """
    sanitized_content = content
    tmp_filepath = None

    try:
        with tempfile.NamedTemporaryFile(
            mode='w+',
            delete=False,
            suffix=os.path.splitext(filename)[1],
            encoding='utf-8'
        ) as tmp_file:
            tmp_file.write(content)
            tmp_filepath = tmp_file.name

        secrets = SecretsCollection()

        # --- FIX: Use the 'default_settings' context manager as per the docs ---
        # This automatically loads the default plugins for the duration of the 'with' block.
        with default_settings():
            # Use scan_file for a single file path
            secrets.scan_file(tmp_filepath)
        # --- END OF FIX ---

        if tmp_filepath in secrets:
            for secret in secrets[tmp_filepath]:
                sanitized_content = sanitized_content.replace(
                    secret.secret_value,
                    f"REDACTED_{secret.type.upper()}"
                )

    finally:
        if tmp_filepath and os.path.exists(tmp_filepath):
            os.unlink(tmp_filepath)

    sanitized_content = re.sub(r'[\w\.-]+@[\w\.-]+\.[\w]+', 'REDACTED_EMAIL', sanitized_content)
    sanitized_content = re.sub(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', 'REDACTED_IP', sanitized_content)

    return sanitized_content

def sanitize_code(content: str, filename: str) -> str:
    """
    A pipeline function to fully sanitize a string of code.
    1. Removes comments.
    2. Removes secrets and PII.
    3. Cleans up excessive whitespace.
    """
    if not content or not isinstance(content, str):
        return ""

    uncommented_code = remove_comments(content, filename)
    sanitized_code = remove_secrets_and_pii(uncommented_code, filename)

    sanitized_code = re.sub(r'\n\s*\n', '\n\n', sanitized_code).strip()

    return sanitized_code