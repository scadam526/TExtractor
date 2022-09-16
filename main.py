"""
    App for searching text files for given regex pattern(s) and writing to CSV file.
    Each group in the regex pattern will correspond to an output column.
    GUI initially built in QT Designer.
    Shawn Adams - shawn.adams@titanmedicalinc.com - 07SEP2022

    PyCharm External Tool settings for Qt Designer .ui to .py converter pyuic6.
        Program: .../envs/TExtractor/Scripts/pyuic6.exe
        Arguments: $FileName$ -o $FileNameWithoutExtension$.py
        Working dir: $FileDir$
        Synchronize files after execution: True
        Open console: False

    App converted to .exe via auto-py-to-exe.

    Cap sense values regex pattern: ProcessCapacitivePads\(\).{10}(\d+\.\d+).+(\d+\.\d+).+(\d+\.\d+).+(\d+\.\d+)

"""

import sys
import re
import os
from TExtractor import *


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)

    # *** default file path for debug purposes. remove in final build ***
    ui.headerText.setText("Num, Neck, Thumb, Bulb2, Bulb 1")
    ui.patternText.setPlainText(r"ProcessCapacitivePads\(\).{10}(\d+\.\d+).+(\d+\.\d+).+(\d+\.\d+).+(\d+\.\d+)")
    ui.inputFileText.setText(os.getcwd() + r"/logs/1. right handpiece - long cable - clutch pulled "
                             r"when hand present.log")
    ui.outputFileText.setText(os.getcwd() + r"/logs/output_test_log.txt")


    def previewLog():
        try:
            inFile = open(ui.inputFileText.text(), "r")
        except FileExistsError:
            print('Input file path does not exist')
            return
        text = inFile.read()
        inFile.close()
        ui.textDisplay.setText(text)
        return


    def previewData():
        try:
            inFile = open(ui.inputFileText.text(), "r")
        except FileExistsError:
            print('Input file path does not exist')
            return
        text = inFile.read()
        inFile.close()
        pattern = ui.patternText.toPlainText()
        ui.textDisplay.setText(ui.headerText.text())
        try:
            p = re.compile(pattern)
        except re.error:
            print("Invalid regex pattern")
            return

        i = 0
        for match in re.finditer(pattern, text):
            cleanList = str(list(match.groups())).replace("'","")
            cleanList = cleanList.replace("[","")
            cleanList = cleanList.replace("]","")
            ui.textDisplay.append(str(i) +", " + cleanList)
            i += 1

    def outputData():
        outFilePath: str = ui.outputFileText.text()
        outText = loadInputFile()
        if outFilePath != '':
            outFile = open(outFilePath, "w")
            outFile.write(outText)


    def procData(p, t):
        numGroups = p.count('(') - p.count(r'\(')
        pattern = ui.pattern.toPlainText()
        try:
            p = re.compile(pattern)
        except re.error:
            print("Invalid regex pattern")
            return
        print(p.pattern)


    ui.previewLog.clicked.connect(previewLog)
    ui.previewData.clicked.connect(previewData)
    ui.outputDataButton.clicked.connect(outputData)

    window.show()
    sys.exit(app.exec())
