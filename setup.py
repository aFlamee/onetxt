from setuptools import setup, find_packages

setup(
    name="onetxt",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    entry_points={
        'console_scripts': [  
            'onetxt=onetxt.gui.main_window:run_ui'
        ],
    },
    python_requires='>=3.8',
    include_package_data=True,
)