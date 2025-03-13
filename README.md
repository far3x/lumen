#   PTAP - Project To AI Prompt

**Effortlessly Prepare Your Code Projects for AI Analysis**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/ptap.svg)](https://badge.fury.io/py/ptap)

Tired of manually crafting prompts for AI to understand your code? PTAP automates the process, generating structured prompts that include your project's file structure and code content. Give your AI the complete context it needs with PTAP.

##   Why Use PTAP?

AI is powerful for code analysis, but it needs context. Manually providing that context is time-consuming and error-prone.

**PTAP solves this by:**

* **Automating Prompt Generation:** PTAP handles the tedious work of gathering file paths and code.
* **Providing Structured Context:** Prompts include a clear JSON representation of your project's structure and file content.
* **Ensuring Privacy and Security:** PTAP runs locally, so your code never leaves your machine.
* **Offering Customization:** Tailor prompts by excluding folders, adding custom introductions, and controlling file title inclusion.
* **Boosting Efficiency:** Quickly prepare project context, saving you time and effort.

**PTAP fills a crucial gap: there's no easy way to give AI comprehensive project context. It streamlines the workflow for any developer using AI for code-related tasks.**

##   Installation

Ensure you have Python 3.7+ installed. Then, install PTAP using pip:

```bash
pip install ptap
```

##   Usage

PTAP is a command-line tool. Here are the key commands:

**1. Basic Usage (Current Directory, Clipboard):**

```bash
ptap
```

* Analyzes the current directory.
* Generates an AI prompt.
* Copies the prompt to your clipboard.

**2. Specify a Project Path:**

```bash
ptap folder1/folder2/pathtoproject
```

**3. Output to a Text File:**

```bash
ptap -t project_prompt
```

* Saves the prompt to `project_prompt.txt` in the project root.

**4. Open Configuration File:**

```bash
ptap -c
```

* Opens `config.json` (located in `~/.ptap/config.json`) for customization.

**5. Reset Configuration to Default:**

```bash
ptap -r
```

**6. Hide Elements in the Prompt:**

* Hide introduction text:

    ```bash
    ptap -hd intro
    ```

* Hide file titles:

    ```bash
    ptap -hd title
    ```

* Hide both:

    ```bash
    ptap -hd intro,title
    ```

##   Configuration Options (in `config.json`)

* `intro_text`: Introductory text at the beginning of the prompt.
* `show_intro`: Boolean to show/hide the intro text.
* `title_text`: Format for file titles (e.g., "--- {file} ---").
* `show_title`: Boolean to show/hide file titles.
* `skipped_folders`: List of folders to exclude (e.g., `.git`, `__pycache__`).
* `allowed_files` (in `ptap/file_reader.py`): List of file extensions to include/exclude.

##   Limitations

* **AI Input Limits:** Large projects may generate prompts that exceed AI input limits.
* **Large Project Performance:** Processing very large projects can take time.
* **File Readability:** PTAP is designed for text-based code files.
* **AI Interpretation:** AI understanding of the prompt can vary.
* **Edge Cases:** Unexpected project structures may cause issues.
* **Ongoing Development:** PTAP is actively being improved.

##   License

PTAP is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

##   Contributing

Contributions are welcome! Please report issues or submit pull requests on the [GitHub repository](https://github.com/Far3000-YT/PTAP).

##   Author

Developed by Far3k ([GitHub Profile](https://github.com/Far3000-YT)) - Mail: far3000yt@gmail.com - Discord: @far3000 - X: @0xFar3000

---

**Start using AI more effectively with PTAP!**
