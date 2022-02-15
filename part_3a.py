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

#import what we need
from pyrsistent import pdeque
import ray
import numpy as np
import pandas as pd

#read in the data file
data = pd.read_csv("test_data.txt", sep='\t')

#define the map function to take the data and create a df of one column with a tuple containing (quarter, variant) for each row
@ray.remote
def map(data):
    #isolate the date column
    date = data['Collection date']
    #convert the year-month-day date to quarter
    quarter = pd.PeriodIndex(date, freq = 'Q')
    #convert to a dataframe
    quarter = pd.DataFrame(quarter)
    #isolate the variant column
    variant = data['Variant']
    #turn into a dataframe
    #join the quarter and variant to one dataframe
    variant = pd.DataFrame(variant)
    frames = [quarter, variant]
    result = pd.concat(frames, axis = 1)
    #add a third column with a tuple of the first two in each row
    result['tuples'] = result[['Collection date', 'Variant']].apply(tuple, axis = 1)
    #isolate the tuple column
    map_result = result.tuples
    return map_result

#define the reduce function to count how many times each quarter and variant combination occurs
@ray.remote
def reduce(map_result):
    count = map_result.value_counts()
    return count

#initialize ray, and run the map function using the data. Then run the reduce function and print the output.
ray.init()
map_result = map.remote(data)
count = reduce.remote(map_result)
print(ray.get(count))