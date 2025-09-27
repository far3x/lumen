<p align="center">
  <img src="./assets/logo.jpg" alt="Lumen Logo" width="200">
</p>

<h2 align="center">
  The official CLI for the Lumen Protocol & Local Prompt Generation.
</h2>

<p align="center">
    <a href="https://badge.fury.io/py/pylumen"><img src="https://badge.fury.io/py/pylumen.svg" alt="PyPI version"></a>
    <a href="https://pepy.tech/project/pylumen"><img src="https://static.pepy.tech/badge/pylumen" alt="Downloads"></a>
    <a href="https://pypi.org/project/pylumen/"><img src="https://img.shields.io/pypi/pyversions/pylumen.svg" alt="Python Version"></a>
    <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
</p>
<p align="center">
    <a href="https://github.com/Far3000-YT/lumen/actions/workflows/release.yaml"><img src="https://github.com/Far3000-YT/lumen/actions/workflows/release.yaml/badge.svg" alt="Build Status"></a>
    <a href="https://github.com/Far3000-YT/lumen/blob/main/CONTRIBUTING.md"><img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat" alt="Contributions welcome"></a>
    <a href="https://lumen.onl/docs/introduction"><img src="https://img.shields.io/badge/docs-lumen.onl-13131A.svg" alt="Documentation"></a>
    <a href="https://github.com/Far3000-YT/lumen/stargazers/"><img src="https://img.shields.io/github/stars/Far3000-YT/lumen.svg?style=social&label=Star" alt="GitHub stars"></a>
</p>

---

### Table of Contents

-   [Why Lumen?](#why-lumen)
-   [Features](#features)
-   [Prerequisites](#prerequisites)
-   [Installation & Troubleshooting](#installation--troubleshooting)
-   [Commands](#commands)
    -   [Network Commands](#network-commands)
    -   [Local Prompt Generation](#local-prompt-generation)
    -   [Configuration](#configuration)
-   [Documentation](#documentation)
-   [Contributing](#contributing)
-   [License](#license)

---

<h2 id="why-lumen">Why Lumen?</h2>

Lumen is a dual-purpose CLI designed for developers. It began as a powerful local tool to solve the tedious process of manual context building for LLMs and evolved into a gateway for developers to ethically contribute to the AI data economy.

1.  **A Best-in-Class Local Prompt Helper:** A 100% private utility for your daily AI-assisted development.
2.  **A Gateway to the Data Economy:** A secure bridge to the Lumen Protocol, allowing developers to ethically contribute their anonymized code and earn rewards.

If you find the local tools useful, please consider **starring the repository!**

<h2 id="features">Features</h2>

*   **Network Interaction:** Securely contribute your anonymized code to the Lumen Protocol and track your submission history.
*   **Local Prompt Generation:** Assemble entire codebases into a single, LLM-ready prompt without sending any data.
*   **100% Local Anonymization:** All code sanitization for protocol contributions happens on your machine. Your raw code is never uploaded.
*   **Smart File Handling:** Intelligently respects `.gitignore`, ignores dotfiles, parses Jupyter Notebooks (`.ipynb`) (locally), and uses an optimized / custom-built + unique file reading strategy.
*   **GitHub Repository Support:** Analyze any public GitHub repository directly by providing its URL.
*   **Token Usage Analysis:** Identify the most token-heavy files in a project to manage context window limitations.
*   **Customizable Filtering:** Use the CLI or edit a simple `config.json` file to control which files, folders, and types are processed.

<h2 id="prerequisites">Prerequisites</h2>

1.  **Python (3.7 or higher):** Check with `python --version`.
2.  **Git:** Required only for analyzing GitHub repositories (`-g` flag). Check with `git --version`.

<h2 id="installation--troubleshooting">Installation & Troubleshooting</h2>

Install directly from PyPI:
```bash
pip install pylumen
```

To upgrade to the latest version:
```bash
pip install --upgrade pylumen
```

#### Troubleshooting `command not found: lum`
This occurs when the `pip` scripts directory is not in your system's PATH.

*   **Quick Fix:** Run the tool as a Python module: `python -m lum --version`.
*   **Permanent Fix (Recommended):**
    *   **macOS/Linux:** Find your Python script path (often `~/.local/bin`) and add it to your shell configuration (`~/.zshrc`, `~/.bashrc`): `export PATH="$HOME/.local/bin:$PATH"`. Restart your terminal.
    *   **Windows:** Reinstall Python and ensure the "Add Python to PATH" checkbox is selected.

<h2 id="commands">Commands</h2>

### Network Commands
These commands interact with the Lumen Protocol backend.

**Authorize Device**
Initiates the secure login flow to link your CLI to a Lumen account.
```bash
lum login
```

**Contribute Code**
Analyzes, sanitizes, and submits the current project to the Lumen network.
```bash
lum contribute
```

**View History**
Displays the status of your last 10 contributions.
```bash
lum history
```

**De-authorize Device**
Logs out and securely removes the local authentication token.
```bash
lum logout
```

### Local Prompt Generation
These commands do **not** send any data to the network.

**Analyze Current Directory**
Assembles the project into a prompt and copies it to your clipboard.
```bash
lum local
```

**Save Prompt to File**
Saves the prompt to a `.txt` file instead of copying.
```bash
lum local -t my_project_prompt
```

**Analyze a GitHub Repository**
Clones a public repo to a temporary directory for analysis.
```bash
lum local -g https://github.com/user/repo-name
```

**Identify Token-Heavy Files**
Shows a leaderboard of the most token-consuming files.
```bash
# See the top 20 (default) files
lum local -l

# See the top 10 files
lum local -l 10
```

<h3 id="configuration">Configuration</h3>

**Edit Configuration**
Opens `config.json` in your system's default text editor.
```bash
lum config --edit
```

**Reset Configuration**
Resets all settings in `config.json` to their default values.
```bash
lum config --reset
```

**Set a Specific Value**
Changes a single setting directly from the terminal.
```bash
# Enable a boolean setting
lum config --set use_ai_instructions true

# Overwrite a list (provide as a comma-separated string)
lum config --set skipped_files ".DS_Store,yarn.lock"
```

---

<h2 id="documentation">Documentation</h2>

For detailed documentation on the Lumen Protocol, including the valuation engine, security practices, and our long-term vision, please visit our official documentation site.

-   [Installation Guide](https://lumen.onl/docs/installation)
-   [CLI Authentication](https://lumen.onl/docs/authentication)
-   [Protocol Valuation Engine](https://lumen.onl/docs/valuation)
-   [Security by Design](https://lumen.onl/docs/security)
-   [The Lumen Whitepaper](https://lumen.onl/docs/whitepaper)

<h2 id="contributing">Contributing</h2>

Contributions, issues, and feature requests are welcome! Please check the [issues page](https://github.com/Far3000-YT/lumen/issues) and see `CONTRIBUTING.md` for details.

<h2 id="license">License</h2>

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.