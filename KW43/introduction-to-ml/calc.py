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

# extract the 3rd column (0-based index 2)
# third_col = arr[:, 2]

# drop missing values and convert to Python list if you want
# third_col_clean = third_col[~np.isnan(third_col)]
# data = third_col_clean.tolist()
# 
# mean_value = np.mean(third_col_clean)   # or np.nanmean(third_col) to ignore NaNs
# print("data =", data)
# print("mean =", mean_value)

##   ---------------------------------------------   #
####                    TASK                     #####
##   ---------------------------------------------   #
#
import numpy as np
from datetime import datetime

DATA = "./wetter.csv"

# Datei einlesen, Datumsspalte als String behalten
arr = np.genfromtxt(DATA, delimiter=',', skip_header=1, dtype=None, encoding='utf-8')

# Beispiel: Spaltenreihenfolge (Datum,Bewoelkung,Temperatur,Windgeschwindigkeit,Wettercode)
dates = np.array([datetime.strptime(row[0], "%Y-%m-%d") for row in arr])
temps = np.array([row[2] for row in arr], dtype=float)

# create months once
months = np.array([d.month for d in dates])

# define mask specs (you can add more tuples/lists)
mask_specs = [[5, 6, 7], [5], [7]]

# build list of boolean masks (each mask is 1D, length == len(dates))
masks = [np.isin(months, vals) for vals in mask_specs]

# filtered temperatures per mask: list of 1D numpy arrays
temps_filtered = [temps[m] for m in masks]

# convert to object array if you prefer numpy-indexable container
temps_filtered_arr = np.array(temps_filtered, dtype=object)

# per-mask means (use nanmean to ignore NaNs)
mean_temps = np.array([np.nanmean(t) if t.size else np.nan for t in temps_filtered])

# calculation
diff = np.abs(mean_temps[1]-mean_temps[2])

# example prints by integer index
# print("temps_filtered for mask 0:", temps_filtered_arr[0])   # array of temps for [5,7]

# ---------------------------
# Konsistente, saubere Ausgabe
# ---------------------------
print("\n" + "-"*55)
print(" TEMPERATURE STATISTICS")
print("-"*55 + "\n")

print(f"mean_T (all)        = {mean:6.2f}°C")
print(f"mean_T (may-july)   = {mean_temps[0]:6.2f}°C\n")

print(f"mean_T (may)        = {mean_temps[1]:6.2f}°C")
print(f"mean_T (july)       = {mean_temps[2]:6.2f}°C\n")

print(f"ΔT(may, july)       = |{mean_temps[1]:.2f}°C - {mean_temps[2]:.2f}°C| = {diff:.2f}°C\n")
print(f"data                = {data}\n")

print("-"*55 + "\n")
