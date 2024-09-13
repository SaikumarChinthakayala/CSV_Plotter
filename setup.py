from setuptools import setup, find_packages

setup(
    name='csv_plotter',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'pyqtgraph',
        'PyQt6',
    ],
    entry_points={
        'console_scripts': [
            'csv_plotter=csv_plotter.main:main',
        ],
    },
    python_requires='>=3.6',
    description='A Python applet for plotting CSV data with PyQt6 and pyqtgraph.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)

