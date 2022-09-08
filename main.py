# App for searching text files for given regex pattern(s) and writing to CSV file.
# Each group in the regex pattern will correspond to an output column.
# GUI initially built in QT Designer.
# Shawn Adams - shawn.adams@titanmedicalinc.com - 07SEP2022


import sys
from sample import Ui_MainWindow
from PyQt6 import QtCore, QtGui, QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec())
