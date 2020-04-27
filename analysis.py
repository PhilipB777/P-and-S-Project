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

# Initialise the variable with an empty string.
irisVar = ""
# Use this while loop to allow the user to exit the program.
while irisVar != "E":
    # Use this nested while loop to allow the user to view multiple histograms.
    while irisVar not in ("Sepal length", "Sepal width", "Petal length", "Petal width", "E"):
        # The capitalise function allows the user to enter the variable in any case.
        irisVar = input("Enter the Iris Variable Name to view a histogram or press 'e' to Exit: ").capitalize()
    # Checks that the user hasn't entered e for exit.
    if irisVar != "E":
        # Use the pyplot module to create a histogram of the input iris variable.
        # Use red for a better visual display.
        plt.hist(irisData[irisVar], color = "red")
        # Add a title to the histogram.
        # The title is a concatenation with the input iris variable.
        plt.title("Iris " + irisVar)
        # Add an x label to the histogram.
        # The x label is a concatenation with the input iris variable.
        plt.xlabel(irisVar + " in cm")
        # Add a y label Irises to the histogram.
        plt.ylabel("Irises")
        # Save the figure of the histogram in the users folder.
        plt.savefig(irisVar + " Histogram.png")
        # Clear the figure of the histogram to allow the user to save a new
        # histogram of another variable.
        plt.clf()
        # Reset the variable to an empty string to allow the user to input
        # another variable.
        irisVar = ""