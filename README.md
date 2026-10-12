# AI File Search

AI File Search is a Python utility that indexes files and folders on your computer and lets you find them by name, by fuzzy/typo-tolerant matching, or by describing what you want in plain English. It can also search inside plain-text documents and basic office/PDF files.

This project is designed to work entirely on your local machine. Your files are never uploaded. In `ask` mode, only the sentence you type is sent to the AI provider (and never when using the built-in `mock` mode or Ollama running locally on your own machine).

## Features

- Fast local indexing of files and folders using SQLite
- Search by exact match, partial match, or fuzzy/typo-tolerant matching
- Search only files or only folders
- Limit searches by file extension, such as `.pdf`, `.docx`, or `.py`
- Use natural-language "ask" mode to describe what you want in plain English
- Search inside documents for a phrase or keyword
- Works on Windows, macOS, and Linux
- Optional AI providers: `mock`, `ollama`, and `anthropic`

## Project goals

This tool was built to help you:

- Find files and folders anywhere on your machine without remembering exact names
- Work when you only remember part of the name or a rough description
- Search content inside text-based and common document files
- Keep the workflow local and private

## How it works

The tool follows a simple workflow:

1. Index your drives once and store the names in a local SQLite database
2. Search by filename using exact, partial, or fuzzy matching
3. Optionally describe what you want in plain English and let the script interpret it
4. Search inside supported document types for text content

## Requirements

- Python 3.10+
- Access to local filesystem
- Optional: Ollama or Anthropic API access for AI-assisted natural-language search

## Installation

Clone the repository:

```bash
git clone https://github.com/Nayan123732/Ai-tools.git
cd Ai-tools
```

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
# On Windows:
# .venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

If you do not yet have a `requirements.txt`, install the needed packages manually:

```bash
pip install pypdf requests anthropic
```

## Quick start

### 1) Build the index

This scans your local drives and stores metadata in a SQLite database.

```bash
python ai_file_search.py index
```

You can optionally limit the roots being indexed:

```bash
python ai_file_search.py index --roots C:\ D:\
```

On macOS/Linux, the default root is your home directory. You can also include system folders if needed:

```bash
python ai_file_search.py index --include-system
```

By default, the database is stored at:

```text
~/.ai_file_search.db
```

You can override this with:

```bash
python ai_file_search.py --db /path/to/custom.db index
```

### 2) Search by name

Search for a file or folder by name:

```bash
python ai_file_search.py find "resume"
```

Limit to files only:

```bash
python ai_file_search.py find "budget" --type file
```

Limit to folders only:

```bash
python ai_file_search.py find "projects" --type folder
```

Limit by extension:

```bash
python ai_file_search.py find "report" --ext .pdf .docx
```

### 3) Ask in plain English

Describe the file you want in natural language:

```bash
python ai_file_search.py ask "find my tax return pdf from last year"
```

The script will turn the sentence into search settings and look for the most likely match.

Available providers:

```bash
python ai_file_search.py --provider mock ask "find my python file for web scraping"
python ai_file_search.py --provider ollama ask "find my project plan"
python ai_file_search.py --provider anthropic ask "find my client contract"
```

### 4) Search inside documents

Search for text inside supported docs:

```bash
python ai_file_search.py content "quarterly revenue"
```

Search only under a certain folder:

```bash
python ai_file_search.py content "customer feedback" --under "C:\\Users\\YourName\\Documents"
```

## Supported content types

The content search module reads the following document types:

- `.txt`
- `.md`
- `.csv`
- `.log`
- `.json`
- `.py`
- `.js`
- `.html`
- `.xml`
- `.sql`
- `.pdf`
- `.docx`

## Example usage patterns

### Find a project folder

```bash
python ai_file_search.py find "portfolio"
```

### Find a resume or PDF

```bash
python ai_file_search.py find "resume" --ext .pdf .docx
```

### Search for a term inside notes or reports

```bash
python ai_file_search.py content "budget approval" --under /Users/yourname/Documents
```

### Search for a file without remembering its exact name

```bash
python ai_file_search.py ask "find the spreadsheet with my sales numbers for 2023"
```

## CLI reference

```bash
python ai_file_search.py --help
```

Main commands:

- `index` — build or refresh the local index
- `find` — search for file/folder names
- `ask` — describe a file in plain English
- `content` — search inside document text

### `index` options

```bash
python ai_file_search.py index --roots C:\ D:\
python ai_file_search.py index --include-system
```

### `find` options

```bash
python ai_file_search.py find "report" --type file --ext .pdf .docx
```

### `content` options

```bash
python ai_file_search.py content "team updates" --under /Users/yourname/Documents
```

## Local AI providers

### Mock provider

The default provider is `mock`. It parses your text into likely keywords and extensions without calling an external API.

```bash
python ai_file_search.py --provider mock ask "find my python script for scraping"
```

### Ollama

If you have Ollama installed locally, you can use it for AI understanding:

```bash
export OLLAMA_URL=http://localhost:11434/api/chat
export OLLAMA_MODEL=llama3.2
python ai_file_search.py --provider ollama ask "find my design mockups"
```

### Anthropic

Set the API key and model:

```bash
export ANTHROPIC_MODEL=claude-sonnet-5-5
python ai_file_search.py --provider anthropic ask "find my contract draft"
```

## Notes on privacy

- The file index is stored locally in SQLite.
- The tool does not upload your files.
- In `ask` mode, only the sentence you type is sent to the AI provider.
- The `mock` mode and a local Ollama instance keep the process entirely on your own machine.

## Limitations

- the index needs to be refreshed when new files are added or moved
- very large drives may take time to scan the first time
- content search is limited to supported file types
- PDF and DOCX extraction depends on available libraries and readable file content

## Project structure

```text
Ai-tools/
├── ai_file_search.py
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
└── tests/
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing

Contributions are welcome. If you want to improve the project:

1. Fork the repo
2. Create a feature branch
3. Add tests for your changes
4. Run the project locally
5. Open a pull request

## Future ideas

- Add incremental indexing for faster refreshes
- Add smarter ranking for file search results
- Add support for more document formats
- Add a GUI version for easier desktop use
- Add CLI-configurable default roots/provider preferences

## Author

Built by Nayan.
