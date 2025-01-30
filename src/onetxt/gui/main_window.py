import tkinter as tk
from tkinter import ttk, filedialog
import subprocess
import os
import sys
import webbrowser

from ..core.processor import run_onetxt
from ..utils.presets import PRESET_IGNORES, HIDDEN_IGNORE_KEYWORDS, NON_HIDDEN_IGNORE_KEYWORDS

root = None
style = None
path_var = None
custom_ignore_var = None
preset_var = None
preset_info_label = None
status_label = None
btn_clipboard = None
btn_vscode = None
open_button = None
theme_var = None
entry_ignore = None
feedback_bar = None
use_gitignore_var = None
use_dockerignore_var = None

PLACEHOLDER_IGNORE = "E.g. .env, secrets"
default_ignore_vars = {}
ignore_all_hidden_var = None
hidden_checkboxes = []

def open_donation_link():
    webbrowser.open("https://buymeacoffee.com/flameeey")

def open_donation_link_paypal():
    webbrowser.open("https://paypal.me/flameeey")

def set_status(msg):
    pass

def set_buttons_state(state):
    btn_clipboard.config(state=state)
    btn_vscode.config(state=state)
    open_button.config(state=state)

def hide_feedback():
    pass

def animate_feedback_bar(value):
    if value <= 100:
        feedback_bar["value"] = value
        root.after(30, animate_feedback_bar, value + 1)
    else:
        root.after(1000, hide_feedback)

def show_executed_feedback():
    feedback_frame = ttk.Frame(main_frame)
    feedback_frame.pack(pady=(5,0), anchor="w", fill="x")
    
    status_label = ttk.Label(
        feedback_frame, 
        text="✓ Script executed", 
        foreground="#4CAF50" if theme_var.get() == "Dark" else "#2E7D32"
    )
    status_label.pack(anchor="w")
    
    feedback_bar = ttk.Progressbar(
        feedback_frame,
        style="Feedback.Horizontal.TProgressbar",
        orient="horizontal",
        mode="determinate",
        maximum=100,
        value=100
    )
    feedback_bar.pack(pady=(2,5), fill="x")

    def animate(current_value):
        if current_value > 0:
            feedback_bar["value"] = current_value
            feedback_frame.after(50, animate, current_value - 1)
        else:
            feedback_frame.destroy()

    animate(100) 


def select_directory():
    folder = filedialog.askdirectory(initialdir=os.path.expanduser("~"))
    if folder:
        path_var.set(folder)

def update_preset_label(*_):
    preset = preset_var.get()
    ignores = PRESET_IGNORES.get(preset, [])
    text = f"Ignored by {preset}:\n{', '.join(ignores)}" if ignores else "No specific ignores."
    preset_info_label.config(text=text)

def run_script():
    set_buttons_state(tk.DISABLED)
    p = path_var.get().strip()
    txt = custom_ignore_var.get().strip()
    user_ignores = []
    
    if ignore_all_hidden_var.get():
        user_ignores.append(".*")
    
    if txt and txt != PLACEHOLDER_IGNORE:
        user_ignores = [x.strip() for x in txt.split(',') if x.strip()]
    user_ignores += PRESET_IGNORES.get(preset_var.get(), [])
    for kw, var in default_ignore_vars.items():
        if var.get():
            user_ignores.append(kw)
    if p:
        try:
            use_gitignore = use_gitignore_var.get()
            use_dockerignore = use_dockerignore_var.get()
            
            run_onetxt(p, user_ignores, use_gitignore, use_dockerignore)
            show_executed_feedback()
            set_buttons_state(tk.NORMAL)
        except subprocess.CalledProcessError as e:
            set_status(f"Error: {e}")
    else:
        set_status("Please select a directory first.")

def get_response_file():
    p = path_var.get().strip()
    if not p:
        set_status("No directory selected.")
        return None, None
    out_file = os.path.join(p, "response.txt")
    if not os.path.exists(out_file):
        set_status("No 'response.txt' found.")
        return p, None
    return p, out_file

def open_output_file():
    p, out_file = get_response_file()
    if not out_file:
        return
    if sys.platform.startswith("darwin"):
        subprocess.run(["open", out_file])
    elif os.name == "nt":
        os.startfile(out_file)
    else:
        subprocess.run(["xdg-open", out_file])

def open_response_in_vscode():
    p, out_file = get_response_file()
    if not out_file:
        return
    try:
        subprocess.run(["code", out_file], check=True)
    except FileNotFoundError:
        set_status("VSCode not found or 'code' command not in PATH.")
    except subprocess.CalledProcessError as e:
        set_status(f"Error opening in VSCode: {e}")

def copy_response_to_clipboard():
    p, out_file = get_response_file()
    if not out_file:
        return
    try:
        with open(out_file, "r", encoding="utf-8") as f:
            content = f.read()
        root.clipboard_clear()
        root.clipboard_append(content)
        set_status("response.txt content copied to clipboard.")
    except Exception as e:
        set_status(f"Error copying file content: {e}")

def create_ignore_checkbuttons(parent_frame):
    global ignore_all_hidden_var, hidden_checkboxes, default_ignore_vars
    global use_gitignore_var, use_dockerignore_var 
    
    frame = ttk.Frame(parent_frame)
    frame.pack(fill="x", pady=(5, 10))

    ignore_files_frame = ttk.Frame(frame)
    ignore_files_frame.pack(anchor="w", pady=5, fill="x")

    use_gitignore_var = tk.BooleanVar(value=True)
    ttk.Checkbutton(
        ignore_files_frame,
        text="Auto-apply .gitignore rules",
        variable=use_gitignore_var
    ).pack(side="left", padx=10)
    
    use_dockerignore_var = tk.BooleanVar(value=True)
    ttk.Checkbutton(
        ignore_files_frame,
        text="Auto-apply .dockerignore rules",
        variable=use_dockerignore_var
    ).pack(side="left", padx=10)

    ignore_all_hidden_var = tk.BooleanVar(value=False)
    ttk.Checkbutton(frame,
                    text="Ignore ALL hidden files/dirs (.*)",
                    variable=ignore_all_hidden_var,
                    style="Bold.TCheckbutton").pack(anchor="w", pady=5)

    grid_frame = ttk.Frame(frame)
    grid_frame.pack(fill="x")

    ttk.Label(grid_frame, 
             text="Common hidden:", 
             style="Sub.TLabel").grid(row=0, column=0, sticky="nw", padx=5, pady=2)
    
    hidden_frame = ttk.Frame(grid_frame)
    hidden_frame.grid(row=0, column=1, sticky="w")
    
    MAX_COLS = 7
    current_row = 0
    current_col = 0
    
    for idx, kw in enumerate(HIDDEN_IGNORE_KEYWORDS):
        var = tk.BooleanVar(value=True)
        default_ignore_vars[kw] = var
        cb = ttk.Checkbutton(
            hidden_frame, 
            text=kw.replace(".", "") if kw.startswith(".") else kw,
            variable=var
        )
        cb.grid(
            row=current_row, 
            column=current_col, 
            padx=3,
            pady=1, 
            sticky="w"
        )
        hidden_checkboxes.append(cb)
        
        current_col += 1
        if current_col >= MAX_COLS:
            current_row += 1
            current_col = 0

    ttk.Label(grid_frame, 
             text="Other common:", 
             style="Sub.TLabel").grid(row=1, column=0, sticky="nw", padx=5, pady=2)
    
    non_hidden_frame = ttk.Frame(grid_frame)
    non_hidden_frame.grid(row=1, column=1, sticky="w")
    
    current_row = 0
    current_col = 0
    
    for idx, kw in enumerate(NON_HIDDEN_IGNORE_KEYWORDS):
        var = tk.BooleanVar(value=True)
        default_ignore_vars[kw] = var
        cb = ttk.Checkbutton(
            non_hidden_frame, 
            text=kw, 
            variable=var
        )
        cb.grid(
            row=current_row, 
            column=current_col, 
            padx=3,
            pady=1, 
            sticky="w"
        )
        
        current_col += 1
        if current_col >= MAX_COLS:
            current_row += 1
            current_col = 0

    style.configure("Bold.TCheckbutton", 
                   font=("Segoe UI", 9, "bold"),
                   padding=2)
    style.configure("Sub.TLabel", 
                   font=("Segoe UI", 9, "italic"),
                   padding=2)
    
    def toggle_hidden_cb(*_):
        state = tk.NORMAL if not ignore_all_hidden_var.get() else tk.DISABLED
        for cb in hidden_checkboxes:
            cb.configure(state=state)
    
    ignore_all_hidden_var.trace_add("write", toggle_hidden_cb)
    return frame

def apply_styles():
    style.theme_use("clam")
    style.configure(".", 
                    font=("Segoe UI", 10),
                    relief="flat")
    
    style.configure("TButton", 
                    padding=6,
                    borderwidth=0)
    
    style.map("TButton",
              background=[
                  ("disabled", "#666666"),
                  ("active", "#404040"),
                  ("pressed", "#303030"),
                  ("!disabled", "#2d2d2d")
              ],
              foreground=[
                  ("disabled", "#888"),
                  ("active", "white"),
                  ("!disabled", "white")
              ])
    
    style.configure("TEntry",
                    padding=5,
                    insertwidth=1)
    
    style.configure("TCheckbutton",
                    padding=4,
                    indicatorsize=14)
    
    style.configure("Feedback.Horizontal.TProgressbar",
        thickness=2,
        troughcolor="",
        background="#4CAF50",
        troughrelief="flat")

    style.configure("TCheckbutton",
                    padding=4,
                    indicatorsize=14,
                    darkcolor='#1a1a1a', 
                    lightcolor='#1a1a1a')

def apply_dark_theme():
    root.configure(bg="#1a1a1a")
    style.configure(".", 
                    background="#1a1a1a",
                    foreground="white",
                    fieldbackground="#2a2a2a")
    
    style.map("TEntry",
              fieldbackground=[("!disabled", "#2a2a2a")],
              foreground=[("!disabled", "white")])
    
    style.configure("TLabel", background="#1a1a1a")
    style.configure("TFrame", background="#1a1a1a")

    style.configure("TCombobox",
                    fieldbackground="#2a2a2a",
                    background="#2a2a2a",
                    foreground="white",
                    arrowcolor="white",
                    insertcolor="white",
                    bordercolor="#404040",
                    darkcolor="#2a2a2a",
                    lightcolor="#2a2a2a")
    
    style.map("TCombobox",
              fieldbackground=[("readonly", "#2a2a2a")],
              selectbackground=[("!focus", "#404040")],
              selectforeground=[("!focus", "white")],
              background=[("active", "#404040")])
    
    root.option_add("*TCombobox*Listbox*Background", "#2a2a2a")
    root.option_add("*TCombobox*Listbox*Foreground", "white")
    root.option_add("*TCombobox*Listbox*selectBackground", "#404040")
    root.option_add("*TCombobox*Listbox*selectForeground", "white")

    style.map("TCheckbutton",
              background=[
                  ('active', '#2a2a2a'),
                  ('!disabled', '#1a1a1a') 
              ],
              foreground=[
                  ('active', 'white'), 
                  ('!disabled', 'white')
              ])

def apply_light_theme():
    root.configure(bg="#ffffff")
    style.configure(".", 
                    background="#ffffff",
                    foreground="black",
                    fieldbackground="#f8f8f8")
    
    style.map("TButton",
              background=[
                  ("disabled", "#dddddd"),
                  ("active", "#e0e0e0"),
                  ("pressed", "#d0d0d0"),
                  ("!disabled", "#f0f0f0")
              ],
              foreground=[
                  ("disabled", "#888"),
                  ("active", "black"),
                  ("!disabled", "black")
              ])
    
    style.map("TEntry",
              fieldbackground=[("!disabled", "#f8f8f8")],
              foreground=[("!disabled", "black")])
    
    style.configure("TLabel", background="#ffffff")
    style.configure("TFrame", background="#ffffff")
    style.configure("TCombobox",
                    fieldbackground="#f8f8f8",
                    background="#ffffff",
                    foreground="black",
                    arrowcolor="black",
                    insertcolor="black",
                    bordercolor="#cccccc",
                    darkcolor="#f8f8f8",
                    lightcolor="#f8f8f8")
    
    style.map("TCombobox",
              fieldbackground=[("readonly", "#f8f8f8")],
              selectbackground=[("!focus", "#e0e0e0")],
              selectforeground=[("!focus", "black")],
              background=[("active", "#e0e0e0")])
    
    root.option_add("*TCombobox*Listbox*Background", "#ffffff")
    root.option_add("*TCombobox*Listbox*Foreground", "black")
    root.option_add("*TCombobox*Listbox*selectBackground", "#e0e0e0")
    root.option_add("*TCombobox*Listbox*selectForeground", "black")
    
    style.configure("Feedback.Horizontal.TProgressbar",
        background="#2E7D32") 
    style.map("TCheckbutton",
              background=[
                  ('active', '#e0e0e0'), 
                  ('!disabled', '#ffffff') 
              ],
              foreground=[
                  ('active', 'black'), 
                  ('!disabled', 'black') 
              ])

def switch_theme():
    if theme_var.get() == "Dark":
        apply_dark_theme()
    else:
        apply_light_theme()

def on_ignore_focus_in(_):
    if custom_ignore_var.get() == PLACEHOLDER_IGNORE:
        entry_ignore.delete(0, "end")
        entry_ignore.config(foreground="white" if theme_var.get() == "Dark" else "black")

def on_ignore_focus_out(_):
    if not custom_ignore_var.get():
        entry_ignore.insert(0, PLACEHOLDER_IGNORE)
        entry_ignore.config(foreground="#888")

def run_ui():
    global root, style
    global path_var, custom_ignore_var, preset_var
    global preset_info_label, status_label
    global btn_clipboard, btn_vscode, open_button
    global theme_var, entry_ignore
    global main_frame

    root = tk.Tk()
    root.title("OneTXT - Directory to Text")
    root.geometry("900x700")
    root.resizable(False, False)

    style = ttk.Style(root)
    apply_styles()

    main_frame = ttk.Frame(root, padding=10)
    main_frame.pack(fill="both", expand=True)

    header_frame = ttk.Frame(main_frame)
    header_frame.pack(fill="x", pady=(0, 10))
    
    ttk.Label(header_frame, 
              text="OneTXT", 
              font=("Segoe UI", 16, "bold")).pack(side="left")
    
    theme_var = tk.StringVar(value="Dark")
    theme_frame = ttk.Frame(header_frame)
    theme_frame.pack(side="right")
    ttk.Radiobutton(theme_frame, text="☀", variable=theme_var, 
                    value="White", command=switch_theme).pack(side="right", padx=2)
    ttk.Radiobutton(theme_frame, text="🌙", variable=theme_var,
                    value="Dark", command=switch_theme).pack(side="right", padx=2)

    dir_frame = ttk.Frame(main_frame)
    dir_frame.pack(fill="x", pady=5)
    ttk.Label(dir_frame, text="Project Folder:").pack(side="left")
    path_var = tk.StringVar()
    entry_path = ttk.Entry(dir_frame, textvariable=path_var)
    entry_path.pack(side="left", expand=True, fill="x", padx=5)
    ttk.Button(dir_frame, text="Browse", command=select_directory, width=8).pack(side="left")

    preset_frame = ttk.Frame(main_frame)
    preset_frame.pack(fill="x", pady=5)
    ttk.Label(preset_frame, text="Preset:").pack(side="left")
    preset_var = tk.StringVar(value="No Preset")
    combo_presets = ttk.Combobox(preset_frame, 
                               textvariable=preset_var, 
                               values=list(PRESET_IGNORES.keys()),
                               width=18,
                               state="readonly")
    combo_presets.pack(side="left", padx=5)
    combo_presets.bind("<<ComboboxSelected>>", update_preset_label)

    preset_info_label = ttk.Label(main_frame, wraplength=560)
    preset_info_label.pack(pady=(0, 5))

    default_box = ttk.LabelFrame(main_frame, text="Ignore Settings", padding=5)
    default_box.pack(fill="x", pady=5)
    create_ignore_checkbuttons(default_box)

    ttk.Label(main_frame, text="Additional Ignores:").pack(anchor="w", pady=(5, 0))
    custom_ignore_var = tk.StringVar()
    entry_ignore = ttk.Entry(main_frame, textvariable=custom_ignore_var)
    entry_ignore.pack(fill="x", pady=2)
    entry_ignore.insert(0, PLACEHOLDER_IGNORE)
    entry_ignore.config(foreground="#888")
    entry_ignore.bind("<FocusIn>", on_ignore_focus_in)
    entry_ignore.bind("<FocusOut>", on_ignore_focus_out)

    btn_frame = ttk.Frame(main_frame)
    btn_frame.pack(fill="x", pady=10)
    ttk.Button(btn_frame, text="Generate txt", command=run_script).pack(side="left")
    btn_clipboard = ttk.Button(btn_frame, text="Copy to Clipboard", command=copy_response_to_clipboard, state=tk.DISABLED)
    btn_clipboard.pack(side="left", padx=5)
    btn_vscode = ttk.Button(btn_frame, text="Open in VSCode", command=open_response_in_vscode, state=tk.DISABLED)
    btn_vscode.pack(side="left", padx=5)

    open_button = ttk.Button(btn_frame, text="Open File", command=open_output_file, state=tk.DISABLED)
    open_button.pack(side="left", padx=5)

    support_frame = ttk.Frame(main_frame)
    support_frame.pack(fill="x", pady=(10, 0))
    ttk.Button(support_frame, text="☕️ Buy Me a Coffee", command=open_donation_link).pack(side="right", padx=2)
    ttk.Button(support_frame, text="🅿 PayPal", command=open_donation_link_paypal).pack(side="right", padx=2)

    status_label = ttk.Label(main_frame)
    status_label.pack(anchor="w", pady=(5, 0))

    update_preset_label()
    switch_theme()
    root.mainloop()