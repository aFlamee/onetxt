PRESET_IGNORES = {
    "No Preset": [],
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
        "pnpm-lock.yaml", "bun.lockb", "assets", ".rubocop.yml",
        ".ruby-version"
    ],
    "Angular": [
        "node_modules", "dist", ".angular",
        "package-lock.json", "yarn.lock",
        "pnpm-lock.yaml", "bun.lockb"
    ]
}

DEFAULT_IGNORE_KEYWORDS = [
    ".github",".git","tmp", "cache", "bin", "build", "dist", "out", "logs", "README.md",
    "node_modules", "venv", ".venv", "__pycache__", ".idea", ".vscode", ".gitignore"
]

HIDDEN_IGNORE_KEYWORDS = [
    ".github", ".git", ".gitignore", ".idea", ".vscode", ".env",
    ".dockerignore", ".DS_Store", ".npmignore", ".yarn", ".ruby-version"
]

NON_HIDDEN_IGNORE_KEYWORDS = [
    "tmp", "cache", "bin", "build", "dist", "out", "logs", "README.md",
    "node_modules", "venv", ".venv", "__pycache__"
]
