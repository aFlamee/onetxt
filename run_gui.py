import tkinter as tk
from tkinter import ttk, filedialog
import subprocess
import os
import sys

# --------------------
# PRESETS
# --------------------
PRESET_IGNORES = {
    "NextJs": [
        "node_modules", ".next", "package-lock.json", "yarn.lock",
        "pnpm-lock.yaml", "bun.lockb"
    ],
    "SvelteKit": [
        "node_modules", ".svelte-kit", "package-lock.json", "yarn.lock",
        "pnpm-lock.yaml", "bun.lockb"
    ],
    "React": [
        "node_modules", "build", "package-lock.json", "yarn.lock",
        "pnpm-lock.yaml", "bun.lockb"
    ],
    "Ruby on Rails": [
        "tmp", "log", "vendor", "coverage", "node_modules",
        "Gemfile.lock", "package-lock.json", "yarn.lock",
        "pnpm-lock.yaml", "bun.lockb"
    ],
    "Angular": [
        "node_modules", "dist", ".angular",
        "package-lock.json", "yarn.lock",
        "pnpm-lock.yaml", "bun.lockb"
    ],
    "No Preset": []
}

DEFAULT_IGNORE_KEYWORDS = [
    "tmp", "cache", "bin", "build", "dist", "out", "logs",
    "node_modules", "venv", ".venv", "__pycache__", ".idea", ".vscode"
]


def show_executed_feedback():
    global feedback_bar
    status_label.config(text="Script executed.")
    feedback_bar["value"] = 0
    feedback_bar.pack(pady=(0, 10))
    animate_feedback_bar(0)

def animate_feedback_bar(value):
    global feedback_bar
    if value <= 100:
        feedback_bar["value"] = value
        root.after(30, animate_feedback_bar, value + 1)
    else:
        root.after(1000, hide_feedback)

def hide_feedback():
    global feedback_bar
    status_label.config(text="")
    feedback_bar.pack_forget()

def select_directory():
    folder = filedialog.askdirectory(initialdir=os.path.expanduser("~"))
    if folder:
        path_var.set(folder)

def update_preset_label(*_):
    preset = preset_var.get()
    ignores = PRESET_IGNORES.get(preset, [])
    text = f"Ignored by {preset}: {', '.join(ignores)}" if ignores else "No specific ignores."
    preset_info_label.config(text=text)

def run_script():
    btn_clipboard.config(state=tk.DISABLED)
    btn_vscode.config(state=tk.DISABLED)
    open_button.config(state=tk.DISABLED)

    p = path_var.get().strip()
    txt = custom_ignore_var.get().strip()
    user_ignores = []

    if txt and txt != PLACEHOLDER_IGNORE:
        user_ignores = [x.strip() for x in txt.split(',') if x.strip()]

    user_ignores += PRESET_IGNORES.get(preset_var.get(), [])

    # Alle angehakten Default-Keywords hinzufügen
    for kw, var in default_ignore_vars.items():
        if var.get():
            user_ignores.append(kw)

    if p:
        try:
            target = os.path.join(os.path.dirname(__file__), "repo2txt.py")
            subprocess.run([sys.executable, target, p, ",".join(user_ignores)], check=True)
            show_executed_feedback()

            btn_clipboard.config(state=tk.NORMAL)
            btn_vscode.config(state=tk.NORMAL)
            open_button.config(state=tk.NORMAL)
        except subprocess.CalledProcessError as e:
            status_label.config(text=f"Error: {e}")
    else:
        status_label.config(text="Please select a directory first.")

def open_output_file():
    p = path_var.get().strip()
    if not p:
        status_label.config(text="No directory selected.")
        return
    out_file = os.path.join(p, "response.txt")
    if os.path.exists(out_file):
        if sys.platform.startswith("darwin"):
            subprocess.run(["open", out_file])
        elif os.name == "nt":
            os.startfile(out_file)  # type: ignore
        else:
            subprocess.run(["xdg-open", out_file])
    else:
        status_label.config(text="No 'response.txt' found.")

def open_response_in_vscode():
    p = path_var.get().strip()
    if not p:
        status_label.config(text="No directory selected.")
        return
    out_file = os.path.join(p, "response.txt")
    if not os.path.exists(out_file):
        status_label.config(text="No 'response.txt' found.")
        return
    try:
        subprocess.run(["code", out_file], check=True)
    except FileNotFoundError:
        status_label.config(text="VSCode not found or 'code' command not in PATH.")
    except subprocess.CalledProcessError as e:
        status_label.config(text=f"Error opening in VSCode: {e}")


def create_ignore_checkbuttons(parent_frame):
    global default_ignore_vars
    default_ignore_vars = {}

    frame = ttk.Frame(parent_frame)
    frame.pack(fill="x", pady=(10, 15), anchor="w")

    cols = 5  # Zwei Spalten für eine breitere Darstellung
    for index, kw in enumerate(DEFAULT_IGNORE_KEYWORDS):
        var = tk.BooleanVar(value=True)
        default_ignore_vars[kw] = var

        check_frame = ttk.Frame(frame, padding=5, relief="ridge")
        check_frame.grid(row=index // cols, column=index % cols, padx=10, pady=5, sticky="w")

        cbtn = ttk.Checkbutton(check_frame, text=kw, variable=var, style="Modern.TCheckbutton")
        cbtn.pack(side="left", padx=5, pady=2)
    
    return frame

def apply_styles():
    style = ttk.Style()
    style.theme_use("clam")
    
    style.configure("Modern.TCheckbutton",
                    font=("Helvetica", 10, "bold"),
                    background="#2e2e2e", foreground="white",
                    padding=5, borderwidth=2, relief="flat")
    style.map("Modern.TCheckbutton",
              background=[("active", "#555555"), ("!disabled", "#444444")],
              foreground=[("active", "#ffffff"), ("!disabled", "#dddddd")])

def copy_response_to_clipboard():
    p = path_var.get().strip()
    if not p:
        status_label.config(text="No directory selected.")
        return
    out_file = os.path.join(p, "response.txt")
    if not os.path.exists(out_file):
        status_label.config(text="No 'response.txt' found.")
        return
    try:
        with open(out_file, "r", encoding="utf-8") as f:
            content = f.read()
        root.clipboard_clear()
        root.clipboard_append(content)
        status_label.config(text="response.txt content copied to clipboard.")
    except Exception as e:
        status_label.config(text=f"Error copying file content: {e}")

def apply_dark_theme():
    style.theme_use("clam")
    root.configure(bg="#1c1c1c")

    # Checkbutton-Style
    style.configure("Custom.TCheckbutton",
                    background="#1c1c1c", foreground="white",
                    borderwidth=0, highlightthickness=0, relief="flat")

    style.configure("TLabel",
                    background="#1c1c1c", foreground="white",
                    borderwidth=0, relief="flat")
    style.configure("TFrame", background="#1c1c1c")
    style.configure("TEntry",
                    fieldbackground="#3a3a3a", foreground="white",
                    borderwidth=0, relief="flat")
    style.configure("Feedback.Horizontal.TProgressbar",
                    thickness=3,
                    troughcolor="#1c1c1c",
                    background="yellow",
                    bordercolor="#1c1c1c")
    style.configure("TButton",
                    foreground="black",
                    borderwidth=0, relief="flat")
    style.map("TButton",
              background=[
                  ("disabled", "#666666"),
                  ("active", "#e6b800"),
                  ("pressed", "#d6a600"),
                  ("!disabled", "#f0c400")
              ],
              foreground=[
                  ("disabled", "white"),
                  ("active", "black"),
                  ("!disabled", "black")
              ])
    style.configure("TCombobox",
                    fieldbackground="#3a3a3a", foreground="white",
                    borderwidth=0, relief="flat")
    style.map("TCombobox",
              foreground=[("readonly", "white"), ("disabled", "#888")],
              background=[("readonly", "#3a3a3a"), ("disabled", "#3a3a3a")])

    style.configure("Custom.TRadiobutton",
                    background="#1c1c1c", foreground="white",
                    borderwidth=0, highlightthickness=0, relief="flat")
    style.map("Custom.TRadiobutton",
              background=[("active", "#3a3a3a")],
              foreground=[("active", "white")])

    status_label.config(foreground="yellow")
    preset_info_label.config(foreground="yellow")

def apply_light_theme():
    style.theme_use("clam")
    root.configure(bg="#f2f2f2")

    style.configure("Custom.TCheckbutton",
                    background="#f2f2f2", foreground="black",
                    borderwidth=0, highlightthickness=0, relief="flat")

    style.configure("TLabel",
                    background="#f2f2f2", foreground="black",
                    borderwidth=0, relief="flat")
    style.configure("TFrame", background="#f2f2f2")
    style.configure("TEntry",
                    fieldbackground="white", foreground="black",
                    borderwidth=0, relief="flat")
    style.configure("Feedback.Horizontal.TProgressbar",
                    thickness=3,
                    troughcolor="#f2f2f2",
                    background="yellow",
                    bordercolor="#f2f2f2")
    style.configure("TButton",
                    foreground="white",
                    borderwidth=0, relief="flat")
    style.map("TButton",
              background=[
                  ("disabled", "#dddddd"),
                  ("active", "#0052cc"),
                  ("pressed", "#003d99"),
                  ("!disabled", "#007bff")
              ],
              foreground=[
                  ("disabled", "black"),
                  ("active", "white"),
                  ("!disabled", "white")
              ])
    style.configure("TCombobox",
                    fieldbackground="white", foreground="black",
                    borderwidth=0, relief="flat")
    style.map("TCombobox",
              foreground=[("readonly", "black"), ("disabled", "#666")],
              background=[("readonly", "#f2f2f2"), ("disabled", "#f2f2f2")])

    style.configure("Custom.TRadiobutton",
                    background="#f2f2f2", foreground="black",
                    borderwidth=0, highlightthickness=0, relief="flat")
    style.map("Custom.TRadiobutton",
              background=[("active", "#cccccc")],
              foreground=[("active", "black")])

    status_label.config(foreground="blue")
    preset_info_label.config(foreground="blue")

def switch_theme():
    if theme_var.get() == "Dark":
        apply_dark_theme()
    else:
        apply_light_theme()

def on_ignore_focus_in(_):
    if custom_ignore_var.get() == PLACEHOLDER_IGNORE:
        entry_ignore.delete(0, "end")
        if theme_var.get() == "Dark":
            entry_ignore.config(foreground="white")
        else:
            entry_ignore.config(foreground="black")

def on_ignore_focus_out(_):
    if not custom_ignore_var.get():
        entry_ignore.insert(0, PLACEHOLDER_IGNORE)
        entry_ignore.config(foreground="#888")

def main():
    global root, style
    global path_var, custom_ignore_var, preset_var
    global preset_info_label, status_label
    global btn_clipboard, btn_vscode, open_button
    global theme_var, entry_ignore
    global feedback_bar
    global PLACEHOLDER_IGNORE
    global default_ignore_vars

    root = tk.Tk()
    root.title("aFlamee - OneTXT")
    root.geometry("750x550")
    root.resizable(False, False)

    style = ttk.Style(root)
    style.theme_use("clam")

    heading_frame = ttk.Frame(root, padding="10")
    heading_frame.pack(fill="x")
    lbl_heading = ttk.Label(heading_frame, text="Welcome to OneTXT!", font=("Helvetica", 14, "bold"))
    lbl_heading.pack(side="left")

    theme_var = tk.StringVar(value="Dark")
    theme_switch_frame = ttk.Frame(heading_frame)
    theme_switch_frame.pack(side="right")
    ttk.Label(theme_switch_frame, text="Theme:").pack(side="left", padx=(0,5))

    dark_rb = ttk.Radiobutton(theme_switch_frame, text="Dark", variable=theme_var, value="Dark",
                              command=switch_theme, takefocus=False, style="Custom.TRadiobutton")
    dark_rb.pack(side="left", padx=5)
    light_rb = ttk.Radiobutton(theme_switch_frame, text="White", variable=theme_var, value="White",
                               command=switch_theme, takefocus=False, style="Custom.TRadiobutton")
    light_rb.pack(side="left", padx=5)

    main_frame = ttk.Frame(root, padding="10")
    main_frame.pack(fill="both", expand=True)

    note_label = ttk.Label(main_frame, text="Note: .gitignore and .dockerignore are also used by default.")
    note_label.pack(anchor="w", pady=(0,10))

    dir_frame = ttk.Frame(main_frame)
    dir_frame.pack(fill="x", pady=5)
    ttk.Label(dir_frame, text="Select Directory:").pack(side="left", padx=(0,5))
    path_var = tk.StringVar()
    entry_path = ttk.Entry(dir_frame, textvariable=path_var, width=40)
    entry_path.pack(side="left", expand=True, fill="x")
    b_browse = ttk.Button(dir_frame, text="Browse", command=select_directory)
    b_browse.pack(side="left", padx=5)

    # Schönes LabelFrame für die Default-Ignores
    default_box = ttk.LabelFrame(main_frame, text="Default Ignores (Check/Uncheck as you like)")
    default_box.pack(fill="x", pady=(5, 10), anchor="w")

    # Dictionary: Keyword -> BooleanVar
    default_ignore_vars = {}
    col_count = 0
    row_count = 0
    max_per_col = 5  # 5 Einträge pro Spalte

    # LabelFrame für die Default-Ignores mit modernisiertem Look
    default_box = ttk.LabelFrame(main_frame, text="Default Ignores (Check/Uncheck as you like)", padding=10)
    default_box.pack(fill="x", pady=(10, 15), anchor="w")
    create_ignore_checkbuttons(default_box)  # Modernisierte Checkbuttons

    preset_frame = ttk.Frame(main_frame)
    preset_frame.pack(fill="x", pady=5)
    ttk.Label(preset_frame, text="Technology Preset:").pack(side="left", padx=(0,5))
    preset_var = tk.StringVar(value="No Preset")
    combo_presets = ttk.Combobox(preset_frame, textvariable=preset_var, values=list(PRESET_IGNORES.keys()),
                                 width=20, state="readonly")
    combo_presets.pack(side="left")
    combo_presets.bind("<<ComboboxSelected>>", update_preset_label)

    preset_info_label = ttk.Label(main_frame, text="No specific ignores.", wraplength=560)
    preset_info_label.pack(pady=(5,0))

    PLACEHOLDER_IGNORE = "E.g. .env, secrets"
    ttk.Label(main_frame, text="Additional Ignores (comma-separated):").pack(anchor="w", pady=(15,0))
    custom_ignore_var = tk.StringVar()
    global entry_ignore
    entry_ignore = ttk.Entry(main_frame, textvariable=custom_ignore_var, width=40)
    entry_ignore.pack(anchor="w")
    entry_ignore.insert(0, PLACEHOLDER_IGNORE)
    entry_ignore.config(foreground="#888")
    entry_ignore.bind("<FocusIn>", on_ignore_focus_in)
    entry_ignore.bind("<FocusOut>", on_ignore_focus_out)

    btn_frame = ttk.Frame(main_frame)
    btn_frame.pack(fill="x", pady=15)
    b_run = ttk.Button(btn_frame, text="Run Script", command=run_script)
    b_run.pack(side="left")

    global btn_clipboard
    btn_clipboard = ttk.Button(btn_frame, text="Copy to Clipboard", command=copy_response_to_clipboard, state=tk.DISABLED)
    btn_clipboard.pack(side="left", padx=5)

    global btn_vscode
    btn_vscode = ttk.Button(btn_frame, text="Open in VSCode", command=open_response_in_vscode, state=tk.DISABLED)
    btn_vscode.pack(side="left", padx=5)

    global open_button
    open_button = ttk.Button(btn_frame, text="Open response.txt", command=open_output_file, state=tk.DISABLED)
    open_button.pack(side="left", padx=5)

    global status_label
    status_label = ttk.Label(main_frame, text="")
    status_label.pack(anchor="w")

    global feedback_bar
    feedback_bar = ttk.Progressbar(main_frame,
                                   style="Feedback.Horizontal.TProgressbar",
                                   orient="horizontal",
                                   mode="determinate",
                                   maximum=100,
                                   value=0)
    feedback_bar.pack_forget()

    update_preset_label()
    apply_dark_theme()

    root.mainloop()

if __name__ == "__main__":
    main()