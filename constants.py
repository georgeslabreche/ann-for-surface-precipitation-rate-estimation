# data types 1C correspond to Brightness Temperature (TB)
DATA_FILENAME_TB = '1C-R.GPM.GMI.XCAL2016-C.20200916-S130832-E144106.037225.V07A.HDF5'

# data types 2A correspond to Precipitation
DATA_FILENAME_PRECIPITATION = '2A.GPM.GMI.GPROF2021v1.20200916-S130832-E144106.037225.V07A.HDF5'

# data used for training
# training data: 13 channels for Brightness Temperature (TB) measurement
# target labels: the surface rain rates (RR)
DATA_FILENAME_GMI_DPR_RR = 'dataset2_GMI_DPR_RR.nc'

# urls of the data
DATA_URLS = [
  f'https://get.ecmwf.int/repository/mooc-machine-learning-weather-climate/tier_3/observations/{DATA_FILENAME_TB}',
  f'https://get.ecmwf.int/repository/mooc-machine-learning-weather-climate/tier_3/observations/{DATA_FILENAME_PRECIPITATION}',
  f'https://get.ecmwf.int/repository/mooc-machine-learning-weather-climate/tier_3/observations/{DATA_FILENAME_GMI_DPR_RR}'
]

# the data directory path relative to the project home folder
DATA_DIR = "data"

# lat and lon bounding box bounds for the Ionian Sea on 16/09/2020
# this are is of interest becasue it captures the Mediterranean Hurricane (Medicane)
# over the Ionian Sea between Southern Italy and Greece.
LAT_BOUNDS_IONIAN_SEA = [34, 40]
LON_BOUNDS_IONIAN_SEA = [14, 22]