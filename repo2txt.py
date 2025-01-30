import sys
import os
import fnmatch

def load_ignore_patterns(ignore_file_path):
    patterns = []
    if os.path.isfile(ignore_file_path):
        with open(ignore_file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                patterns.append(line)
    return patterns

def is_ignored_by_patterns(relative_path, ignore_patterns):
    for pattern in ignore_patterns:
        if fnmatch.fnmatch(relative_path, pattern):
            return True
    return False

def main():

    if len(sys.argv) > 1:
        script_dir = sys.argv[1]
    else:
        script_dir = os.path.dirname(os.path.abspath(__file__))

    if len(sys.argv) > 2:
        custom_ignores = sys.argv[2].split(',')
        custom_ignores = [x.strip() for x in custom_ignores if x.strip()]
    else:
        custom_ignores = []

    # load .gitignore / .dockerignore
    gitignore_path = os.path.join(script_dir, '.gitignore')
    dockerignore_path = os.path.join(script_dir, '.dockerignore')

    ignore_patterns_list = []
    ignore_patterns_list += load_ignore_patterns(gitignore_path)
    ignore_patterns_list += load_ignore_patterns(dockerignore_path)

    output_file = os.path.join(script_dir, 'response.txt')

    with open(output_file, 'w', encoding='utf-8') as out:
        for root, dirs, files in os.walk(script_dir):

            default_ignore_keywords = [
                'tmp', 'cache', 'bin', 'build', 'dist', 'out', 'logs',
                'node_modules', 'venv', '.venv', '__pycache__', '.idea', '.vscode'
            ]
            
            def should_ignore_dir(d):
                # 1) Hidden folders -> ignore
                if d.startswith('.'):
                    return True
                # 2) In custom_ignore included?
                if d in custom_ignores:
                    return True
                # 3) Custom-User-Keywords
                d_lower = d.lower()
                return any(keyword in d_lower for keyword in default_ignore_keywords)

            dirs[:] = [d for d in dirs if not should_ignore_dir(d)]

            for file_name in files:
                if file_name.startswith('.'):
                    continue
                if file_name in custom_ignores:
                    continue

                file_path = os.path.join(root, file_name)
                rel_path = os.path.relpath(file_path, script_dir)

                file_lower = file_name.lower()
                if ('tmp' in file_lower or
                    'cache' in file_lower or
                    file_name in {'.DS_Store', 'Thumbs.db', '.env'} or
                    file_lower.endswith('.log') or
                    file_lower.endswith('.pyc') or
                    file_lower.endswith('.pyo')):
                    continue

                if rel_path == os.path.basename(__file__):
                    continue
                if rel_path == 'response.txt':
                    print(f"Done! reponsefile can be found here: {output_file}")
                    continue

                # .gitignore / .dockerignore
                if is_ignored_by_patterns(rel_path, ignore_patterns_list):
                    continue

                out.write(f"\n===== {rel_path} =====\n")
                try:
                    with open(file_path, 'r', encoding='utf-8') as file_content:
                        out.write(file_content.read())
                except UnicodeDecodeError:
                    out.write("[File cannot be read]\n")

if __name__ == '__main__':
    main()
