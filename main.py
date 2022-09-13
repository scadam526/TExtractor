# App for searching text files for given regex pattern(s) and writing to CSV file.
# Each group in the regex pattern will correspond to an output column.
# GUI initially built in QT Designer.
# Shawn Adams - shawn.adams@titanmedicalinc.com - 07SEP2022


import sys
import re
from sample import *

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)

    # *** default file path for debug purposes. remove in final build ***
    ui.inputFileText.setText(r"C:\project\handpiece_fw\v0.1.0-REL\bitbucket_repo\v0.1.0-REL\log\presence_debug.log")


    def setPattern():
        pattern = ui.pattern.toPlainText()
        try:
            p = re.compile(pattern)
        except re.error:
            print("Invalid regex pattern")
            return
        print(p.pattern)


    def loadInputFile():
        try:
            inFile = open(ui.inputFileText.text(), "r")
        except FileExistsError:
            print('Input file path does not exist')
            return
        text = inFile.read()
        inFile.close()
        ui.textDisplay.setText(text)
        return text


    def openOutFile():
        outFilePath: str = ui.outputFileText.text()
        outText = loadInputFile()
        if outFilePath != '':
            outFile = open(outFilePath, "w")
            outFile.write(outText)


    ui.setPatternButton.clicked.connect(setPattern)
    ui.loadInputFile.clicked.connect(loadInputFile)
    ui.processDataButton.clicked.connect(openOutFile)

    window.show()
    sys.exit(app.exec())
