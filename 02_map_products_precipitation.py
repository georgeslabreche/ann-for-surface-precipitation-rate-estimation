#!/usr/bin/env python

import h5py
import numpy as np
import warnings

from constants import *
from plot_utils import plot_rr

# read the TB data
gmi_precipitation_file_path = f'{DATA_DIR}/{DATA_FILENAME_PRECIPITATION}'

# open the data file
# todo: apply a filter to only keep data with the lat and lon values that are within the area interest
#       don't do it for this first experiment because we want to play with different areas of interest
hf = h5py.File(gmi_precipitation_file_path,'r')

# fetch TB data from Swath S1
lat_S1 = hf['S1/Latitude'][:]
lon_S1 = hf['S1/Longitude'][:]

# fetch surface precipitation
# use the "rr" variable to denote "rainfall rate"
rr = hf['S1/surfacePrecipitation'][:]
rr[rr < 0] = np.NaN # NaN the -9999.9 missing values

# plot the data on a map
plot_rr(
  RR = rr,
  lat = lat_S1,
  lon = lon_S1,
  lat_bounds = LAT_BOUNDS_IONIAN_SEA,
  lon_bounds = LON_BOUNDS_IONIAN_SEA,
  colorAxisMin = 0,
  colorAxisMax = 40,
  title = "Estimated Rainfall Rate",
  #show = False,
  #filepath = "figures/fig5_aoi_sea_rr.png"
)