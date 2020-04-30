# Programming and Scripting Project 2020

This repository contains the project (Project 2020) for the Programming and Scripting module.  The Programming and Scripting module is part of the Higher Diploma in Data Analytics which is taught from Galway-Mayo Institute of Technology.

I was given the task of carrying out a detailed investigation of the well-known Fisher’s Iris data set.  I used code in Python to aid my analysis of the data set.

The repository holds various elements of my investigation.
-	The data set **[iris.csv](/iris.csv)** which I downloaded from https://archive.ics.uci.edu/ml/machine-learning-databases/iris/.
-	The program **[analysis.py](/analysis.py)** which I developed during my investigation.  It generates the various outputs which aided my investigation.
-	The file **[Iris Data Summary.txt](/Iris%20Data%20Summary.txt)** which holds a summary of each variable.
-	The files **[Sepal length Histogram.png](/Sepal%20length%20Histogram.png)**, **[Sepal width Histogram.png](/Sepal%20width%20Histogram.png)**, **[Petal length Histogram.png](/Petal%20length%20Histogram.png)** and **[Petal width Histogram.png](/Petal%20width%20Histogram.png)** which show a histogram of each variable.
-	The file **[Scatter Plots.png](/Scatter%20Plots.png)** which shows a scatter plot of each pair of variables.


## Introduction
Ronald Fisher was a British statistician and biologist who generated the Iris data set in 1936.  He introduced it as an example of linear discriminant analysis.  He analysed three species of the Iris flower by measuring four of their structural features. The three species chosen were 50 Iris setosa, 50 Iris virginica and 50 Iris versicolor.  The sepal length and width along with the petal length and width were measured in centimetres.  He was able to use combinations of these features to distinguish between the species based on his linear discriminant model.


## Investigation using Python
I began my program **[analysis.py](/analysis.py)** by importing the various libraries which I required.

    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns

Pandas is an open source data analysis tool which is built on Python.<br>
Matplotlib's pyplot module is an interface to matplotlib which helps to develop plots.<br>
Seaborn is a library based on matplotlib.  It is an interface which helps to develop statistical graphics.

I then used the pandas library to read in the data from the iris.csv file.

    irisData = pd.read_csv('iris.csv')
 
 
#### Investigation Part One Programming
I output a summary of each variable to a single text file.

I achieved this by:<br>

a) Using the describe function to obtain a summary of the Iris Data.

    summary = irisData.describe()
    
b) Converting the summary to a string and rounding to one decimal place for a better visual.

    text = str(summary.round(1))

c) Creating a new file called 'Iris Data Summary' and writing the text summary to it.

    with open ('Iris Data Summary.txt', 'w') as f:
        f.write(text)


#### Investigation Part One Analysis
           Sepal length  Sepal width  Petal length  Petal width
    count         150.0        150.0         150.0        150.0
    mean            5.8          3.1           3.8          1.2
    std             0.8          0.4           1.8          0.8
    min             4.3          2.0           1.0          0.1
    25%             5.1          2.8           1.6          0.3
    50%             5.8          3.0           4.4          1.3
    75%             6.4          3.3           5.1          1.8
    max             7.9          4.4           6.9          2.5

It immediately stands out that there is a big variation in the measurements of the four variables.  The petal length has a min value of 1 cm and a max value of 6.9 cm.  This is a big range of values, but I can see that 25% of the flowers are under 1.6 cm.  I would expect that this 25% is one of the species.  There is also a difference between the mean value of 3.8 cm and the 50% value of 4.4 cm whereas in the other three variables these values are similar.  I would expect that this will make it easier to identify a single species as having a longer petal.


#### Investigation Part Two Programming
I saved a histogram of each variable to png files.  I then decided to have the user interact with my finished program by taking the input of a variable.  The input is not case sensitive as I used the capitalise function to format the input to the correct case for the program to run without error.  The program also deals with incorrect data entry and allows the user to exit when the required histograms are saved.  A histogram of each input variable would be saved to the user’s folder.

I achieved this by:<br>

a) Initialising the variable with an empty string.

    irisVar = ""
    
b) Using a while loop to allow the user to exit the program.

    while irisVar != "E":
    
c) Using a nested while loop to allow the user to view multiple histograms.

    while irisVar not in ("Sepal length", "Sepal width", "Petal length", "Petal width", "E"):
    
d) Using the capitalise function to format the input in the required case.

    irisVar = input("Please enter one of the following variables for the histogram required."
                    "\n -Sepal length \n -Sepal width \n -Petal length \n -Petal width \nEnter here:"
                    "(Press 'e' to exit.) \n -").capitalize()
        
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


#### Investigation Part Two Analysis
![Sepal Length Histogram](/Sepal%20length%20Histogram.png "Sepal Length Histogram")

The standout features of the sepal length histogram are the three highest bars.  They represent different lengths, greater than 20 samples and are significantly taller than the other bars, so I would expect that each of the three bars matches each of the three species of flowers.

![Sepal Width Histogram](/Sepal%20width%20Histogram.png "Sepal Width Histogram")

The sepal width histogram shows that about 110 samples are between 2.5 and 3.5 cm in length.  This large number of samples in the range makes it difficult to differentiate the species with this variable.  There is one larger bar of over 35 samples at around 3.2 cm which may relate to a single species.

![Petal Length Histogram](/Petal%20length%20Histogram.png "Petal Length Histogram")

The petal length histogram is very significant because there are no samples between 2.2 and 2.8 cm in length.  This separates the 50 samples which are between 1 and 2.2 cm in length.  These 50 samples should all be of the one species.  The other bars between 2.8 and 7 cm in length suggest that it will be difficult to differentiate between the other two species based on this variable.

![Petal Width Histogram](/Petal%20width%20Histogram.png "Petal Width Histogram")

The petal width histogram is also very significant because it shows a cluster of 50 samples between 0.2 and 0.7 cm in length.  I would expect that these 50 samples are of the same species and are the same as the 50 sample cluster in the petal length histogram.  There is one other noticeable feature, the high bar of approximately 32 samples between 1.3 and 1.5 cm in length.  They could be from the one species which may allow the other two species to be differentiated by this variable.


#### Investigation Part Three Programming
I output a scatter plot of each pair of variables.  I used the seaborn library to produce these scatter plots on a single figure.  I also saved the figure to a png file.

I achieved this by:<br>

a) Using the seaborn library to create a scatter plot of each pair of variables.  The hue appropriately matches each of the three species a unique colour, while the height of two offers an optimal visual display.

    sns.pairplot(irisData, hue = "Species", height = 2)

b) Saving the figure of the scatter plots in the user’s folder.

    plt.savefig("Scatter Plots.png")

c) Displaying the figure of the scatter plots to the user.

    plt.show()


#### Investigation Part Three Analysis
![Scatter Plots](/Scatter%20Plots.png "Scatter Plots")

I picked four of the scatter plots for this part of my analysis. 
1. Sepal length vs Petal length<br>
The Iris-setosa can clearly be identified in its own cluster.  The short petal length is the standout feature of the setosa.  There is some overlap between the Iris-versicolor and Iris-virginica, but they are mostly differentiated on this plot.

2. Sepal length vs Sepal width<br>
The Iris-setosa can again be clearly identified in its own cluster.  There is however one outlier with a much shorter width than the other setosa samples.  The short sepal length makes it easy to distinguish the setosa.  The Iris-versicolor and Iris-virginica cannot be differentiated on this plot.

3. Petal length vs Petal width<br>
The Iris-setosa is distinguished again in this plot but the samples are in a much smaller cluster.  There is a clear differentiation between the setosa and the other two species.  The small cluster shows that a short petal length and width are standout features of the setosa.  This plot also seems to show that the Iris-versicolor and Iris-virginica can be identified using this combination of features.  The virginica has the longest and widest petals of the three species.

4. Petal width vs Sepal width<br>
The short petal width makes the Iris-setosa distinguishable from the other two species.  The outlier is again identifiable in this plot because of the shorter width than the other setosa samples.  At first look the Iris-versicolor and Iris-virginica can be distinguished clearly because the virginica has the widest petal of the three species.  There are however three samples that overlap directly with the versicolor.


## Conclusion
In using scatter plots to show the relationship between each pair of variables, it was possible to draw more accurate conclusions about the data set.  The scatter plots enabled me to prove or disprove some of the analysis which I had previously carried out using the summary method and histograms.  Overall, as Ronald Fisher set out to do, I was able to use Python to generate combinations of the Iris flower’s structural features to distinguish between the species based on his linear discriminant model.


## References
[1] “A Whirlwind Tour of Python by Jake VanderPlas (O’Reilly). Copyright 2016 O’Reilly Media, Inc., 978-1-491-96465-1.”

[2] The Python Standard Library. https://docs.python.org/3/library/

[3] Real Python Tutorials. https://realpython.com/

[4] Reading in a csv file. https://pandas.pydata.org/docs/user_guide/io.html#csv-text-files

[5] Creating histograms. https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.hist.html#matplotlib.pyplot.hist

[6] Creating scatter plots. https://seaborn.pydata.org/generated/seaborn.pairplot.html

[7] Data set research. https://en.wikipedia.org/wiki/Iris_flower_data_set

[8] Data set research and download. https://archive.ics.uci.edu/ml/datasets/iris

[9] Data set research. https://www.kaggle.com/arshid/iris-flower-dataset

[10] Data set research. https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html

[11] Data set research. https://github.com/RitRa/Project2018-iris

[12] Data set research. https://pythonhosted.org/bob/temp/bob.db.iris/doc/example.html

[13] Writing string to a text file. https://pythonexamples.org/python-write-string-to-text-file/

[14] Rounding off all columns. https://www.geeksforgeeks.org/python-pandas-dataframe-round/

[15] Wrapping strings in python. https://stackoverflow.com/questions/3346230/wrap-long-lines-in-python

[16] Markdown syntax. https://www.markdownguide.org/basic-syntax/

[17] Markdown editor. https://dillinger.io/

[18] Dealing with file name spaces in markdown. https://stackoverflow.com/questions/34569256/link-to-filenames-with-spaces-in-bitbucket-markdown
