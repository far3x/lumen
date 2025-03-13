# PTAP - Project To AI Prompt

**Effortlessly Generate AI Prompts from Your Code Projects for Enhanced AI Understanding**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/ptap.svg)](https://badge.fury.io/py/ptap)

PTAP (Project To AI Prompt) is a command-line tool designed to simplify the process of providing comprehensive context to AI models about your coding projects.  With PTAP, you can quickly generate a structured and informative prompt containing your project's file structure and code content, enabling AI to understand your codebase effectively.

## Why PTAP?

In the age of powerful AI models, leveraging them for code understanding, analysis, or generation is becoming increasingly valuable. However, effectively communicating the context of an entire coding project to an AI in a single prompt can be challenging and time-consuming.

**PTAP solves this problem by:**

*   **Automating Prompt Creation:**  No more manual copying and pasting of file paths and code snippets. PTAP does it all for you.
*   **Structured Context:**  PTAP generates a well-structured prompt that includes:
    *   A JSON representation of your project's directory hierarchy.
    *   The content of your source code files.
    *   Clear file titles (optional) to indicate file paths.
*   **Offline & Secure:**  Unlike online tools that may require uploading your code, PTAP runs locally on your machine, ensuring the privacy and security of your projects.
*   **Customizable:** Tailor the generated prompt to your needs by excluding specific folders, customizing the introduction text, and controlling the inclusion of file titles.
*   **Efficiency:**  Quickly prepare project context for AI interactions, saving you valuable time and effort.

**Currently, there isn't a readily available online tool specifically designed to structure a coding project into an AI prompt like PTAP does.** PTAP fills this gap, providing a focused and efficient solution for developers looking to leverage AI for code-related tasks.

## Limitations

While PTAP is a powerful tool, it's important to be aware of potential limitations:

*   **AI Input Length Limits:**  Some AI models have limitations on the maximum input length they can process. For very large projects, the generated prompt might exceed these limits and could be truncated by the AI, potentially affecting its understanding.
*   **Large Projects & Performance:**  For extremely large projects with thousands of files, PTAP might take a noticeable amount of time to process and generate the prompt. We are actively working on performance optimizations for future updates.
*   **File Readability:** PTAP is designed to read plain text code files. Certain file formats, such as `.ipynb` (Jupyter Notebooks) or binary files, may not be directly readable as text and their content might not be accurately included in the generated prompt.  Support for more file types may be added in future versions.
*   **AI Interpretation Variability:**  The effectiveness of the generated prompt depends on the specific AI model being used and its ability to interpret structured text and code context. Different AI models may have varying levels of understanding.
*   **Potential Edge Cases:**  While PTAP is designed to handle various project structures and file types, there might be unforeseen edge cases or project configurations where it may not function perfectly. Please report any issues you encounter!
*   **Ongoing Development:** PTAP is under active development, and we are committed to continuously improving its performance, features, and user experience. Stay tuned for future updates and enhancements!

## Installation

You can easily install PTAP using pip:

`pip install ptap`

Ensure you have Python 3.7 or later installed on your system.

## Functionalities & Usage Examples

PTAP is a command-line tool accessible via the `ptap` command in your terminal.

**Basic Usage (Current Directory, Clipboard Output):**

In your project's root directory, simply run:

`ptap`

This will:

1.  Analyze your current directory as the project root.
2.  Generate a structured AI prompt.
3.  Copy the prompt to your clipboard, ready to be pasted into your AI of choice.

**Specify a Project Path:**

To process a project located at a different path, provide the path as an argument:

`ptap folder1/folder2/pathtoproject`

**Output to a Text File:**

To save the generated prompt to a `.txt` file in your project's root directory, use the `-t` or `--txt` option followed by the desired filename (without the `.txt` extension):

`ptap -t project_prompt`

This will create a file named `project_prompt.txt` in your project's root.

**Open Configuration File:**

To customize PTAP's settings, open the configuration file using the `-c` or `--configure` option:

`ptap -c`

This will open the `config.json` file in your default code editor, allowing you to modify settings like skipped folders, intro text, and title format. The configuration file is located in `~/.ptap/config.json` (in your user's home directory).

**Reset Configuration to Default:**

To revert all settings back to their original defaults, use the `-r` or `--reset` option:

`ptap -r`

**Hide Elements in the Prompt:**

You can selectively hide elements from the generated prompt using the `-hd` or `--hide` option.  Specify elements to hide as a comma-separated list:

*   **Hide the introduction text:**

    `ptap -hd intro`

*   **Hide file titles (not recommended for AI understanding):**

    `ptap -hd title`

*   **Hide both intro and titles:**

    `ptap -hd intro,title`

**Configuration Options:**

The `config.json` file allows you to customize the following:

*   `intro_text`:  The introductory text added at the beginning of the prompt.
*   `show_intro`:  Boolean to control whether the intro text is included.
*   `title_text`:  The format for file titles (e.g., "--- {file} ---").
*   `show_title`: Boolean to control whether file titles are included.
*   `skipped_folders`:  A list of folder names to be excluded from project analysis (e.g., `.git`, `__pycache__`, `node_modules`).
*   `allowed_files` (in `ptap/file_reader.py`): You can modify the `allowed_files` list in `ptap/file_reader.py` to include or exclude specific file extensions that PTAP will process.

## License

PTAP is distributed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

If you want to contribute, do not hesitate ! Feedback is also needed, especially if you use any OS that is not Windows, since the module was not tested on other OS's yet.

If you encounter any issues, have feature requests, or would like to contribute to PTAP, please feel free to open an issue or submit a pull request on the [GitHub repository](https://github.com/Far3000-YT/PTAP).

## Author

Developed by Far3k ([GitHub Profile](https://github.com/Far3000-YT)) - Mail: far3000yt@gmail.com - Discord: @far3000 - X: @0xFar3000

---

**Start leveraging AI to understand your code projects better with PTAP!**
