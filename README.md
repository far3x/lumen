💡 Lumen - Supercharge Your AI with Perfect Code Context</h1>

[![PyPI version](https://badge.fury.io/py/pylumen.svg)](https://badge.fury.io/py/pylumen)
[![Downloads](https://static.pepy.tech/badge/pylumen)](https://pepy.tech/project/pylumen)
[![Python Version](https://img.shields.io/pypi/pyversions/pylumen.svg)](https://pypi.org/project/pylumen/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/Far3000-YT/lumen.svg?style=social&label=Star&maxAge=14400)](https://github.com/Far3000-YT/lumen/stargazers/)

---

**Unlock Your AI's Full Potential with Flawless Code Understanding.**

Large Language Models (LLMs) are revolutionizing software development. But their power is capped by one crucial factor: **context**. Feeding your AI the right information about your codebase is tedious, error-prone, and often impossible for large projects due to context window limitations.

**Lumen is here to change that.**

Lumen is your intelligent CLI companion that automatically scans, structures, and formats your entire codebase into a perfectly crafted prompt for *any* LLM. Stop wrestling with manual copy-pasting and context limits. With Lumen, you give your AI the deep, structured understanding it needs to deliver truly insightful and accurate results.

**Elevate your AI interactions from frustrating to phenomenal. Power up with Lumen.**

---

## Why Lumen?

* 🚀 - **Effortless Context Generation:** Automatically gathers and structures your entire project, no more manual drudgery.
* 🧠 - **Smart File Handling:** Intelligently reads various file types (including `.ipynb` notebooks) with automatic encoding detection.
* ⚙️ - **Optimized for AI:** Delivers a standardized, AI-friendly output format, including consistent file separators and an introductory message, ensuring maximum LLM comprehension.
* 🌐 - **GitHub Repo Analysis:** Seamlessly analyze public GitHub repositories with a single command. Lumen handles the cloning and cleanup.
* 🛡️ - **100% Private & Secure:** Processes everything locally. Your code never leaves your machine during context generation for local projects.
* 📊 - **Token Insights (New !):** Use the `-l` or `--leaderboard` option to identify the most token-heavy files in your project (top 20 by default), helping you optimize large contexts.
* ✅ - **Reliable & Tested:** Backed by a comprehensive test suite.

---

## Prerequisites

Before installing Lumen, ensure you have the following installed and correctly configured on your system. Lumen is a Python tool and relies on standard development environments.

1.  **Python (3.7 or higher):**
    *   **How to Check:** Open your terminal or command prompt and type `python --version` or `python3 --version`.
    *   **Installation & Environment Setup:**
        *   **Windows:** Download the installer from [python.org](https://www.python.org/downloads/windows/). **Crucially, during installation, ensure you check the box that says "Add Python to PATH"**.
        *   **macOS:** Python 3 is often pre-installed or easily available via Homebrew (`brew install python`).
        *   **Linux (Debian/Ubuntu):** `sudo apt update && sudo apt install python3 python3-pip`
        *   **Linux (Fedora/CentOS/RHEL):** `sudo dnf install python3 python3-pip` (or `yum`)
    *   **Pip:** Python's package installer, usually installed with Python 3.7+.
        *   **How to Check:** `pip --version` or `pip3 --version`.
        *   **Upgrade (Recommended):** `python -m pip install --upgrade pip`.

2.  **Git:** (Required *only* if you plan to use the GitHub repository feature (`-g` flag)).
    *   **How to Check:** `git --version`.
    *   **Installation:** Download from [git-scm.com](https://git-scm.com/downloads) or use your system's package manager (e.g., `brew install git`, `sudo apt install git`).

---

## Installation

Install Lumen easily using pip:

`pip install pylumen`

---

## Quick Start & Usage

Lumen is a breeze to use from your command line (`lum`).

**1. Generate Full Context (Clipboard):**
   Navigate to your project's root and run:
   `lum`
   *(The complete, structured prompt is copied to your clipboard.)*

**2. Analyze a Specific Path:**
   `lum /path/to/your/project`

**3. Save to File:**
   `lum -t my_project_context`
   *(Creates `my_project_context.txt` in the project's root.)*

**4. Analyze a Public GitHub Repository:**
   *(Requires Git installed!)*
   `lum -g https://github.com/user/repo-name`

**5. Identify Token-Heavy Files (New!):**
   See the top 20 (default) most token-consuming files:
   `lum -l`
   Or specify a different number (e.g., top 10):
   `lum -l 10`
   *(This also generates and copies/saves the full context as per other commands.)*

**6. Manage Configuration:**
   *   Edit your settings: `lum -c`
       *(Opens `~/.lum/config.json` in your default editor.)*
   *   Reset to defaults: `lum -r`

*For a full list of commands and options, Lumen features a clear and consistent help section:*
`lum --help`

---

## Configuration (`~/.lum/config.json`)

Tailor Lumen to your exact needs by editing its configuration file (`~/.lum/config.json`). Use `lum -c` to open it.

Key settings include:
*   `intro_text`: Customize the introductory message for your prompts.
*   `title_text`: Define the format for file titles (e.g., `--- FILE : {file} ---`).
*   `skipped_folders`: A comprehensive list of folder names to ignore (e.g., `.git`, `node_modules`, `venv`).
*   `skipped_files`: A list of specific file names to exclude from context (e.g., `package-lock.json`, `.DS_Store`).
*   `allowed_file_types`: Specify which file extensions Lumen should process.

**Automatic Updates:** Lumen's configuration is designed to be future-proof. If new configuration options are added in an update, your `config.json` will be intelligently updated to include them, typically preserving your existing customizations. You can always reset to the latest defaults with `lum -r`.

---

## What's Next? The Lumen Roadmap

Lumen is actively evolving! Here's a glimpse of exciting features planned:

*   **Streamlined Configuration:** Optimizing the `config.json` structure for conciseness and easier management.
*   **Enhanced Core Logic:** Refactoring configuration loading and internal data handling for greater efficiency and robustness.
*   **Lumen as a Library:** Making core utilities like `chunk_read`, `read_ipynb`, and `detect_encoding` easily importable for your Python projects.
*   **Smarter Token Reduction:**
    *   Option to exclude comments from the generated context.
    *   Option to minimize excessive whitespace.
*   **IDE Integration:** A VS Code extension for "Lumen: Copy Context" right from your editor.
*   **Advanced Code Understanding:** Exploring Abstract Syntax Tree (AST) integration for a more semantic, potentially even lower-token, representation of your code.

Stay tuned for these and more improvements!

---

## Love Lumen? Give us a Star!

If Lumen helps you supercharge your AI workflows, please consider starring the project on GitHub! It's a great way to show your support and helps others discover Lumen.

[![GitHub stars](https://img.shields.io/github/stars/Far3000-YT/lumen.svg?style=social&label=Star&maxAge=2592000)](https://github.com/Far3000-YT/lumen/stargazers/)

---

## Contributing

We welcome contributions, issues, and feature requests! Check out the [issues page](https://github.com/Far3000-YT/lumen/issues) or submit a pull request. See `CONTRIBUTING.md` for more details. Let's make Lumen even better, together!

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Author

Developed by **Far3k**

*   **GitHub:** [Far3000-YT](https://github.com/Far3000-YT)
*   **Email:** far3000yt@gmail.com
*   **Discord:** @far3000
*   **X (Twitter):** [@0xFar3000](https://twitter.com/0xFar3000)