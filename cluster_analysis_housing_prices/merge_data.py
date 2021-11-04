# Import, merge, and clean data. 
# Returns two data frames: one with growth time series, and the other with growth indices

# Import packages
import numpy as np
import pandas as pd
import glob

path = r'data' # use path where input data files are stored
all_files = glob.glob(path + "/*.csv")

#### PSEUDOCODE ####
# Load the csv
# Set the 0th column (with dates) as the index for the pandas df
# Iteratively merge on the index.
# pd.merge((pd.read_csv(f) for f in all_files), axis=1) 

# Create a list with House Price Indices for each state. Each item in the list 
# contains the series for another state. Starting date of 1990 chosen in part to 
# limit NaNs, but also b/c conceptually this seems to be sufficiently before when Austin
# started to really see growth in house prices (beginning in the early 00s).

# Note that the index is set to 1995, ie, for 1995 the index = 100.
combined_list = []
i = 0
for f in all_files:
    fth_df = pd.read_csv(f)    
    fth_df['DATE'] = pd.to_datetime(fth_df['DATE'])
    fth_df.set_index('DATE', inplace=True)
    fth_df = fth_df.loc['1990-01-01':]
    combined_list.append(fth_df)

# Combine the list of time series into a single df for further cleaning
combined_df = pd.DataFrame()
for df in combined_list:
    combined_df = pd.concat([combined_df, df], axis = 1)
    
combined_df = combined_df.astype(float)

# Drop NaNs, and transpose the df so it can be easily used in the
# cluster algorithm in the upcoming analysis.
data_index = combined_df.dropna().transpose()
data_growth = combined_df.pct_change().dropna().transpose()

# Export
data_index.to_csv('data/merged_data/ts_index_all_cities.csv')
data_growth.to_csv('data/merged_data/ts_growth_all_cities.csv')