import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import warnings

# resolution: use 'h' for high or 'f' for full (much slower render time)
BASEMAP_RESOLUTION = 'l'

def plot_tb(TB, lat, lon, lat_bounds, lon_bounds, colorAxisMin, colorAxisMax):
  ''' Use Basemap to visualize brightness temperature (TB) products on a map.'''

  # the basemap bounding
 
  m = Basemap(projection = 'merc',
    resolution = BASEMAP_RESOLUTION,
    lat_ts = 20,
    llcrnrlat = lat_bounds[0],
    urcrnrlat = lat_bounds[1],
    llcrnrlon = lon_bounds[0],
    urcrnrlon = lon_bounds[1])

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


def plot_tb_all(TBs, lat, lon, lat_bounds, lon_bounds, colorAxisMin, colorAxisMax, show=True, filepath=None):
  ''' Loop through TB data for each channel and plot the data on a map.'''

  # create a figure to draw the data into a map plot
  fig = plt.figure(figsize=(24, 10))

  # draw the plots as subplots
  subplot_index = 1

  for TB in TBs:
    # plot location
    ax = fig.add_subplot(2, 3, subplot_index)

    # check that TB data is given
    if TB:
      # draw the plot for the TB at the given channel
      plot_tb(TB[1], lat, lon, lat_bounds, lon_bounds, colorAxisMin, colorAxisMax)

      # plot title
      plt.title(TB[0])

    else:
      # draw empty plot if no TB data for the channel
      plt.axis('off')

    # increment index for the placement of the next subplot
    subplot_index += 1

  # write the plots into an image file
  if filepath:
    plt.savefig(
      f'{filepath}',
      bbox_inches='tight',
      dpi = 300)

  # show the plots!
  if show: plt.show()


def plot_rr(RR, lat, lon, lat_bounds, lon_bounds, colorAxisMin, colorAxisMax, show=True, filepath=None):
  ''' Use Basemap to visualize rainfall rates (surface precipitation) products on a map.'''

  fig = plt.figure()
  ax = fig.add_subplot(111)

  # the basemap bounding
  # resolution: use 'h' for high or 'f' for full (much slower render time)
  m = Basemap(projection = 'merc',
    resolution = BASEMAP_RESOLUTION,
    lat_ts = 20,
    llcrnrlat = lat_bounds[0],
    urcrnrlat = lat_bounds[1],
    llcrnrlon = lon_bounds[0],
    urcrnrlon = lon_bounds[1])

  # set min/max values of the colorbar
  with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    im1 = m.pcolor(lon[:], lat[:], RR[:],
      shading = 'nearest',
      cmap = 'turbo',
      latlon = True,
      vmin = colorAxisMin,
      vmax = colorAxisMax)

  # draw coast lines
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
  cbar.set_label('Rainfall Rate [mm/h]')

  # add title
  plt.title('Surface Precipitation', fontsize=12)

  # write the plots into an image file
  if filepath:
    plt.savefig(
      f'{filepath}',
      bbox_inches='tight',
      dpi = 300)

  # show the plots!
  if show: plt.show()