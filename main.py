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

# import sys
# import re
# import os
from sys import exit
from os import getcwd
from re import compile
from re import finditer
from re import error

# import pandas as pd
from TExtractor import *

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)

    # *** default file path for debug purposes. remove in final build ***
    ui.headerText.setText("Num, Neck, Thumb, Bulb2, Bulb 1")
    ui.patternText.setPlainText(r"ProcessCapacitivePads\(\).{10}(\d+\.\d+).+(\d+\.\d+).+(\d+\.\d+).+(\d+\.\d+)")
    ui.inputFileText.setText(getcwd() + r"\logs\1. right handpiece - long cable - clutch pulled "
                                        r"when hand present.log")
    ui.outputFileText.setText(getcwd() + r"\logs\output_test_log.csv")


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


    def getData():

        # Open input file and load it to a string then close file. Load input pattern to string.
        try:
            inFile = open(ui.inputFileText.text(), "r")
        except FileExistsError:
            print('Input file path does not exist')
            return
        text = inFile.read()
        inFile.close()
        pattern = ui.patternText.toPlainText()

        # Compile regex pattern to make sure it is valid.
        try:
            compile(pattern)
        except error:
            print("Invalid regex pattern")
            return

        # Set first line of output to header. Then for each iteration found trim unwanted characters
        #    and append new line to the string. Return the final string with header.
        output = ui.headerText.text() + chr(13)
        i = 0
        for match in finditer(pattern, text):
            cleanList = str(list(match.groups())).replace("'", "")
            cleanList = cleanList.replace("[", "")
            cleanList = cleanList.replace("]", "")
            output += str(i) + ", " + cleanList + chr(13)
            i += 1
        return output


    def previewData():
        # Instantiate the vertical scrollbar, write output data to text window, scroll back to top.
        scrollbar = ui.textDisplay.verticalScrollBar()
        ui.textDisplay.setText(getData())
        scrollbar.setValue(scrollbar.minimum())


    def outputData():
        previewData()
        outFile = open(ui.outputFileText.text(), "w")
        outFile.write(getData())


    ui.previewLog.clicked.connect(previewLog)
    ui.previewData.clicked.connect(previewData)
    ui.outputDataButton.clicked.connect(outputData)

    window.show()
    exit(app.exec())
