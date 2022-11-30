# hha-data-cleanup
HHA507 / Data Science / Assignment 2 / Data Cleanup


## This repo aims to:
- practice formatting and cleaning a public dataset
- **Public dataset from healthdata.gov:** [School Learning Modalities](https://healthdata.gov/National/School-Learning-Modalities/aitj-yx37)

## This repo Contains:
- **readme.md**: provides the instructions for what I am doing
- **data** folder: contains original .csv file and cleaned .csv file
- **scripts** folder: contains my .py file
- **requirements.txt** file containing necessary libraries

## Created a .py script file that performs the following on the dataset:
1. Loads the data into python
- https://github.com/alicewu1/hha-data-cleanup/blob/5e464d1fe031860555091e3a2a13c0802d13013e/scripts/datacleaning.py#L7-L9

2. Prints the count of columns and rows
- https://github.com/alicewu1/hha-data-cleanup/blob/5e464d1fe031860555091e3a2a13c0802d13013e/scripts/datacleaning.py#L11-L12

3. Provides a print out of the column names
- https://github.com/alicewu1/hha-data-cleanup/blob/5e464d1fe031860555091e3a2a13c0802d13013e/scripts/datacleaning.py#L15-L20

4. Cleans the column names, Strings that might exist within each column, Assess white space or special characters
- https://github.com/alicewu1/hha-data-cleanup/blob/5e464d1fe031860555091e3a2a13c0802d13013e/scripts/datacleaning.py#L23-L28

5. Converts the column types to the correct types
- https://github.com/alicewu1/hha-data-cleanup/blob/5e464d1fe031860555091e3a2a13c0802d13013e/scripts/datacleaning.py#L31-L43
- https://github.com/alicewu1/hha-data-cleanup/blob/5e464d1fe031860555091e3a2a13c0802d13013e/scripts/datacleaning.py#L63-L69

6. Look for duplicate rows and remove duplicate rows
- https://github.com/alicewu1/hha-data-cleanup/blob/5e464d1fe031860555091e3a2a13c0802d13013e/scripts/datacleaning.py#L46-L47

7. Assess missingness and whitespace
- https://github.com/alicewu1/hha-data-cleanup/blob/5e464d1fe031860555091e3a2a13c0802d13013e/scripts/datacleaning.py#L50-L60

8. Creating new data (create new column using binary variable from existing column)
- https://github.com/alicewu1/hha-data-cleanup/blob/5e464d1fe031860555091e3a2a13c0802d13013e/scripts/datacleaning.py#L73-L76

9. Exported dataframe into new .csv file called School_Learning_Modalities_2
- https://github.com/alicewu1/hha-data-cleanup/blob/5e464d1fe031860555091e3a2a13c0802d13013e/scripts/datacleaning.py#L78 


## Packages Used:
- https://github.com/alicewu1/hha-data-cleanup/blob/5e464d1fe031860555091e3a2a13c0802d13013e/scripts/datacleaning.py#L1-L5

