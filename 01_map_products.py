
import h5py
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import warnings

from constants import *

'''
Use Basemap to visualize brightness temperature (TB) products into maps
'''

# defining the funcion to plot
def plot_tb(TB, lat, lon, lat_bounds, lon_bounds, colorAxisMin, colorAxisMax):

  # the basemap bounding 
  m = Basemap(projection = 'merc',
    resolution = 'l',
    lat_ts = 20,
    llcrnrlat = lat_bounds[0],
    urcrnrlat=lat_bounds[1],
    llcrnrlon = lon_bounds[0],
    urcrnrlon=lon_bounds[1])

  # set min/max values of the colorbar
  with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    im1 = m.pcolor(lon[:], lat[:] ,TB[:],
    shading = 'nearest',
    cmap = 'turbo',
    latlon = True,
    vmin = colorAxisMin,
    vmax = colorAxisMax)

  # draw the coast lines
  m.drawcoastlines()

  # set parallels and meridians
  dparal = 2 #separation in deg between drawn parallels
  parallels = np.arange(lat_bounds[0], lat_bounds[1], dparal)
  dmerid = 2 #separation in deg between drawn meridians
  meridians = np.arange(lon_bounds[0], lon_bounds[1], dmerid)
  m.drawparallels(parallels, labels=[1,0,0,0], fontsize=15)
  m.drawmeridians(meridians, labels=[0,0,0,1], fontsize=15)

  # add colorbar.
  cbar = m.colorbar(location='right', pad="5%")
  cbar.set_label('Kelvin (K)') # temperature in Kelvin

# read the TB data
# properties of the six GMI frequencies are determined by whether the TB measurement is warmer or colder than the background
# see: D'Adderio et al. 10.1016/j.atmosres.2022.106174
# https://www.sciencedirect.com/science/article/pii/S0169809522001600
gmi_tb_file_path = f'{DATA_DIR}/{DATA_FILENAME_TB}'

# open the data file
# todo: apply a filter to only keep data with the lat and lon values that are within the area interest
# don't do it for this first experiment because we want to play with different areas of interest
hf = h5py.File(gmi_tb_file_path,'r')

# fetch TB data from Swath S1
lat_S1 = hf['S1/Latitude'][:]
lon_S1 = hf['S1/Longitude'][:]

# fetch the GPM Common Calibrated Brightness Temperature for channels 1 through 9
TB = hf['S1/Tc'][:]

# Central frequency: 10.65 GHz, IFOV size: 19x32 km
# TB warmer than background: emission from large raindrops (lower rain layers)
TB_10v = TB[:,:,0] # Vertical Polarisation
TB_10h = TB[:,:,1] # Horizontal Polarisation

# Central frequency: 18.7 GHz, IFOV size: 11x18 km
# TB warmer than background: emission from large raindrops (rain)
TB_19v = TB[:,:,2] # Vertical Polarisation
TB_19h = TB[:,:,3] # Horizontal Polarisation

# Central frequency: 23.8 GHz, IFOV size: 9.2x15 km
# TB warmer than background:
#   - emission from large raindrops (rain)
#   - emission from water vapour
TB_23v = TB[:,:,4] # Vertical Polarisation

# Central frequency: 36.5 GHz, IFOV size: 8.6x14 km
# TB warmer than background: emission from raindrops (rain)
# TB colder than background: scattering by large and dense ice (e.g. hail – deep convection)
TB_37v = TB[:,:,5] # Vertical Polarisation
TB_37h = TB[:,:,6] # Horizontal Polarisation

# Central frequency: 89.0 GHz, IFOV size: 4.4x7.2 km
# TB warmer than background: emission from water vapour and cloud liquid water
# TB colder than background: scattering by precipitating heavily rimed ice (e.g., graupel – convection/deep convection)
TB_89v = TB[:,:,7] # Vertical Polarisation
TB_89h = TB[:,:,8] # Horizontal Polarisation

# fetch TB data from Swath S2
lat_S2 = hf['S2/Latitude'][:]
lon_S2 = hf['S2/Longitude'][:]

# fetch the GPM Common Calibrated Brightness Temperature for channels 10 and 11
TB = hf['S2/Tc'][:]

# Central frequency: 166.5 GHz, IFOV size: 4.4x7.2 km
# TB warmer than background: emission from water vapour and cloud liquid water
# TB colder than background: scattering by less dense ice (snowflakes and aggregates – stratiform/convective precip)
TB_166v = TB[:,:,0] # Vertical Polarisation
TB_166v[TB_166v < 0] = np.NaN # NaN the -9999.9 missing value because there's a lot of them.
TB_166h = TB[:,:,1] # Horizontal Polarisation

# close the data file
hf.close()

# create a figure to draw the data into a map plot
fig = plt.figure(figsize=(24, 16))

# draw the plots as subplots
subplot_index = 1

# loop through the TB data with vertical polarisation and plot each of them
for TB in [('TB 10.65 GHz (V)', TB_10v), ('TB 18.7 GHz (V)', TB_19v), ('TB 23.8 GHz (V)', TB_23v), ('TB 36.5 GHz (V)', TB_37v), ('TB 89.0 GHz (V)', TB_89v), ('TB 166.5 GHz (V)', TB_166v)]:

  # plot location
  ax = fig.add_subplot(2, 3, subplot_index)

  # draw the plot for the TB at the given channel
  plot_tb(TB[1], lat_S1, lon_S1, LAT_BOUNDS_IONIAN_SEA, LON_BOUNDS_IONIAN_SEA, colorAxisMin=130, colorAxisMax=300)

  # plot title
  plt.title(TB[0])

  # increment index for the placement of the next subplot
  subplot_index += 1

# show the plots!
plt.show()