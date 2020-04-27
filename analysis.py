# Philip Brady
# The Programming and Scripting Project 2020.
# This program displays an analysis of Fisher's
# Iris Data Set.

import pandas as pd
import matplotlib.pyplot as plt

irisData = pd.read_csv('iris.csv')

# Use the describe function to obtain a summary of the Iris Data.
#summary = irisData.describe()
# Convert the summary to a string and round to one decimal place for a better visual.
#text = str(summary.round(1))
# Create a new file and write the text summary to it.
#with open ('Iris Data Summary.txt', 'w') as f:
#    f.write(text)


irisVar = ""
while irisVar != "E":
    while irisVar not in ("Sepal length", "Sepal width", "Petal length", "Petal width", "E"):
        irisVar = input("Enter the Iris Variable Name to view a histogram or press 'e' to Exit: ").capitalize()
    if irisVar != "E":
        plt.hist(irisData[irisVar], color = "red")
        plt.title("Iris " + irisVar)
        plt.xlabel(irisVar + " in cm")
        plt.ylabel("Irises")
        plt.savefig(irisVar + " Histogram.png")
        plt.clf()
        irisVar = ""