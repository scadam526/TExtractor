# App for searching text files for given regex pattern(s) and writing to CSV file.
# Each group in the regex pattern will correspond to an output column.
# GUI initially built in QT Designer.
# Shawn Adams - shawn.adams@titanmedicalinc.com - 07SEP2022


import sys
from sample import *

"""
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)

    window.

    def on_click():
        print('Yo!')

    window.show()
    sys.exit(app.exec())
"""


class myApp(Ui_MainWindow):
    def __init__(self, window):
        self.setupUi(window)
        self.pushButton.clicked.connect(self.whenClicked)
        self.buttonBox.accepted.connect(self.clickOK)
        self.buttonBox.rejected.connect(self.clickCancel)

    @staticmethod
    def whenClicked():
        print('Yo!')

    @staticmethod
    def clickOK():
        print('Yo mama!')

    @staticmethod
    def clickCancel():
        print('Not yo mama!')


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui = myApp(MainWindow)

MainWindow.show()
app.exec()
