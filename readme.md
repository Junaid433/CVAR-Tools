# PUBG CVAR Tools

[![PyPI version](https://img.shields.io/pypi/v/pubg-cvar-tools.svg)](https://pypi.org/project/pubg-cvar-tools/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Build Status](https://github.com/yourusername/pubg-cvar-tools/actions/workflows/ci.yml/badge.svg)](https://github.com/yourusername/pubg-cvar-tools/actions/workflows/ci.yml)

---

A Python toolkit with a PySide6 GUI to **encrypt** and **decrypt** PUBG Mobile CVAR configuration strings. Useful for developers and enthusiasts managing PUBG Mobile client config files.

---

## Features

- **Encrypt** plaintext CVAR lines into PUBG Mobile hex strings.
- **Decrypt** PUBG Mobile CVAR hex strings back to human-readable format.
- Easy to use GUI with **export to text file** functionality.
- Supports batch processing of multiple CVAR lines.
- Robust error handling and validation.
- Fully tested with `pytest`.
- Cross-platform (Linux, Windows, macOS) thanks to Python & Qt.

---

## Installation

Ensure you have Python 3.8+ installed. Then:

```bash
git clone https://github.com/yourusername/pubg-cvar-tools.git
cd pubg-cvar-tools
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
