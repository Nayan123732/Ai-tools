# AI File Search

This repository contains a Python utility that indexes files and folders on a local machine and enables quick file discovery by exact, partial, fuzzy, and natural-language search.

## Project summary

The project is built to help users find files without needing to remember the exact location or filename. It can also search inside text-based and common document formats to locate keywords and phrases in files.

## Features

- SQLite-backed local indexing
- Exact and partial filename search
- Typo-tolerant fuzzy matching
- Support for files and folders separately
- Natural-language query parsing via built-in mock parsing, Ollama, or Anthropic
- Content search inside supported document types
- Cross-platform support for Windows, macOS, and Linux

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python ai_file_search.py index
python ai_file_search.py find "resume"
```

## Testing

```bash
pytest -q
```

## License

This project is licensed under the MIT License.
