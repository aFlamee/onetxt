from setuptools import setup, find_packages

setup(
    name="onetxt",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    entry_points={
        'gui_scripts': [
            'onetxt=onetxt.gui.main_window:run_ui'
        ],
    },
)