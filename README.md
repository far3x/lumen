💡 Lumen - Illuminate Your Codebase for AI</h1>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/pylumen.svg)](https://badge.fury.io/py/pylumen)
[![Python Version](https://img.shields.io/pypi/pyversions/lum.svg)](https://pypi.org/project/pylumen/)

---

## The Context Challenge: Bridging Code and AI Understanding

Large Language Models (LLMs) offer transformative potential for software development – from debugging and refactoring to documentation and architectural analysis. However, their effectiveness is fundamentally limited by the **context window**: the amount of information they can process at one time.

Providing an LLM with the necessary context for a complex query about your project is a significant challenge:

*   **Manual Effort:** Copying and pasting file structures, code snippets, and dependencies for a large codebase is time-consuming and prone to errors.
*   **Context Limits:** Even with large context models, providing the *entire* codebase is often impossible, expensive, or leads to the "lost in the middle" problem where relevant information is overlooked amidst noise.
*   **Lack of Structure:** Simply dumping files doesn't help the AI understand the relationships between different parts of your project.

## Introducing Lumen: Intelligent Code Context for Any LLM

**Lumen** is a command-line tool designed to solve the AI context problem. It scans your project, understands its structure, and **intelligently selects and formats the most relevant code context** for a given natural language query.

Unlike tools that aim to replace your coding environment or fully automate tasks, Lumen focuses on perfecting the **input** you provide to the AI. It empowers you to use *any* LLM (public APIs like Gemini, Claude, ChatGPT, or local models) with a comprehensive, yet focused, understanding of your specific codebase, enabling more accurate and insightful AI responses.

**Stop struggling with context windows. Give your AI the precise information it needs, powered by Lumen.**

---

## Key Features

*   **Intelligent Context Retrieval:** Uses advanced techniques (like vector embeddings) to find and include only the code chunks most relevant to your specific question, overcoming context window limitations for large projects.
*   **Clear Project Structure:** Generates a JSON representation of your directory tree, providing the AI with essential architectural context.
*   **Full or Focused Context Modes:** Choose between providing the entire project content (for smaller projects or general overview) or using intelligent search for query-specific context.
*   **Highly Customizable:** Configure which folders and files are included or skipped, control output formatting, and adjust indexing parameters.
*   **Private & Secure:** Operates **100% locally** on your machine for local projects. Your code content is never sent to external services during context generation or indexing.
*   **Flexible Output:** Copies the generated prompt to your clipboard or saves it to a text file in your project directory.
*   **GitHub Repository Support:** Analyze public GitHub repositories directly by providing a URL. Lumen handles temporary cloning and cleanup.

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

`pip install lum`

---

## Usage

Lumen is primarily a command-line tool (`lum`).

**1. Generate Full Context for Current Directory (Output to Clipboard):**
   *Navigate to your project's root directory in your terminal and run:*

`lum`
   *(This is the default behavior. The complete, structured prompt including structure and file contents is copied to your clipboard. Suitable for smaller projects or general overview.)*

**2. Generate Full Context for a Specific Project Path:**

`lum /path/to/your/project`

**3. Generate Intelligent, Query-Specific Context: (coming soon, in development for now !)**
   *For larger projects, provide a natural language query to get only the most relevant code chunks:*

    `lum --query "Explain how users are authenticated"`
   *This triggers the embedding-based retrieval.*
   *   **Indexing:** The *first time* you use `--query` on a project, Lumen will build a local index of your codebase (chunking files, generating embeddings). This takes time depending on project size and your hardware. Subsequent queries are fast.
   *   **Prompt:** The generated prompt will include your query, the project structure, and the content of the top relevant code chunks found.

**4. Force Re-indexing for Queries: (In dev too)**
   *If your code changes significantly after indexing, you might want to rebuild the index:*

`lum --query "check payment processing logic" --reindex`
   *This clears the old index for the project and builds a new one.*

**5. Control Number of Relevant Chunks (Query Mode): (In dev too)**
   *Specify how many top relevant code chunks to include in the prompt:*

`lum --query "What are the main API endpoints?" --top-k 20`
   *Overrides the default set in the configuration.*

**6. Save Prompt to a Text File:**
   *Creates a `.txt` file in the analyzed project's root directory.*

`lum -t my_project_prompt`
   *(This will create `my_project_prompt.txt`)*

**7. Analyze a Public GitHub Repository:**
   *(Requires Git to be installed!)*

`lum -g https://github.com/user/public-repository-name`
   *(Lumen will clone the repo temporarily, generate the prompt (full dump or query-based if `--query` is also used), and then clean up the cloned repository.)*

**8. Customize Output (Hide Elements):**
   *   Hide the default introduction text:

`lum -hd intro`
   *   Hide the `--- File: path/to/file.py ---` titles (Not Recommended - can confuse AI, automatically hidden in `--query` mode):

`lum -hd title`
   *   Hide both:

`lum -hd intro,title`

**9. Configure Lumen:**
   *   Open the configuration file (`config.json`) for editing:

`lum -c`
       *(This opens the file in your default editor. The file is located in your user's configuration directory, e.g., `~/.ptap/config.json` - this path might change to `~/.lumen/config.json` in a future rename)*
   *   Reset the configuration file to its default settings:

`lum -r`

---

## Configuration (`~/.ptap/config.json` or `~/.lumen/config.json`)

You can customize Lumen's behavior by editing its configuration file (use `lum -c` to open it). Key options include:

*   `intro_text`: The default text prepended to every prompt. Modify it to suit your needs.
*   `show_intro`: `true` or `false` to always show/hide the intro text by default.
*   `title_text`: The format string for file/chunk titles (e.g., `--- File: {file} ---`). `{file}` is the placeholder for the relative path.
*   `show_title`: `true` or `false` to always show/hide file titles by default (ignored in `--query` mode for individual chunks).
*   `skipped_folders`: A list of folder names to **completely ignore** during scanning (e.g., `.git`, `__pycache__`, `node_modules`).
*   `embedding_model_name`: The name of the Sentence Transformer model to use for embeddings (e.g., ``"BAAI/bge-base-en-v1.5"``). Choose a model suitable for code embeddings, often listed on the MTEB leaderboard.
*   `max_chunk_tokens`: The maximum number of tokens per code chunk during indexing. Ensure this is less than the chosen embedding model's maximum sequence length.
*   `overlap_tokens`: The number of tokens to overlap between consecutive chunks during indexing. This is crucial for ensuring relevant information isn't split between chunks.
*   `search_top_k`: The default number of top relevant chunks to retrieve when using `--query`.

This version of the configuration is abit too updated (in the future), do not take into account the last 4 variables (from ``embedding_model_name``) please !
---

## Future Objectives (Roadmap)

Lumen is under active development. Key areas for future focus include:

*   **Advanced Chunking:** Exploring language-aware or more intelligent chunking strategies beyond fixed-size blocks to better capture semantic units like functions and classes.
*   **IDE Integrations:** Developing extensions for popular IDEs (VS Code, JetBrains) to provide a more seamless workflow for generating context directly from your development environment.
*   **Enhanced Relevance Tuning:** Improving the embedding and retrieval process with techniques specifically tailored for code, potentially including code-specific embedding models.
*   **Context Summarization:** Exploring ways to provide high-level summaries of less critical files or sections to include alongside detailed code context.
*   **Performance Optimizations:** Continuously improving indexing and search speed, especially for very large repositories.
*   **Broader Language Support:** Ensuring robust handling of file types and structures across an even wider range of programming languages.
*   **Team Features & Collaboration:** Investigating features for teams to manage project profiles, share context, and collaborate on AI-assisted tasks.

---

## Limitations

*   **AI Interpretation:** The quality of the AI's response still ultimately depends on the capabilities of the LLM you use.
*   **Very Large Projects:** While embeddings will help, extremely massive projects (millions of lines) may still present challenges in balancing context size and relevance.
*   **File Types:** Primarily designed for text-based source code and configuration files. Binary files or unusual encodings are not supported.

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

**Empower your AI with the context it needs. Install Lumen today.**