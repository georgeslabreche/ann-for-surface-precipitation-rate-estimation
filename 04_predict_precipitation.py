#!/usr/bin/env python

import h5py
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler

from constants import *
from plot_utils import plot_rr

# open and read the TB data file
gmi_file_path = f'{DATA_DIR}/{DATA_FILENAME_TB}'
hf = h5py.File(gmi_file_path,'r')

# fetch model input values
lat_S1 = hf['S1/Latitude'][:]
lon_S1 = hf['S1/Longitude'][:]
TB_S1 = hf['S1/Tc'][:]
TB_S2 = hf['S2/Tc'][:]

# close the the TB data file
hf.close()

# merge the two TB data sources into a single data object
TB = np.concatenate((TB_S1, TB_S2,), axis=2)
TB = np.reshape(TB, (2963*221, 13))
TB[np.any(TB<=0, axis=1),:] = np.NaN # NaN the missing values

# scaling: standardize features by removing the mean and scaling to unit variance
scaler = StandardScaler()

# mean and variance are calculated on the input dataset
# todo: however, variance are calculated might have to be calculated on the same dataset used to train the model?
scaler.fit_transform(TB)

# load the model
model = tf.keras.models.load_model(f'{MODELS_DIR}/{MODEL_FILENAME}')

# check its architecture
model.summary()

# make predictions
rr_predictions = model.predict(TB)

# plot the predicted precipitation on a map (reshape it first so it can be plotted)
rr_predictions = np.reshape(rr_predictions, (2963, 221))

# plot the estimated precipitation on a map
plot_rr(
  RR = rr_predictions,
  lat = lat_S1,
  lon = lon_S1,
  lat_bounds = LAT_BOUNDS_IONIAN_SEA,
  lon_bounds = LON_BOUNDS_IONIAN_SEA,
  colorAxisMin = 0,
  colorAxisMax = 40,
  title = "Estimated Surface Precipitation",
  #show = False,
  #filepath = "figures/fig7_aoi_sea_rr_estimated.png"
)
