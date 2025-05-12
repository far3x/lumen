💡 Lumen - Illuminate Your Codebase for AI</h1>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/pylumen.svg)](https://badge.fury.io/py/pylumen)
[![Python Version](https://img.shields.io/pypi/pyversions/pylumen.svg)](https://pypi.org/project/pylumen/)

---

## The Context Challenge: Bridging Code and AI Understanding

Large Language Models (LLMs) offer transformative potential for software development – from debugging and refactoring to documentation and architectural analysis. However, their effectiveness is fundamentally limited by the **context window**: the amount of information they can process at one time.

Providing an LLM with the necessary context for a complex query about your project is a significant challenge:

*   **Manual Effort:** Copying and pasting file structures, code snippets, and dependencies for a large codebase is time-consuming and prone to errors.
*   **Context Limits:** Even with large context models, providing the *entire* codebase is often impossible or expensive.
*   **Lack of Structure:** Simply dumping files doesn't help the AI understand the relationships between different parts of your project.

## Introducing Lumen: Structured Code Context for Any LLM

**Lumen** is a command-line tool designed to solve the AI context problem by automating the process of gathering and structuring your codebase for LLMs. It scans your project, understands its file structure, and **formats the relevant code content** into a clear, comprehensive prompt.

Lumen focuses on perfecting the **input** you provide to the AI. It empowers you to use *any* LLM (public APIs like Gemini, Claude, ChatGPT, or local models) with a structured understanding of your specific codebase, enabling more accurate and insightful AI responses without the manual overhead.

**Stop struggling with context windows and manual copy-pasting. Give your AI the structured information it needs, powered by Lumen.**

---

## Key Features

*   **Clear Project Structure:** Generates a JSON representation of your directory tree, providing the AI with essential architectural context.
*   **Comprehensive Context Generation:** Gathers the content of all specified files within the project directory.
*   **Intelligent File Reading:** Supports various file types, including `.ipynb` (Jupyter Notebooks), and automatically detects file encoding for reliable reading.
*   **Highly Customizable:** Configure which folders and files are included or skipped, and control output formatting.
*   **Private & Secure:** Operates **100% locally** on your machine for local projects. Your code content is never sent to external services during context generation.
*   **Flexible Output:** Copies the generated prompt to your clipboard or saves it to a text file in your project directory.
*   **GitHub Repository Support:** Analyze public GitHub repositories directly by providing a URL. Lumen handles temporary cloning and cleanup.
*   **Improved Readability:** Includes options to hide introductory text or file titles for a more focused output if needed.
*   **Robust Testing:** Includes a suite of tests covering file reading, structure visualization, and GitHub integration.

---

## Prerequisites

Before installing Lumen, ensure you have the following installed and correctly configured on your system. Lumen is a Python tool and relies on standard development environments.

1.  **Python (3.7 or higher):**
    *   **How to Check:** Open your terminal or command prompt and type `python --version` or `python3 --version`.
    *   **Installation & Environment Setup:**
        *   **Windows:** Download the installer from [python.org](https://www.python.org/downloads/windows/). **Crucially, during installation, ensure you check the box that says "Add Python to PATH"**. This makes `python` and `pip` commands available from any terminal window. If you missed this, you might need to reinstall or manually add Python to your system's Environment Variables.
        *   **macOS:** Python 3 is often pre-installed or easily available via Homebrew (``brew install python``). Ensure the Homebrew bin directory is in your PATH (usually set up automatically). You can verify Python and Pip availability by opening a new terminal window after installation.
        *   **Linux (Debian/Ubuntu):**
            ```bash
            sudo apt update
            sudo apt install python3 python3-pip
            ```
        *   **Linux (Fedora/CentOS/RHEL):**
            ```bash
            sudo dnf install python3 python3-pip
            # or
            sudo yum install python3 python3-pip
            ```
        *   Ensure `python3` and `pip3` (or symlinks like `python` and `pip`) are in your PATH. Installing via package managers typically handles this.
    *   **Pip:** Python's package installer. It's usually installed with Python 3.7+.
        *   **How to Check:** Type `pip --version` or `pip3 --version`.
        *   **How to Upgrade (Recommended):** `python -m pip install --upgrade pip` or `python3 -m pip install --upgrade pip`.

2.  **Git:** (Required *only* if you plan to use the GitHub repository feature (`-g` flag)).
    *   **How to Check:** Type `git --version`.
    *   **Installation:**
        *   **Windows:** Download from [git-scm.com](https://git-scm.com/download/win). Follow the installer steps, ensuring Git is added to your PATH (a default option).
        *   **macOS:** Easiest via Homebrew: ``brew install git``. Or download from [git-scm.com](https://git-scm.com/download/mac). Command Line Tools for Xcode also include Git.
        *   **Linux:** Use your distribution's package manager (as shown for Python, but replace `python` with `git`).

---

## Installation

Install Lumen easily using pip:

`pip install pylumen`

---

## Usage

Lumen is primarily a command-line tool (`lum`).

**1. Generate Full Context for Current Directory (Output to Clipboard):**
   *Navigate to your project's root directory in your terminal and run:*

`lum`
   *(This is the default behavior. The complete, structured prompt including structure and file contents is copied to your clipboard. Suitable for smaller to medium projects or general overview.)*

**2. Generate Full Context for a Specific Project Path:**

`lum /path/to/your/project`

**3. Save Prompt to a Text File:**
   *Creates a `.txt` file in the analyzed project's root directory.*

`lum -t my_project_prompt`
   *(This will create `my_project_prompt.txt`)*

**4. Analyze a Public GitHub Repository:**
   *(Requires Git to be installed!)*

`lum -g https://github.com/user/public-repository-name`
   *(Lumen will clone the repo temporarily, generate the prompt, and then clean up the cloned repository.)*

**5. Customize Output (Hide Elements):**
   *   Hide the default introduction text:

`lum -hd intro`
   *   Hide the `--- File: path/to/file.py ---` titles (Not Recommended - can confuse AI):

`lum -hd title`
   *   Hide both:

`lum -hd intro,title`

**6. Configure Lumen:**
   *   Open the configuration file (`config.json`) for editing:

`lum -c`
       *(This opens the file in your default editor. The file is located in your user's configuration directory, e.g., `~/.lum/config.json`)*
   *   Reset the configuration file to its default settings:

`lum -r`

---

## Configuration (`~/.lum/config.json`)

You can customize Lumen's behavior by editing its configuration file (use `lum -c` to open it). Key options include:

*   `intro_text`: The default text prepended to every prompt. Modify it to suit your needs.
*   `show_intro`: `true` or `false` to always show/hide the intro text by default.
*   `title_text`: The format string for file titles (e.g., `--- File: {file} ---`). `{file}` is the placeholder for the relative path.
*   `show_title`: `true` or `false` to always show/hide file titles by default.
*   `skipped_folders`: A list of folder names to **completely ignore** during scanning (e.g., `.git`, `__pycache__`, `node_modules`).

---

## Future Objectives (Roadmap)

Lumen is under active development. Key areas for future focus include:

*   Reworking the help section for `argparse` for improved clarity.
*   Adding a clear `--- PROJECT STRUCTURE ---` separator before the JSON block in the output.
*   Refactoring the configuration loading logic (`get` functions).
*   Updating `__init__.py` and the README to facilitate using Lumen's core file reading utilities (`chunk_read`, `read_ipynb`, `detect_encoding`) directly as a Python module.
*   Moving the lists of allowed and non-allowed files to the configuration file for easier customization.
*   Implementing a ranking system to identify the most token-expensive files, potentially adding a `--leaderboard` or `-l` option to display them.
*   Adding options to exclude comments and/or excessive whitespace from the output to reduce token count.
*   Exploring integration with Abstract Syntax Trees (AST) to potentially provide a more semantic, lower-token representation of code.
*   Developing extensions for popular IDEs (like VS Code) to provide a more seamless workflow for generating context directly from your development environment (e.g., a "Lumen: Copy Context" right-click option).

The AST integration and IDE extensions represent significant steps towards more advanced code understanding and workflow integration, and are key long-term goals.

---

## Limitations

*   **AI Interpretation:** The quality of the AI's response still ultimately depends on the capabilities of the LLM you use.
*   **Very Large Projects:** While Lumen structures the output, providing the full content of extremely massive projects (millions of lines) in a single prompt may still exceed context window limits or dilute relevance.
*   **File Types:** Primarily designed for text-based source code and configuration files. Binary files or unusual encodings not handled by `chardet` may not be read correctly.

---

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/Far3000-YT/lumen/issues) or submit a pull request. Adherence to code quality and project goals is appreciated.

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

---

**Empower your AI with the structured context it needs. Install Lumen today.**