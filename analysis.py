# Philip Brady
# The Programming and Scripting Project 2020.
# This program displays an analysis of Fisher's
# Iris Data Set.

import pandas as pd
import matplotlib.pyplot as plt

irisdata = pd.read_csv('iris.csv')

# Use the describe function to obtain a summary of the Iris Data.
summary = irisdata.describe()
# Convert the summary to a string and round to one decimal place for a better visual.
text = str(summary.round(1))
# Create a new file and write the text summary to it.
with open ('Iris Data Summary.txt', 'w') as f:
    f.write(text)