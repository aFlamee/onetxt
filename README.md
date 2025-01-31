# OneTXT - Directory to Text Converter

I created OneTXT to make coding with an LLM much easier. When you provide an AI with the full source code of a project, you can get way better answers and suggestions. But manually gathering all files? Ain’t nobody got time for that! And that’s where OneTXT comes in.

OneTXT is an open-source tool that converts directory structures into readable text output while respecting ignore rules (e.g., `.gitignore`, `.dockerignore`). It features a GUI for ease of use and supports predefined presets for popular frameworks like SvelteKit, Next.js, React, Django and more.

## Features

- **GUI-Based**: Simple and intuitive interface for selecting directories and configuring ignore rules.
- **Ignore Patterns**: Supports `.gitignore`, `.dockerignore`, and custom ignore rules.
- **Predefined Presets**: Quick setup for popular frameworks (React, Next.js, Django, etc.).
- **Text Output**: Converts file content into a single text file (`response.txt`).
- **Multi-Platform**: Runs on Windows, macOS, and Linux.

---

## Installation

### Download the Executable (Recommended for Non-IT Users)

If you're a normal user who just wants to click a button and let magic happen, you can download the latest **OneTXT.exe** from the [Releases](https://github.com/YOUR_USERNAME/onetxt/releases) section and run it directly on Windows.

⚠ **Security Warning**: Your OS might panic and yell at you about an "untrusted application". This is just because the app is **not digitally signed**—not because it’s dangerous. Signing costs money, and guess what? I’d rather spend that on coffee. If you trust me, just run the app. If not, feel free to check out the code and run it manually (see below).

### Manual Installation (For Developers & Advanced Users)

#### Prerequisites

- **Python 3.8+** (Make sure `tkinter` is installed)

#### 1. Clone the Repository

```bash
git clone https://github.com/aFlamee/onetxt.git
cd onetxt
```

#### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 3. Run the Application

```bash
python -m onetxt
```

This will launch the graphical interface. Boom. Simple.

For more advanced usage instructions and details on how the project is structured, check out the [Usage Guide](docs/usage.md).

---

## Usage

### 1. Select a Directory

Pick a folder that contains the files you want to process.

### 2. Configure Ignore Rules

- **Use .gitignore/.dockerignore**: Because sometimes, you just don’t want all files.
- **Presets**: Got a React or Django project? One click, and we’ll handle the boring stuff for you.
- **Custom Ignores**: Add additional files/folders to ignore. Because customization is life.

### 3. Run the Script

Click the **Generate txt** button to process the directory. The output will be saved as `response.txt` in the directory you just read from.&#x20;

Yes, it's that easy.

### 4. Output Handling

Once the process is complete, you can:

- **Open response.txt** (To go directly to your favorit LLM afterwards)
- **Copy its content to clipboard**
- **Open it in VSCode** (for all the fancy devs out there)

---

## Contributing

Contributions are welcome! Fork the repo, make your changes, and submit a pull request. No red tape. Just code.

---

## Support

If this tool saves you hours of tedious work, consider fueling my caffeine addiction:

- ☕ [Buy Me a Coffee](https://buymeacoffee.com/flameeey)
- 💰 [Donate via PayPal](https://paypal.me/flameeey)

---

## License

This project is licensed under the GNU General Public License v3. See the [LICENSE](LICENSE) file for details.

