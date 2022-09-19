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
"""

# Cap sense values regex pattern: ProcessCapacitivePads\(\).{10}(\d+\.\d+).+(\d+\.\d+).+(\d+\.\d+).+(\d+\.\d+)

import sys
import re
import os


# import Qt Designer generated UI code from TExtractor.py
from TExtractor import QtWidgets, Ui_MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    msg = QtWidgets.QMessageBox()

    # *** default file path for debug purposes. remove in final build ***
    ui.headerText.setText("Num, Neck, Thumb, Bulb2, Bulb 1")
    ui.patternText.setPlainText(r"ProcessCapacitivePads\(\).{10}(\d+\.\d+).+(\d+\.\d+).+(\d+\.\d+).+(\d+\.\d+)")
    ui.inputFileText.setText(os.getcwd() + r"\logs\1. right handpiece - long cable - clutch pulled "
                                        r"when hand present.log")
    ui.outputFileText.setText(os.getcwd() + r"\logs\output_test_log.csv")


    def previewLog():
        try:
            inFile = open(ui.inputFileText.text(), "r")
        except FileExistsError:
            print('ERROR: Input file path does not exist')
            msg.setText('ERROR: Input file path does not exist')
            msg.exec()
            return
        text = inFile.read()
        inFile.close()
        ui.textDisplay.setText(text)
        return


    def getData():

        # Open input file and load it to a string then close file. Load input pattern to string.
        try:
            inFile = open(ui.inputFileText.text(), "r")
        except FileExistsError:
            print('ERROR: Input file path does not exist')
            msg.setText('ERROR: Input file path does not exist')
            msg.exec()
            return
        text = inFile.read()
        inFile.close()
        pattern = ui.patternText.toPlainText()

        # Compile regex pattern to make sure it is valid.
        try:
            re.compile(pattern)
        except error:
            print("ERROR: Invalid regex pattern")
            msg.setText("ERROR: Invalid regex pattern")
            msg.exec()
            return

        # Set first line of output to header text. Then for each iteration found trim unwanted characters
        #    and append new line to the string. Return the final string with header.
        output = ui.headerText.text() + chr(13)
        i = 1
        for match in re.finditer(pattern, text):
            cleanList = str(list(match.groups())).replace("'", "")
            cleanList = cleanList.replace("[", "")
            cleanList = cleanList.replace("]", "")
            output += str(i) + ", " + cleanList + chr(13)
        i += 1
        inFile.close()
        return output


    def previewData():
        # Instantiate the vertical scrollbar, write output data to text window, scroll back to top.
        scrollbar = ui.textDisplay.verticalScrollBar()
        ui.textDisplay.setText(getData())
        scrollbar.setValue(scrollbar.minimum())


    def outputData():
        previewData()
        # If overwrite file is checked then output whether exists or not. Will only fail if file is locked.
        if ui.overwriteFile.isChecked():
            try:
                outFile = open(ui.outputFileText.text(), "w")
                outFile.write(getData())
            except PermissionError:
                print("ERROR: Cannot access output file.")
                msg.setText("ERROR: Cannot access output file.")
                msg.exec()
                return

        # If file already exists, do not overwrite existing file.
        else:
            try:
                outFile = open(ui.outputFileText.text(), "x")
                outFile.write(getData())
            except PermissionError:
                print("ERROR: Cannot access output file.")
                msg.setText("ERROR: Cannot access output file.")
                msg.exec()
                return
            except FileExistsError:
                print("ERROR: Output file already exists.")
                msg.setText("ERROR: Output file already exists.")
                msg.exec()
                return


    # Connect buttons to functions.
    ui.previewLog.clicked.connect(previewLog)
    ui.previewData.clicked.connect(previewData)
    ui.outputDataButton.clicked.connect(outputData)

    window.show()
    sys.exit(app.exec())
