# Programming and Scripting Project 2020

This repository contains the project (Project 2020) for the Programming and Scripting module.  The Programming and Scripting module is part of the Higher Diploma in Data Analytics which is taught from Galway-Mayo Institute of Technology.

I was given the task of carrying out a detailed investigation of the well-known Fisher’s Iris data set.  I used code in Python to aid my analysis of the data set.

The repository holds various elements of my investigation.
-	The data set ‘iris.csv’ which I downloaded from https://archive.ics.uci.edu/ml/machine-learning-databases/iris/.
-	The program ‘analysis.py’ which I developed during my investigation.  It generates the various outputs which aided my investigation.
-	The file ‘Iris Data Summary.txt’ which holds a summary of each variable.
-	The files ‘Sepal length Histogram.png’, ‘Sepal width Histogram.png’, ‘Petal length Histogram.png’ and ‘Petal width Histogram.png’ which show a histogram of each variable.
-	The file ‘Scatter Plots.png’ which shows a scatter plot of each pair of variables.

### Introduction
Ronald Fisher was a British statistician and biologist who generated the Iris data set in 1936.  He introduced it as an example of linear discriminant analysis.  He analysed three species of the Iris flower by measuring four of their structural features. The three species chosen were 50 Iris setosa, 50 Iris virginica and 50 Iris versicolor.  The sepal length and width along with the petal length and width were measured in centimetres.  He was able to use combinations of these features to distinguish between the species based on his linear discriminant model.

### Investigation using Python
I began my program ‘analysis.py’ by importing the various libraries which I required.

    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns

Pandas is an open source data analysis tool which is built on Python.
Matplotlib.pyplot is an interface to matplotlib which helps to develop plots.
Seaborn is a library based on matplotlib.  It is an interface which helps to develop statistical graphics.

I then used the pandas library to read in the data from the iris.csv file.

    irisData = pd.read_csv('iris.csv')
    
##### Investigation Part One Programming
I output a summary of each variable to a single text file.

           Sepal length  Sepal width  Petal length  Petal width
    count         150.0        150.0         150.0        150.0
    mean            5.8          3.1           3.8          1.2
    std             0.8          0.4           1.8          0.8
    min             4.3          2.0           1.0          0.1
    25%             5.1          2.8           1.6          0.3
    50%             5.8          3.0           4.4          1.3
    75%             6.4          3.3           5.1          1.8
    max             7.9          4.4           6.9          2.5

I achieved this by:<br>
a) using the describe function to obtain a summary of the Iris Data.

    summary = irisData.describe()
    
b) Converting the summary to a string and rounding to one decimal place for a better visual.

    text = str(summary.round(1))

c) Creating a new file called ‘Iris Data Summary.txt’ and writing the text summary to it.

    with open ('Iris Data Summary.txt', 'w') as f:
        f.write(text)

##### Investigation Part One Analysis
It immediately stands out that there is a big variation in the measurements of the four variables.  The petal length has a min value of 1 cm and a max value of 6.9 cm.  This is a big range of values, but I can see that 25% of the flowers are under 1.6 cm.  I would expect that this 25% is one of the species.  There is also a difference between the mean value of 3.8 cm and the 50% value of 4.4 cm whereas in the other three variables these values are similar.  I would expect that this will make it easier to identify a single species as having a longer petal.


##### Investigation Part Two Programming
I saved a histogram of each variable to png files.  I then decided to have the user interact with my finished program by taking the input of a variable.  The input is not case sensitive as I used the capitalise function to format the input to the correct case for the program to run without error.  The program also takes deals with incorrect data entry and allows the user to exit when the required histograms are saved.  A histogram of each input variable would be saved to the user’s folder.

I achieved this by:<br>
a) Initialising the variable with an empty string.

    irisVar = ""
    
b) Using a while loop to allow the user to exit the program.

    while irisVar != "E":
    
c) Using a nested while loop to allow the user to view multiple histograms.

    while irisVar not in ("Sepal length", "Sepal width", "Petal length", "Petal width", "E"):
    
d) Using the capitalise function to format the input in the required case.

    irisVar = input("Enter the Iris Variable Name to view a histogram or press 'e' to Exit: ").capitalize()
        
e) Checking that the user hasn't entered e for exit.

    if irisVar != "E":
    
f) Using the pyplot module to create a histogram of the input iris variable.  The use of ten bins and the colour red enabled an optimal visual display.

    plt.hist(irisData[irisVar], bins = 10, color = "red")
        
g) Adding a title to the histogram.  The title is a concatenation with the input iris variable.

    plt.title("Iris " + irisVar)
        
h) Adding an x label to the histogram.  The x label is a concatenation with the input iris variable.
        
    plt.xlabel(irisVar + " in cm")
    
i) Adding a y label ‘Irises’ to the histogram.

    plt.ylabel("Irises")
        
j) Saving the figure of the histogram in the user’s folder.

    plt.savefig(irisVar + " Histogram.png")
        
k) Clearing the figure of the histogram to allow the user to save a new histogram of another variable.

    plt.clf()
    
l) Resetting the variable to an empty string to allow the user to input another variable.

    irisVar = ""

##### Investigation Part Two Analysis
![Sepal Length Histogram](/Sepal%20length%20Histogram.png "Sepal Length Histogram")

The standout features of the sepal length histogram are the three highest bars.  They represent different lengths, greater than 20 samples and are significantly taller than the other bars, so I would expect that each of the three bars matches each of the three species of flowers.
