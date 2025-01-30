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
        ".ruby-version", "storage", "public/uploads", ".rspec", 
        "config/credentials.yml.enc", "config/master.key",
        "docker-compose.override.yml"
    ],
    "Angular": [
        "node_modules", "dist", ".angular",
        "package-lock.json", "yarn.lock",
        "pnpm-lock.yaml", "bun.lockb",
        "e2e", "browser", "karma.conf.js",
        ".angular/cache", "*.ngsummary.json"
    ],
    "Django/Flask (Python)": [
        "__pycache__", "*.pyc", ".venv", "venv",
        "db.sqlite3", "migrations", ".coverage",
        "media", "staticfiles", ".pytest_cache"
    ],
    "Vue.js/Nuxt": [
        "node_modules", "dist", ".nuxt", ".output",
        ".vuepress", "*.log", ".env.local"
    ],
    "Laravel (PHP)": [
        "vendor", "node_modules", "storage/framework/cache",
        "storage/logs", ".env", "bootstrap/cache",
        "public/storage", "public/hot"
    ],
    "Go": [
        "bin", "pkg", ".exe", "debug", "vendor",
        "coverage.out", "*.test", ".vscode"
    ],
    "Android (Java/Kotlin)": [
        "build", ".gradle", "captures", ".idea",
        "local.properties", "*.apk", "*.aab",
        "*.iml", "app/release"
    ],
    "iOS (Swift)": [
        "Pods", "DerivedData", "*.xcworkspace",
        "Podfile.lock", "Cartfile.resolved",
        "fastlane/report.xml", "build"
    ]
}

DEFAULT_IGNORE_KEYWORDS = [
    ".github",".git","tmp", "cache", "bin", "build", "dist", "out", "logs", "README.md",
    "node_modules", "venv", ".venv", "__pycache__", ".idea", ".vscode", ".gitignore"
]

HIDDEN_IGNORE_KEYWORDS = [
    ".github", ".git", ".gitignore", ".idea", ".vscode", ".env",
    ".dockerignore", ".DS_Store", ".npmignore", ".yarn", ".ruby-version",
    ".eslintcache", ".tern-port", 
    ".sass-cache", ".nyc_output",
    ".cache-loader", ".babelcache",
    ".metro-cache", ".fusebox",
    ".history"
]

NON_HIDDEN_IGNORE_KEYWORDS = [
    "tmp", "cache", "bin", "build", "dist", "out", "logs", "README.md",
    "node_modules", "venv", ".venv", "__pycache__",
    "coverage", "reports", 
    "junit", "test-results",
    "docker-data", "dump.rdb",
    "*.log", "*.tmp", "*.bak",
    "*.swp", "*.swo"
]
