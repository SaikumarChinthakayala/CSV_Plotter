# CSV Plotter

A Python applet for plotting CSV data with PyQt6 and pyqtgraph. This tool allows you to select columns for the X and Y axes, choose between scatter and line graph types, and adjust point sizes and line widths.

## Features
- Open and visualize CSV data
- Select X and Y axes from the file
- Switch between scatter and line graphs
- Adjust point size for scatter plots and line width for line graphs

## Requirements
Before installing, ensure you have the following:
- Python 3.6+ installed
- `pip` (Python's package installer)

## Installation

### 1. Clone the Repository
First, download the project by cloning the repository from GitHub or manually downloading it.

```bash
git clone https://github.com/SaikumarChinthakayala/CSV_Plotter.git
cd csv-plotter
python3 -m venv venv
source venv/bin/activate   # On Windows, use venv\Scripts\activate
pip install -r requirements.txt
python3 main.py
```

### 2. Optional stuff
Create a file called run_csv_plotter.sh

```bash
#!/bin/bash
cd /path/to/your/csv-plotter
source venv/bin/activate
python3 main.py
```

```bash
chmod +x run_csv_plotter.sh
```

Run the .sh file :

```bash
./run_csv_plotter.sh
```

Or a desktop shortcut can be created to this .sh file
### 3. Mac Application
If the user is on Mac OSX, an automator script to run the python script can be setup. 
It is not as straight forward copy pasting the same terminal command. The automator script also needs the python binary installation
location which can be obtained using:
```bash
where python
```

In the automator app, 
```bash
$(which python) main.py 
```

one could have this command and this creates an application file which can be placed on the dock with a fancy icon of your choice



Example looks like :
![alt text](https://github.com/SaikumarChinthakayala/CSV_Plotter/blob/master/examples/ex1.png)
