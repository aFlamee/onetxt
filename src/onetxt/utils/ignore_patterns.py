# Copyright (C) 2024 Flameeey
# SPDX-License-Identifier: GPL-3.0-only

import os
import fnmatch

def load_ignore_patterns(ignore_file_path):
    patterns = []
    if os.path.isfile(ignore_file_path):
        with open(ignore_file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    if line.endswith('/'):
                        line = line[:-1]
                    patterns.append(line)
    return patterns

def is_ignored_by_patterns(relative_path, ignore_patterns):
    for pattern in ignore_patterns:
        if fnmatch.fnmatch(relative_path, pattern):
            return True
        if fnmatch.fnmatch(os.path.basename(relative_path), pattern):
            return True
    return False