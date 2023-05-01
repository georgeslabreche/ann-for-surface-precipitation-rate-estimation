#!/usr/bin/env python

import h5py
import numpy as np

from constants import *
from plot_utils import plot_tb, plot_tb_all

# read the TB data
# properties of the six GMI frequencies are determined by whether the TB measurement is warmer or colder than the background
# see: D'Adderio et al. 10.1016/j.atmosres.2022.106174
# https://www.sciencedirect.com/science/article/pii/S0169809522001600
gmi_tb_file_path = f'{DATA_DIR}/{DATA_FILENAME_TB}'

# open the data file
# todo: apply a filter to only keep data with the lat and lon values that are within the area interest
#       don't do it for this first experiment because we want to play with different areas of interest
hf = h5py.File(gmi_tb_file_path,'r')

# fetch TB data from Swath S1
lat_S1 = hf['S1/Latitude'][:]
lon_S1 = hf['S1/Longitude'][:]

# fetch the GPM Common Calibrated Brightness Temperature for channels 1 through 9
TB = hf['S1/Tc'][:]

# Central frequency: 10.65 GHz, IFOV size: 19x32 km
# TB warmer than background: emission from large raindrops (lower rain layers)
TB_10v = TB[:,:,0] # Vertical polarization
TB_10h = TB[:,:,1] # Horizontal polarization

# Central frequency: 18.7 GHz, IFOV size: 11x18 km
# TB warmer than background: emission from large raindrops (rain)
TB_19v = TB[:,:,2] # Vertical polarization
TB_19h = TB[:,:,3] # Horizontal polarization

# Central frequency: 23.8 GHz, IFOV size: 9.2x15 km
# TB warmer than background:
#   - emission from large raindrops (rain)
#   - emission from water vapour
TB_23v = TB[:,:,4] # Vertical polarization

# Central frequency: 36.5 GHz, IFOV size: 8.6x14 km
# TB warmer than background: emission from raindrops (rain)
# TB colder than background: scattering by large and dense ice (e.g. hail – deep convection)
TB_37v = TB[:,:,5] # Vertical polarization
TB_37h = TB[:,:,6] # Horizontal polarization

# Central frequency: 89.0 GHz, IFOV size: 4.4x7.2 km
# TB warmer than background: emission from water vapour and cloud liquid water
# TB colder than background: scattering by precipitating heavily rimed ice (e.g., graupel – convection/deep convection)
TB_89v = TB[:,:,7] # Vertical polarization
TB_89h = TB[:,:,8] # Horizontal polarization

# fetch TB data from Swath S2
lat_S2 = hf['S2/Latitude'][:]
lon_S2 = hf['S2/Longitude'][:]

# fetch the GPM Common Calibrated Brightness Temperature for channels 10 and 11
TB = hf['S2/Tc'][:]

# Central frequency: 166.5 GHz, IFOV size: 4.4x7.2 km
# TB warmer than background: emission from water vapour and cloud liquid water
# TB colder than background: scattering by less dense ice (snowflakes and aggregates – stratiform/convective precip)
TB_166v = TB[:,:,0] # Vertical polarization
TB_166v[TB_166v < 0] = np.NaN # NaN the -9999.9 missing value because there's a lot of them.
TB_166h = TB[:,:,1] # Horizontal polarization
TB_166h[TB_166h < 0] = np.NaN # NaN the -9999.9 missing value because there's a lot of them.

# close the data file
hf.close()

# collect the the vertically polarized TB data into a list
# each list item is data for a channel
TBs_V = [
  ('TB 10.65 GHz (V)', TB_10v),
  ('TB 18.7 GHz (V)', TB_19v),
  ('TB 23.8 GHz (V)', TB_23v),
  ('TB 36.5 GHz (V)', TB_37v),
  ('TB 89.0 GHz (V)', TB_89v),
  ('TB 166.5 GHz (V)', TB_166v)]

# collect the the horizontally polarized TB data into a list
# each list item is data for a channel
TBs_H = [
  ('TB 10.65 GHz (H)', TB_10h),
  ('TB 18.7 GHz (H)', TB_19h),
  None, # todo: look into why there is no horizontally polarized TB data in this channel
  ('TB 36.5 GHz (H)', TB_37h),
  ('TB 89.0 GHz (H)', TB_89h),
  ('TB 166.5 GHz (H)', TB_166h)]

# plot all the TBs!
# todo: optimize the processing time to render these plots
plot_tb_all(TBs_V,
  lat = lat_S1,
  lon = lon_S1,
  lat_bounds = LAT_BOUNDS_IONIAN_SEA,
  lon_bounds = LON_BOUNDS_IONIAN_SEA,
  colorAxisMin = 130,
  colorAxisMax = 300,
  #show = False,
  #filepath = 'figures/fig3_aoi_sea_gmi_v.png'
)

plot_tb_all(TBs_H,
  lat = lat_S1,
  lon = lon_S1,
  lat_bounds = LAT_BOUNDS_IONIAN_SEA,
  lon_bounds = LON_BOUNDS_IONIAN_SEA,
  colorAxisMin = 130,
  colorAxisMax = 300,
  #show = False,
  #filepath = 'figures/fig4_aoi_sea_gmi_h.png'
)