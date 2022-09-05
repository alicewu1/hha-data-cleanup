from this import d
import pandas as pd
import datetime as dt
import uuid # universal unique identifier 
import numpy as np

# load in initial data file
df = pd.read_csv('data\School_Learning_Modalities.csv') # use relative path
df ##view output

df.shape # count dimensions: rows by columns 
df ## view output: 741876 rows x 9 columns 


### READING COLUMN AND ROW NAMES ###
df.head() # reads first 5 column names
column_names = df.columns # define variable 
column_names # view column names 
row_names = df.index # define variable  
row_names #reads row names 


### CLEANING COLUMNS ###
df.columns = df.columns.str.replace('[^A-Za-z0-9]+', '_') ## regex formatting for strings
list(df)
# replace all whitespace in column names with an underscore
df.columns = df.columns.str.replace(' ', '_')
df.columns # view output


### COLUMN TYPES ###
df.dtypes #view column types to see if strings are really strings, number are numbers, dates are dates, and boolean are booleans

# create a list of columns that are strings, and save as strings 
strings = df.select_dtypes(include=['object']).columns
# create a list of columns that are numbers, and save as numbers
numbers = df.select_dtypes(include=['int64','float64']).columns
# create a list of columns that are dates, and save as dates
dates = df.select_dtypes(include=['datetime64[ns]']).columns
# create a list of columns that are booleans, and save as booleans
booleans = df.select_dtypes(include=['bool']).columns
# create a list of columns that are objects, and save as objects
objects = df.select_dtypes(include=['object']).columns


### DUPLICATE ROWS ### 
df.columns.duplicated() # look of duplicate rows 


### REMOVING WHITESPACE ###
# .sum tp get a count of missing values in each column
df.isnull().sum() ## Identified Student_Count Column with missing 604 values

# replacing blank, empty cells with NaN 
#NaN tells python that it is a missing value instead of white space that we can't see
df.replace(to_replace='', value=np.nan, inplace=True)

# drop rows with missing values
df.dropna(inplace=True) # drop rows with missing values
df.isnull().sum() #run again to double verify whitespace was removed


### CONVERTING COLUMNS ###
# Convert Week column from object to datetime
df['Week'] = pd.to_datetime(df['Week'])

#removed empty cells with NaaN before converting Student_Count column
df['Student_Count'] = df['Student_Count'].astype(int)#convert Student_Count column from float64 to int
df.dtypes # re-check datatypes



### NEW DATA ###
#create new column named modality_inperson with Binary Variable from existing column Learning_Modality
df['modality_inperson'] = (df['Learning_Modality'].apply(
    lambda x: 'True' if x == 'in-person' else False)) 

df.to_csv('data\School_Learning_Modalities_2.csv') # creates and exports df into new csv file