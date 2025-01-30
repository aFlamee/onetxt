# README – Installation & Usage

## Prerequisites

- **Python 3.9+** (make sure `tkinter` is included, which is typically part of standard installations)
- Operating System: macOS, Windows, or Linux

## 1. Install Python 3

### macOS
1. **Install Homebrew** (if not already installed):  
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2. **Install Python 3**:  
   ```bash
   brew install python@3.9
   ```
   *(Exact version may differ based on what is currently available.)*

### Windows
1. Go to the [official Python website](https://www.python.org/downloads/).
2. Download the latest Python 3.x installer for Windows.
3. Run the installer and select **“Add Python to PATH”** to allow Python commands in your terminal.
4. After installation, verify the installation in PowerShell or cmd:
   ```bash
   python --version
   ```
   You should see something like `Python 3.x.x`.

### Linux (Debian/Ubuntu-based)
1. Open your terminal.
2. Run the following:
   ```bash
   sudo apt-get update
   sudo apt-get install python3 python3-pip
   ```
3. Verify the version:
   ```bash
   python3 --version
   ```

*(For other distributions like Fedora, openSUSE, etc., use your package manager, such as `dnf`, `yum`, or `zypper`.)*

---

## 2. Clone or Download the Project
1. Download the repository or clone it into a folder of your choice.
2. Navigate into the project directory.

---

## 3. Install Dependencies
A `requirements.txt` file is included in the project. Make sure you’re in the project folder, then run:

### macOS / Linux
```bash
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

### Windows
```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

*(If you prefer using “python3” on Windows, ensure that the appropriate alias is set during the Python installation.)*

---

## 4. Run the Application
After the dependencies have been successfully installed, start the application:

### macOS / Linux
```bash
python3 main.py
```

### Windows
```bash
python main.py
```

- A **GUI window** titled *“aFlamee - rep2txt - Repository -> text”* should appear.
- Select your desired directory, configure ignore settings, and run the script.

---

## 5. Brief Overview
1. **Select a Directory** – for example, your repository folder.
2. **Default Ignores** – check/uncheck known folders/files (e.g., `node_modules`, `.idea`).
3. **Presets** – choose a technology preset (e.g., React, NextJs). This will automatically add relevant ignore patterns.
4. **Additional Ignores** – enter your custom ignores (comma-separated).
5. **Run Script** – click **“Run Script”**.
6. When the process completes, you can:
   - **Open** `response.txt`
   - **Copy** the contents to your clipboard
   - **Open** the file in **VSCode** (if `code` is available on your PATH)

---

## Known Issues
- If **VSCode** doesn’t open via the `code` command, ensure VSCode is installed correctly and [set up for command line usage](https://code.visualstudio.com/docs/setup/mac#_launching-from-the-command-line).
- On macOS, opening `response.txt` via the `open` command may fail if file access permissions are restricted. You can open it directly from Finder as a workaround.

---

### Enjoy using the application!

