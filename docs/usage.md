# OneTXT – Usage Guide

Welcome to the OneTXT Usage Guide! This document is for those who love to look behind the scenes and understand how the magic happens. Grab a cup of coffee, sit back, and enjoy this deep dive into the inner workings of OneTXT.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Installation & Execution (Advanced)](#installation--execution-advanced)
- [The Fancy GUI Explained](#the-fancy-gui-explained)
- [Technical Details](#technical-details)
- [Tips & Tricks](#tips--tricks)
- [Troubleshooting](#troubleshooting)
- [Release & Versioning](#release--versioning)
- [Conclusion](#conclusion)

---

## Project Overview

OneTXT transforms a project folder into a single, well-formatted text file. It’s designed not only to simplify code reviews and debugging but also to help feed your favorite language models with all the context they need. Essentially, it’s like having a digital assistant that tidies up your code—so you don’t have to!

---

## Project Structure

Here’s how OneTXT is organized:

```
onetxt/
├── docs/
│   └── usage.md       # This guide – We are here
├── src/
│   └── onetxt/
│       ├── __init__.py        # Initializes the package
│       ├── __main__.py        # Entry point when running with Python
│       ├── core/
│       │   └── processor.py   # The heart of the file-to-text conversion
│       ├── gui/
│       │   └── main_window.py # The graphical user interface built with Tkinter
│       └── utils/
│           ├── ignore_patterns.py   # Handles ignore rules
│           └── presets.py           # Predefined ignore lists for popular frameworks
└── setup.py         # Setup script to install OneTXT
```

Think of each folder as a well-organized drawer in a toolbox—everything has its place to keep the magic running smoothly.

---

## Installation & Execution

### Installation

For those who want to get their hands dirty:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/aFlamee/onetxt.git
   cd onetxt
   ```

2. **Set Up a Virtual Environment:**
   ```bash
   python3 -m venv .venv
   # On Windows, use: .\.venv\Scripts\activate
   source .venv/bin/activate  
   ```

3. **Install Dependencies in Editable Mode:**
   ```bash
   pip install -e .
   ```

4. **Launch the Application:**
   ```bash
   python -m onetxt
   ```


## The Fancy GUI Explained

When you launch OneTXT, you’re greeted by a clean, intuitive interface:

- **Directory Selection:**  
  The "Browse" button lets you select the project folder to convert.
  
- **Ignore Options:**  
  Choose whether to automatically incorporate `.gitignore` and `.dockerignore` rules or set your own custom ignores.
  
- **Presets:**  
  For popular frameworks, pick a preset and let OneTXT handle the boring details.
  
- **Generate Text:**  
  Hit "Generate txt" and watch as your entire directory is transformed into a beautifully formatted text file.

---

## Technical Details

- **Core Conversion Logic:**  
  In `src/onetxt/core/processor.py`, the tool scans your directory, reads the files, and compiles them into a single text file. This module handles file filtering based on ignore rules and presets.

- **Graphical User Interface:**  
  The GUI in `src/onetxt/gui/main_window.py` is built with Tkinter, providing an accessible interface without the overhead of a web application.

- **Utility Modules:**  
  Located in `src/onetxt/utils/`, these modules manage ignore patterns and preset configurations, ensuring only the relevant files are processed.
