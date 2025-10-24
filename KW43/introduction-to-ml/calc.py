##   ---------------------------------------------   #
####                    TASK                     #####
##   ---------------------------------------------   #
#
# import numpy as np
# 
# data = np.array([1, 2, 3, 4, 5, 6, 9.87654321])
# mean = np.mean(data)
# print(mean)

##   ---------------------------------------------   #
####                    TASK                     #####
##   ---------------------------------------------   #
#
# import statistics
# 
# data = [1, 2, 3, 4, 5, 6, 9.87654321]
# mean = statistics.mean(data)
# print(mean)

##   ---------------------------------------------   #
####                    TASK                     #####
##   ---------------------------------------------   #
#
# (1+2+3+4+5+6+9.87654321)/7

##   ---------------------------------------------   #
####                    TASK                     #####
##   ---------------------------------------------   #
#
# import pandas as pd
# 
# data = pd.Series([1, 2, 3, 4, 5, 6, 9.87654321])
# mean = data.mean()
# print(mean)

##   ---------------------------------------------   #
####                    TASK                     #####
##   ---------------------------------------------   #
#

# 2012-01-05,6,5.3,23,80

import numpy as np

DATA = "./wetter.csv"
# If file has a header row:
arr = np.genfromtxt(DATA, delimiter=',', skip_header=1)   # dtype=float by default
# arr is a 2D numpy.ndarray
# print(arr.shape)
# print(arr[:3])  # first 3 rows

# data = [1, 2, 3, 4, 5, 6, 9.87654321]
data = arr[:,2]
mean = np.mean(data)
print("data =", data)
print("mean =", mean)

# extract the 3rd column (0-based index 2)
# third_col = arr[:, 2]

# drop missing values and convert to Python list if you want
# third_col_clean = third_col[~np.isnan(third_col)]
# data = third_col_clean.tolist()
# 
# mean_value = np.mean(third_col_clean)   # or np.nanmean(third_col) to ignore NaNs
# print("data =", data)
# print("mean =", mean_value)