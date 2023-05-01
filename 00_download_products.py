#!/usr/bin/env python

import wget
import os
from constants import *

'''
The content of the GMI dataset is described by the File Specification for GPM Products:
https://gpm.nasa.gov/resources/documents/file-specification-gpm-products

Within the scope of this project we are interested in the following properties:

Latitude              The earth latitude of the center of the IFOV at the altitude of the earth ellipsiod.
                      Latitude is positive north, negative south.
                      Values range from -90 to 90 degrees.
                      Special values are defined as: -9999.9 Missing value.

Longitude             The earth longitude of the center of the IFOV at the altitude of the earth ellipsiod.
                      Longitude is positive east, negative west.
                      A point on the 180th meridian has the value -180 degrees.
                      Values range from -180 to 180 degrees.
                      Special values are defined as: -9999.9 Missing value.

Tc                    GPM Common Calibrated Brightness Temperature.
                      The GMI is a conical-scanning radiometer measuring vertically (V) and horizontally (H) polarised radiances.
                      In 13 channels between 10.65 and 183.31 GHz.
                      Values range from 0 to 400 K.
                      Special values are defined as: -9999.9 Missing value.


The contents of the GPROF Profiling dataset with are also detailed in the File Specification for GPM Product.
The dataset includes computed vertical hydrometeor profiles for precipitation.
Within the scope of this project we are interested in the surface precipitation measurements:

surfacePrecipitation  The monthly mean of the instantaneous precipitation rate at the surface for each grid.
                      Values range from 0 to 3000 mm/hr.
                      Special values are defined as: -9999.9 Missing value
'''


# Create the data directory if it doesn't exist
if not os.path.exists(DATA_DIR):
  os.makedirs(DATA_DIR)

# a function to download the data that hasn't already been downloaded
def download_data(urls):
  for url in urls:
    data_filename = os.path.basename(url)
    download_file_path = os.path.join(DATA_DIR, data_filename)

    if not os.path.exists(download_file_path):
      print(f"downloading {data_filename}")
      wget.download(url, download_file_path)
    else:
      print(f"already downloaded: {data_filename}")

# download the data
download_data(DATA_URLS)
