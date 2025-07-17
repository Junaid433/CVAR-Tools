# PUBG CVAR Tools

[![Build Status](https://github.com/Junaid433/CVAR-Tools/actions/workflows/build.yml/badge.svg)](https://github.com/Junaid433/CVAR-Tools/actions/workflows/build.yml)

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
