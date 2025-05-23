Lumen - Supercharge Your AI with Perfect Code Context
====================================================

[![PyPI version](https://badge.fury.io/py/pylumen.svg)](https://badge.fury.io/py/pylumen)
[![Downloads](https://static.pepy.tech/badge/pylumen)](https://pepy.tech/project/pylumen)
[![Python Version](https://img.shields.io/pypi/pyversions/pylumen.svg)](https://pypi.org/project/pylumen/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/Far3000-YT/lumen.svg?style=social&label=Star&maxAge=14400)](https://github.com/Far3000-YT/lumen/stargazers/)

---

Disclamer: this code was almost ENTIRELY written by me, AI was poorly involved in this project (only used it for some permission issues while deleting git folders, because git clone is a buggy command for security purposes). Yes, it's fun to code manually and optimize code naturally :))

**Unlock Your AI's Full Potential with Flawless Code Understanding.**

Large Language Models (LLMs) are revolutionizing software development. However, their efficacy is often limited by the quality and completeness of the provided **context**. Manually feeding your AI with relevant information from your codebase can be a tedious, error-prone process, especially for large projects constrained by context window limitations.

**Lumen is engineered to address this challenge.**

Lumen is an intelligent Command Line Interface (CLI) tool that automatically scans, structures, and formats your entire codebase into a meticulously crafted prompt suitable for *any* LLM. Eliminate the friction of manual copy-pasting and context constraints. With Lumen, you provide your AI with the deep, structured understanding necessary to generate truly insightful and accurate results.

**Elevate your AI interactions from challenging to highly effective. Power up with Lumen.**

---

## Why Lumen?

*   **Effortless Context Generation:** Automatically gathers and structures your entire project, removing manual drudgery.
*   **Optimized Performance:** Experience significantly faster context generation. Internal optimizations, especially in configuration handling, deliver substantial speed improvements, particularly noticeable on large-scale projects.
*   **Intelligent File Handling:**
    *   Reads a wide variety of file types, including `.ipynb` notebooks.
    *   Employs a smart encoding strategy: defaults to UTF-8 for speed and reliability, with an intelligent fallback to detect encoding only if an initial read encounters issues. This ensures correct rendering of special characters and improves overall reading performance.
*   **Optimized for AI:** Delivers a standardized, AI-friendly output format, including consistent file separators and an introductory message, ensuring maximum LLM comprehension.
*   **GitHub Repository Analysis:** Seamlessly analyze public GitHub repositories with a single command. Lumen handles the cloning and subsequent cleanup.
*   **100% Private & Secure:** Processes everything locally. For local projects, your code never leaves your machine during context generation.
*   **Token Insights:** Utilize the `-l` or `--leaderboard` option to identify the most token-heavy files in your project (top 20 by default), aiding in the optimization of large contexts.
*   **Reliable & Tested:** Backed by a comprehensive test suite to ensure stability and correctness.

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

To upgrade to the latest version:

`pip install pylumen --upgrade`

---

## Quick Start & Usage

Lumen is designed for ease of use from your command line (`lum`).

**1. Generate Full Context (Clipboard):**
   Navigate to your project's root and run:
   `lum`
   *(The complete, structured prompt is copied to your clipboard. For very large codebases, consider the `-t` option for better performance.)*

**2. Analyze a Specific Path:**
   `lum /path/to/your/project`

**3. Save to File:**
   `lum -t my_project_context`
   *(Creates `my_project_context.txt` in the project's root.)*

**4. Analyze a Public GitHub Repository:**
   *(Requires Git installed!)*
   `lum -g https://github.com/user/repo-name`

**5. Identify Token-Heavy Files:**
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
*   `skipped_folders`: A comprehensive list of folder names to ignore. This supports two types of matching:
    *   **Exact Match:** A string like `"build"` will only skip folders named exactly `build`.
    *   **Ends-With Match:** A string prefixed with `*`, like `"*.log"` or `".cache"`, will skip any folder whose name *ends with* `.log` (e.g., `app.log`, `server.log`) or `.cache` (e.g., `.pytest_cache`, `.mypy_cache`).
*   `skipped_files`: A list of specific file names to exclude from context (e.g., `package-lock.json`, `.DS_Store`).
*   `allowed_file_types`: Specify which file extensions Lumen should process.

**Automatic Updates:** Lumen's configuration is designed to be future-proof. If new configuration options are added in an update, your `config.json` will be intelligently updated to include them with their default values, preserving your existing customizations. You can always reset to the latest defaults with `lum -r`.

---

## What's Next? The Lumen Roadmap

Lumen is actively evolving! Here's a glimpse of planned features and directions:

*   **IDE Integration:** Development of a VS Code extension is underway to allow "Lumen: Copy Context" functionality directly from your editor.
*   **Web Interface (Exploratory):** We are exploring the potential for a web-based interface to further enhance usability and accessibility.
*   **Lumen v1.0:** The next major milestone will be Lumen v1.0, focusing on delivering a highly stable, polished, and production-ready experience with further refinements and potential feature enhancements.

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
