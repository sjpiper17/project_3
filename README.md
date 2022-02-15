# project_3
#This code is designed to use COVID-19 metadata to identify how the prevalence of different variants has changed over time throughout the
#pandemic. This code is part of an assignment to learn about map reduce procedures and gain experience with distributed computing.
#The current goal for the code is to output a count of how many times a variant was detected each quarter. Analyzing this data, connecting it
#to other trends, and making predictions are not goals of this assignment. In the future, this data may be used to identify factors in 
#disease spread and variant propogation, as well as predicting future trends. Ideally, this code can be uploaded to Github and used by
#any user not familiar with how it was made.

#This code contains definitions for two remote ray functions, one map and one reduce. The map function takes the data and returns a 
#dataframe with one column that contains a tuple of (quarter, variant) in each row. This dataframe is then used to get a count of how many 
#times each combination occurs in the reduce function. After both functions are defined, ray is initialized and the functions are run 
#using the data. This code depends on ray, numpy, and pandas. It was tested with a small test data set. The code was run using WSL in ubuntu in 
#a virtual environment. 

#This code was made by Scott Piper (sjpiper@stanford.edu) as part of the Software Engineering for Scientists course at Stanford University in
#Winter Quarter of 2022.

#The file tests.py contains a unit test to ensure that the count of total variants across all quarters from the map reduce matches the number of entries in the original file.
