# repo2txt.py

import os
import fnmatch

from utils.ignore_patterns import load_ignore_patterns, is_ignored_by_patterns

def run_repo2txt(script_dir, custom_ignores):
    """
    Läuft das Verzeichnis ab, ignoriert bestimmte Dateien/Ordner
    und schreibt alles in 'response.txt'.
    """
    # .gitignore / .dockerignore laden
    gitignore_path = os.path.join(script_dir, '.gitignore')
    dockerignore_path = os.path.join(script_dir, '.dockerignore')

    ignore_patterns_list = []
    ignore_patterns_list += load_ignore_patterns(gitignore_path)
    ignore_patterns_list += load_ignore_patterns(dockerignore_path)

    output_file = os.path.join(script_dir, 'response.txt')

    with open(output_file, 'w', encoding='utf-8') as out:
        for root, dirs, files in os.walk(script_dir):

            # Wenn du "default_ignore_keywords" integrieren willst, kannst du das
            # hier oder schon in der UI machen. Beispiel:
            default_ignore_keywords = [
                'tmp', 'cache', 'bin', 'build', 'dist', 'out', 'logs',
                'node_modules', 'venv', '.venv', '__pycache__', '.idea', '.vscode'
            ]

            # Ordner filtern
            def should_ignore_dir(d):
                # 1) Versteckte Ordner
                if d.startswith('.'):
                    return True
                # 2) Custom Ignores (vom User)
                if d in custom_ignores:
                    return True
                # 3) Keywords
                d_lower = d.lower()
                return any(keyword in d_lower for keyword in default_ignore_keywords)

            # dirs[:] anpassen, damit os.walk() nicht in ignorierte Ordner steigt
            dirs[:] = [d for d in dirs if not should_ignore_dir(d)]

            for file_name in files:
                # Versteckte Dateien ignorieren
                if file_name.startswith('.'):
                    continue
                # Custom Ignores
                if file_name in custom_ignores:
                    continue

                file_path = os.path.join(root, file_name)
                rel_path = os.path.relpath(file_path, script_dir)

                # Einige beispielhafte Filter:
                file_lower = file_name.lower()
                if ('tmp' in file_lower or
                    'cache' in file_lower or
                    file_name in {'.DS_Store', 'Thumbs.db', '.env'} or
                    file_lower.endswith('.log') or
                    file_lower.endswith('.pyc') or
                    file_lower.endswith('.pyo')):
                    continue

                # Sich selbst ignorieren, falls dieses Skript im selben Ordner liegt
                if rel_path == os.path.basename(__file__):
                    continue

                # response.txt selbst ignorieren
                if rel_path == 'response.txt':
                    continue

                # .gitignore / .dockerignore Pattern-Test
                if is_ignored_by_patterns(rel_path, ignore_patterns_list):
                    continue

                # Ansonsten Inhalt auslesen und in die response.txt schreiben
                out.write(f"\n===== {rel_path} =====\n")
                try:
                    with open(file_path, 'r', encoding='utf-8') as file_content:
                        out.write(file_content.read())
                except UnicodeDecodeError:
                    out.write("[File cannot be read]\n")

    # Könntest du am Ende zurückgeben, wenn du's in der UI brauchst
    return output_file
