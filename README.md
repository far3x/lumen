<p align="center">
  <img src="./assets/logo.jpg" alt="Lumen Logo" width="200">
</p>

<h1 align="center">
  The official CLI for the Lumen Protocol & Local Prompt Generation.
</h1>

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

Lumen started as a powerful local tool for developers to generate flawless, LLM-ready prompts from their codebases, solving the tedious process of manual context building. As we built it, we recognized a larger opportunity: the very code developers were analyzing held immense, untapped value for the AI ecosystem.

This led to the expansion of our vision. Lumen is now a dual-purpose CLI:
1.  **A Best-in-Class Local Prompt Helper:** It remains a top-tier, 100% private utility for your daily AI-assisted development.
2.  **A Gateway to the Data Economy:** It serves as a secure bridge to the Lumen Protocol, allowing developers to ethically contribute their anonymized code and earn rewards for helping build the next generation of AI.

Whether you use it locally or to interact with the network, you're using a tool built by developers, for developers. If you find the local tools useful, please consider **starring the repository!**

<h2 id="features">Features</h2>

*   **Network Interaction:** Securely contribute your anonymized code to the Lumen Protocol and track your submission history.
*   **Local Prompt Generation:** Assemble entire codebases into a single, LLM-ready prompt without sending any data.
*   **100% Local Anonymization:** All code sanitization for protocol contributions happens on your machine. Your raw code is never uploaded.
*   **Smart File Handling:** Intelligently respects `.gitignore`, parses Jupyter Notebooks (`.ipynb`), and uses an optimized file reading strategy.
*   **GitHub Repository Support:** Analyze any public GitHub repository directly by providing its URL.
*   **Token Usage Analysis:** Identify the most token-heavy files in a project to help manage context window limitations.
*   **Customizable Filtering:** Edit a simple `config.json` file to control which files, folders, and types are processed.

<h2 id="prerequisites">Prerequisites</h2>

1.  **Python (3.7 or higher):** Check with `python --version`. Ensure Python is added to your system's PATH during installation.
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
This common issue occurs when the directory where `pip` installs scripts is not in your system's PATH.

*   **Quick Fix:** Run the tool as a Python module: `python -m lum --version`. If this works, you can use `python -m lum` instead of `lum`.
*   **Permanent Fix (Recommended):**
    *   **macOS/Linux:** Find your Python script path (often `~/.local/bin`) and add it to your shell configuration file (`~/.zshrc`, `~/.bashrc`, or `~/.bash_profile`) by adding this line: `export PATH="$HOME/.local/bin:$PATH"`. Restart your terminal or run `source ~/.zshrc` (or your respective file).
    *   **Windows:** The easiest way is to reinstall Python and ensure the "Add Python to PATH" checkbox is selected during the installation process.

<h2 id="commands">Commands</h2>

### Network Commands
These commands interact with the Lumen Protocol backend.

**Authorize Device**
Initiates the secure, browser-based login flow to link your CLI to your Lumen account.

```bash
lum login
```

**Contribute Code**
Analyzes, sanitizes, and submits the current project from your local machine to the Lumen network.

```bash
lum contribute
```

**View History**
Displays the status of your last 10 contributions to the network.

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
Assembles the current project into a prompt and copies it to your clipboard.

```bash
lum local
```

**Save Prompt to File**
Saves the generated prompt to a `.txt` file instead of copying to the clipboard.

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
Opens your `config.json` file in your system's default text editor.

```bash
lum config --edit
```

**Reset Configuration**
Resets all settings in `config.json` to their latest default values.

```bash
lum config --reset
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

Contributions, issues, and feature requests are welcome! Please check the [issues page](https://github.com/Far3000-YT/lumen/issues) and see `CONTRIBUTING.md` for more details.

<h2 id="license">License</h2>

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.