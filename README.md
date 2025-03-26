# PTAP - Project To AI Prompt 🤖

**Give Your AI the Full Picture: Instantly Generate Perfect Prompts from Your Entire Codebase!**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/ptap.svg)](https://badge.fury.io/py/ptap)
[![Python Version](https://img.shields.io/pypi/pyversions/ptap.svg)](https://pypi.org/project/ptap/)

---

## 🤔 The Problem: AI Needs Context!

Large Language Models (LLMs) are incredible tools for code analysis, debugging, documentation, and more. But to give you useful answers, they need **context**. Explaining your project's structure and providing all the relevant code snippets manually is:

*   **Time-Consuming:** Copying and pasting file structures and code takes forever.
*   **Error-Prone:** It's easy to miss files or format the prompt incorrectly.
*   **Frustrating:** You spend more time preparing the prompt than getting insights.

## ✨ The Solution: PTAP!

**PTAP (Project To AI Prompt)** automates this entire process! It scans your project directory, intelligently gathers the file structure and code content, and generates a **single, comprehensive, well-formatted prompt** ready to be pasted into your favorite AI chat.

**Stop wasting time manually crafting prompts. Let PTAP give your AI the context it needs in seconds!**

---

## 🚀 Key Features

*   ✅ **Automated Prompt Generation:** Scans your project and builds the prompt for you. Saves *massive* amounts of time.
*   🌲 **Clear Project Structure:** Includes a JSON representation of your directory tree, so the AI understands file relationships.
*   📄 **Complete Code Context:** Embeds the content of your relevant source files directly into the prompt.
*   ⚙️ **Highly Customizable:**
    *   Exclude specific folders (like `.git`, `node_modules`, `venv`).
    *   Customize the introductory text.
    *   Show or hide file titles in the output.
    *   Define which file types to include.
*   🔒 **Private & Secure:** Runs **100% locally**. Your code never leaves your machine.
*   📋 **Flexible Output:** Copies the prompt directly to your clipboard or saves it to a text file.
*   🐙 **GitHub Repository Support:** Analyze public GitHub repositories directly by providing a URL.

---

## 🎬 Demo

PTAP streamlines the process of getting your project information to an AI. You point PTAP at your code (either a local folder or a GitHub repository), it generates a detailed prompt including the file structure and code, and then you can easily copy this prompt (or save it to a file) to use with AI models like ChatGPT, Claude, etc.

*(A GIF/video demo might be added here in the future!)*

---

## 🛠️ Prerequisites

Before you install PTAP, make sure you have the following essentials installed on your system:

1.  **Python:** Version 3.7 or higher.
    *   **How to check:** Open your terminal or command prompt and type `python --version` or `python3 --version`.
    *   **How to install:** Download from [python.org](https://www.python.org/downloads/). Installation usually includes `pip`.

2.  **Pip:** Python's package installer (usually comes with Python).
    *   **How to check:** Type `pip --version` or `pip3 --version`.
    *   **How to upgrade (optional but recommended):**
        python -m pip install --upgrade pip

3.  **Git:** (Required *only* if you want to use the GitHub repository feature (`-g` flag)).
    *   **How to check:** Type `git --version`.
    *   **How to install:**
        *   **Windows:** Download from [git-scm.com](https://git-scm.com/download/win).
        *   **macOS:** Easiest way is often via Homebrew: `brew install git`. Or download from [git-scm.com](https://git-scm.com/download/mac).
        *   **Linux (Debian/Ubuntu):**
            sudo apt update && sudo apt install git
        *   **Linux (Fedora/CentOS/RHEL):**
            sudo dnf install git
            *or*
            sudo yum install git

---

## 💾 Installation

Install PTAP easily using pip:

    pip install ptap

---

## ⚙️ Usage

PTAP is a command-line tool. Here’s how to use it:

**1. Analyze Current Directory (Output to Clipboard):**
   *Navigate to your project's root directory in your terminal and run:*

    ptap

   *(This is the simplest use case. The AI prompt is copied to your clipboard.)*

**2. Analyze a Specific Project Path:**

    ptap /path/to/your/project

**3. Save Prompt to a Text File:**
   *Creates a `.txt` file in the analyzed project's root directory.*

    ptap -t my_project_prompt

   *(This will create `my_project_prompt.txt`)*

**4. Analyze a Public GitHub Repository:**
   *(Requires Git to be installed!)*

    ptap -g https://github.com/user/repository-name

   *(PTAP will clone the repo temporarily, generate the prompt, and then clean up.)*

**5. Customize Output (Hide Elements):**
   *   Hide the default introduction text:

        ptap -hd intro

   *   Hide the `--- File: path/to/file.py ---` titles (Not Recommended - can confuse AI):

        ptap -hd title

   *   Hide both:

        ptap -hd intro,title

**6. Configure PTAP:**
   *   Open the configuration file (`config.json`) for editing:

        ptap -c

       *(This opens the file in your default editor. The file is located at `~/.ptap/config.json`)*
   *   Reset the configuration file to its default settings:

        ptap -r

---

## 🔧 Configuration (`~/.ptap/config.json`)

You can customize PTAP's behavior by editing its configuration file (use `ptap -c` to open it). Key options include:

*   `intro_text`: The default text prepended to every prompt. Modify it to suit your needs!
*   `show_intro`: `true` or `false` to always show/hide the intro text by default.
*   `title_text`: The format string for file titles (e.g., `--- File: {file} ---`). `{file}` is the placeholder for the relative path.
*   `show_title`: `true` or `false` to always show/hide file titles by default.
*   `skipped_folders`: A list of folder names to **completely ignore** during scanning (e.g., `.git`, `__pycache__`, `node_modules`).
*   *(Note: The list of allowed file extensions is currently managed within `ptap/file_reader.py` but may move to config in the future.)*

---

## ⚠️ Limitations

*   **AI Input Limits:** Very large projects might generate prompts exceeding the maximum input length of some AI models.
*   **File Types:** Primarily designed for text-based source code files. Binary files or unusual encodings might not be processed correctly.
*   **AI Interpretation:** The AI's understanding still depends on its own capabilities.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/Far3000-YT/PTAP/issues) or submit a pull request.

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

Developed by **Far3k**

*   **GitHub:** [Far3000-YT](https://github.com/Far3000-YT)
*   **Email:** far3000yt@gmail.com
*   **Discord:** @far3000
*   **X (Twitter):** [@0xFar3000](https://twitter.com/0xFar3000)

---

**Unlock the full potential of AI for your code. Give PTAP a try!**