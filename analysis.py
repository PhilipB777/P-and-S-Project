# Philip Brady
# The Programming and Scripting Project 2020.
# This program displays an analysis of Fisher's
# Iris Data Set.

import pandas as pd
import matplotlib.pyplot as plt

irisdata = pd.read_csv('iris.csv')
plt.hist(irisdata['sepal_length'])
plt.title("Iris Sepal Length")
plt.xlabel("Sepal Length in cm")
plt.ylabel("Irises")
plt.savefig("Sepal Length Histogram.png")
plt.show()