import sys
import pandas as pd
import pyqtgraph as pg
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QFileDialog, QLabel, QComboBox, QSpinBox, QLineEdit

class CSVPlotter(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('CSV Plotter')
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.load_button = QPushButton('Open CSV')
        self.load_button.clicked.connect(self.open_csv)
        self.layout.addWidget(self.load_button)

        # Text field to display the full path of the opened CSV
        self.file_path_line_edit = QLineEdit()
        self.file_path_line_edit.setReadOnly(True)
        self.layout.addWidget(self.file_path_line_edit)

        self.x_axis_combo = QComboBox()
        self.y_axis_combo = QComboBox()
        self.layout.addWidget(QLabel('X-axis column:'))
        self.layout.addWidget(self.x_axis_combo)
        self.layout.addWidget(QLabel('Y-axis column:'))
        self.layout.addWidget(self.y_axis_combo)

        self.graph_type_combo = QComboBox()
        self.graph_type_combo.addItems(['Scatter', 'Line'])
        self.layout.addWidget(QLabel('Graph type:'))
        self.layout.addWidget(self.graph_type_combo)

        self.point_size_spinbox = QSpinBox()
        self.point_size_spinbox.setValue(5)
        self.layout.addWidget(QLabel('Scatter point size:'))
        self.layout.addWidget(self.point_size_spinbox)

        self.line_width_spinbox = QSpinBox()
        self.line_width_spinbox.setValue(2)
        self.layout.addWidget(QLabel('Line width:'))
        self.layout.addWidget(self.line_width_spinbox)

        self.plot_widget = pg.PlotWidget()
        self.layout.addWidget(self.plot_widget)

        # Connect signals to update plot
        self.x_axis_combo.currentIndexChanged.connect(self.plot_data)
        self.y_axis_combo.currentIndexChanged.connect(self.plot_data)
        self.graph_type_combo.currentIndexChanged.connect(self.plot_data)
        self.point_size_spinbox.valueChanged.connect(self.plot_data)
        self.line_width_spinbox.valueChanged.connect(self.plot_data)

    def open_csv(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open CSV File", "", "CSV Files (*.csv);;All Files (*)")
        if file_name:
            self.file_path_line_edit.setText(file_name)  # Set file path in the QLineEdit
            self.df = pd.read_csv(file_name)
            self.update_column_selections()
            self.plot_data()

    def update_column_selections(self):
        columns = self.df.columns
        self.x_axis_combo.clear()
        self.y_axis_combo.clear()
        self.x_axis_combo.addItems(columns)
        self.y_axis_combo.addItems(columns)

    def plot_data(self):
        x_col = self.x_axis_combo.currentText()
        y_col = self.y_axis_combo.currentText()
        graph_type = self.graph_type_combo.currentText()
        point_size = self.point_size_spinbox.value()
        line_width = self.line_width_spinbox.value()

        if x_col in self.df.columns and y_col in self.df.columns:
            x_data = self.df[x_col]
            y_data = self.df[y_col]
            self.plot_widget.clear()
            if graph_type == 'Scatter':
                self.plot_widget.plot(x_data, y_data, pen=None, symbol='o', symbolSize=point_size)
            elif graph_type == 'Line':
                self.plot_widget.plot(x_data, y_data, pen=pg.mkPen(width=line_width))

        # Set the labels for the X and Y axes
        self.plot_widget.setLabel('bottom', x_col)  # X-axis label
        self.plot_widget.setLabel('left', y_col)    # Y-axis label

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CSVPlotter()
    window.show()
    sys.exit(app.exec())
