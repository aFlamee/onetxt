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
