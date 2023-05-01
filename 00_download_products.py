import wget
import os
from constants import *

'''
The content of the GMI dataset is described by the File Specification for GPM Products:
https://gpm.nasa.gov/resources/documents/file-specification-gpm-products

ScanTime              A UTC time associated with the scan.

SCstatus              The status of the spacecraft.
                      5 properties: SCorientation, SClatitude, SClongitude, SCaltitude, and FractionalGranuleNumber

Latitude              The earth latitude of the center of the IFOV at the altitude of the earth ellipsiod.
                      Latitude is positive north, negative south.
                      Values range from -90 to 90 degrees.
                      Special values are defined as: -9999.9 Missing value.

Longitude             The earth longitude of the center of the IFOV at the altitude of the earth ellipsiod.
                      Longitude is positive east, negative west.
                      A point on the 180th meridian has the value -180 degrees.
                      Values range from -180 to 180 degrees.
                      Special values are defined as: -9999.9 Missing value.

sunLocalTime          The local hour angle of the Sun at the pixel location,
                      where 0 is midnight and 12 is local noon when the Sun crosses the local meridian. 
                      Also known as apparent solar time at any location.
                      In V7 TMI and GMI products will have values but partner products will be filled with the missing value.
                      Values range from 0 to 24 hours.
                      Special values are defined as: -9999.9 Missing value.

Quality               Quality of Tc in the swath.

incidenceAngle        Earth incidence angle.
                      The angle of the satellite from the local zenith as seen at the pixel location on the earth.
                      Values range from 0 to 90 degrees.
                      Special values are defined as: -9999.9 Missing value.

sunGlintAngle         Sun glint angle.
                      Angles greater than 127 degrees are set to 127.
                      Values range from 0 to 127 degrees.
                      Sun below horizon value is -88.
                      Missing value is -99.

incidenceAngleIndex   Contains a list of indeces of the incidence angle array and sun glint angle array.
                      See the description of the data array incidenceAngleIndex for details.

Tc                    GPM Common Calibrated Brightness Temperature.
                      The GMI is a conical-scanning radiometer measuring vertically (V) and horizontally (H) polarised radiances.
                      In 13 channels between 10.65 and 183.31 GHz.
                      Values range from 0 to 400 K.
                      Special values are defined as: -9999.9 Missing value.
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
