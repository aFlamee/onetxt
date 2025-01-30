import os
import fnmatch
from utils.ignore_patterns import load_ignore_patterns, is_ignored_by_patterns


def load_gitignore_patterns_from_hierarchy(current_path, base_dir, use_gitignore, use_dockerignore):
    patterns = []
    current_dir = os.path.dirname(current_path)
    
    if use_gitignore:
        # Traverse up from current directory to base_dir
        while True:
            gitignore_path = os.path.join(current_dir, '.gitignore')
            if os.path.isfile(gitignore_path):
                patterns += load_ignore_patterns(gitignore_path)
            
            if current_dir == base_dir:
                break
            current_dir = os.path.dirname(current_dir)

    if use_dockerignore:
        # .dockerignore only in root-dir
        dockerignore_path = os.path.join(base_dir, '.dockerignore')
        if os.path.isfile(dockerignore_path):
            patterns += load_ignore_patterns(dockerignore_path)
    
    return patterns

def should_ignore(path, base_dir, user_ignores, use_gitignore, use_dockerignore):
    ignore_patterns = user_ignores.copy()
    
    if use_gitignore or use_dockerignore:
        ignore_patterns += load_gitignore_patterns_from_hierarchy(
            path, base_dir, use_gitignore, use_dockerignore
        )
    
    relative_path = os.path.relpath(path, base_dir)
    return is_ignored_by_patterns(relative_path, ignore_patterns)

def process_directory(base_dir, user_ignores, use_gitignore, use_dockerignore):
    output = []
    total_files = 0
    ignored_files = 0
    
    for root, dirs, files in os.walk(base_dir, topdown=True):
        for filename in files:
            file_path = os.path.join(root, filename)
            if should_ignore(file_path, base_dir, user_ignores, use_gitignore, use_dockerignore):
                ignored_files += 1
                continue
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                output.append(f"\n\n=== {os.path.relpath(file_path, base_dir)} ===\n{content}")
                total_files += 1
            except Exception as e:
                continue
        
        dirs[:] = [d for d in dirs if not should_ignore(
            os.path.join(root, d), 
            base_dir, 
            user_ignores, 
            use_gitignore,
            use_dockerignore
        )]
    
    return {
        'content': '\n'.join(output),
        'stats': {
            'total_files': total_files,
            'ignored_files': ignored_files,
            'total_size': len(''.join(output))
        }
    }

def run_onetxt(base_dir, user_ignores, use_gitignore=True, use_dockerignore=True):
    user_ignores = user_ignores.copy()
    user_ignores.append('response.txt')

    result = process_directory(base_dir, user_ignores, use_gitignore, use_dockerignore)
    output_file = os.path.join(base_dir, 'response.txt')
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(result['content'])
    
    print(f"Processed {result['stats']['total_files']} files "
          f"(ignored {result['stats']['ignored_files']})")
    return output_file