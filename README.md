
## README.md


# OneTXT - Directory to Text Converter

I created OneTXT to make coding with an LLM much easier. When you provide an AI with the full source code of a project, you can get way better answers and suggestions. But manually gathering all files? Ain’t nobody got time for that! And that’s where OneTXT comes in.

OneTXT is an open-source tool that converts directory structures into a single, readable text file while respecting ignore rules (like `.gitignore` and `.dockerignore`). It comes with a simple, intuitive graphical interface so anyone—even non-techie users—can get started without fuss.


## Features

- **Ignore Patterns:**  
  OneTXT supports `.gitignore`, `.dockerignore`, and custom ignore rules to filter out unnecessary files automatically.

- **Predefined Presets:**  
  Quickly set up ignore configurations for popular frameworks like React, Next.js, Django, etc. These presets automatically exclude common ignore files and directories for each selected framework.

- **Ignore Settings:**  
  Fine-tune what gets logged by excluding not only hidden files/directories (such as `.git` or `.github`) but also common clutter folders (like `/tmp` or `/log`). This drastically reduces the size of the output file.

- **Additional Ignore:**  
  Missing a specific file or directory from our defaults? Simply add it to the text field—separate multiple entries with a comma for easy customization.

- **Text Output:**  
  Converts all file content into one neatly formatted text file (`response.txt`), ensuring only the most essential files are included.

- **Multi-Platform:**  
  OneTXT runs seamlessly on Windows, macOS, and Linux.

*Each feature is designed to keep the resulting text file as lean and focused as possible, containing only the necessary files for your LLM to work.*

## Installation & Getting Started

### For Non-IT Users

If you just want to click a button and let the magic happen, follow these steps:

1. **Download the Executable:**  
   Head over to the [Releases](https://github.com/aFlamee/onetxt/releases) page and download the latest **OneTXT.exe** for Windows, Mac and Linux.

2. **Security Note:**  
   Your OS might warn you about an "untrusted application" because the app isn’t digitally signed. This is normal—if you trust the source(me 👉🏼👈🏼), go ahead and run it.

### Manual Installation (For the Advanced or for someone with trust issues)
1. **Clone the Repository or Download the ZIP:**  
   Open your terminal (or Command Prompt) and run:
   ```bash
   git clone https://github.com/aFlamee/onetxt.git
   cd onetxt
   ```
   Or just Download the ZIP.

2. **Create a Virtual Environment (Optional but Recommended):**  
   This keeps your Python packages neat and tidy:
   ```bash
   python3 -m venv .venv
   # On Windows:
   .\.venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install the Project in Editable Mode:**
   ```bash
   pip install -e .
   ```

4. **Start the GUI Application:**  
   Launch OneTXT with:
   ```bash
   python -m onetxt
   ```
   The graphical interface will open and you’re ready to go!


## How to Use OneTXT

OneTXT is designed to be as user-friendly as possible. Follow these steps to convert your directory into a clean, focused text file:

1. **Select a Directory:**  
   - Click the **"Browse"** button to choose the folder you want to convert.  
   - The selected directory will be displayed in the input field, so you can double-check it before proceeding.

2. **Configure Ignore Rules:**  
   OneTXT gives you full control over which files and directories are excluded:
   - **Use `.gitignore`/`.dockerignore`:**  
     - Toggle the checkboxes to decide if you want to automatically apply your existing `.gitignore` and `.dockerignore` files. This helps exclude files you already don’t care about.
   - **Predefined Presets:**  
     - Use the **Preset** dropdown to quickly select ignore configurations for popular frameworks (e.g., React, Next.js, Django).  
     - When you choose a preset, OneTXT automatically excludes common files and directories specific to that framework.
   - **Custom Ignore Settings (Checkboxes):**  
     - You’ll see a set of checkboxes for common hidden files and directories (such as `.git`, `.github`, etc.) as well as for typical clutter like `/tmp` or `/log`.  
     - Check or uncheck these options based on what you want to include or ignore in the final output.
   - **Additional Ignore:**  
     - If there are files or directories that aren’t covered by the presets or checkboxes, simply type them into the **Additional Ignore** text field.  
     - Separate multiple entries with a comma. This ensures that even niche files you want to skip will not clutter your output.

3. **Generate Text:**  
   - Once your settings are configured, click the **Generate txt** button.  
   - OneTXT will process the selected directory using your specified ignore rules and compile the remaining file content into one neatly formatted text file.

4. **Output Handling:**  
   - The generated file, named `response.txt`, is saved directly in the selected directory.
   - From the interface, you have options to:
     - **Open the File:** Directly launch `response.txt` to view the result.
     - **Copy to Clipboard:** Quickly copy the entire content for pasting elsewhere.
     - **Open in VSCode:** Launch the file in Visual Studio Code if you prefer working with it there.

With these steps, OneTXT ensures that only the most essential files are included—keeping your text output lean and ready for feeding into your LLM or for further review.

For a deeper dive into how OneTXT works under the hood, check out our [Usage Guide](docs/usage.md).

---

## Contributing

Contributions are welcome! Fork the repo, make your changes, and submit a pull request. No red tape, just code.

---

## Support

You don't have to support me, but thank you for each Supporter ❤️

- ☕ [Buy Me a Coffee](https://buymeacoffee.com/flameeey)
- 💰 [Donate via PayPal](https://paypal.me/flameeey)

---

## License

This project is licensed under the GNU General Public License v3. See the [LICENSE](LICENSE) file for details.
