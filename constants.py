# the Cyclone Ianos, a.k.a. Medicane Ianos, occured on September 16, 2020
# it was a rare Medicane that impacted the eastern Mediterranean
# https://en.wikipedia.org/wiki/Cyclone_Ianos

# data types 1C correspond to Brightness Temperature (TB)
# the dataset is from when the Cyclone Ianos occured on September 16, 2020
DATA_FILENAME_TB = '1C-R.GPM.GMI.XCAL2016-C.20200916-S130832-E144106.037225.V07A.HDF5'

# data types 2A correspond to Precipitation
# the dataset is from when the Cyclone Ianos occured on September 16, 2020
DATA_FILENAME_PRECIPITATION = '2A.GPM.GMI.GPROF2021v1.20200916-S130832-E144106.037225.V07A.HDF5'

# data used for training
# training data: 13 channels for Brightness Temperature (TB) measurement
# target labels: the surface rain rates (RR)
# this training dataset is built from 10 orbits of March 2014 (i.e. not when the Medicane Ianos occured)
DATA_FILENAME_GMI_DPR_RR = 'dataset2_GMI_DPR_RR.nc'

# urls of the data
DATA_URLS = [
  f'https://get.ecmwf.int/repository/mooc-machine-learning-weather-climate/tier_3/observations/{DATA_FILENAME_TB}',
  f'https://get.ecmwf.int/repository/mooc-machine-learning-weather-climate/tier_3/observations/{DATA_FILENAME_PRECIPITATION}',
  f'https://get.ecmwf.int/repository/mooc-machine-learning-weather-climate/tier_3/observations/{DATA_FILENAME_GMI_DPR_RR}'
]

# the data directory path relative to the project home folder
DATA_DIR = "data"

# the models directory
MODELS_DIR = "models"

# the model filename
MODEL_FILENAME = 'mlp_model.h5'

# lat and lon bounding box bounds for the Ionian Sea
# this area is of interest because it captures the Medicane Ianos (a rare Mediterranean hurricane)
LAT_BOUNDS_IONIAN_SEA = [34, 40]
LON_BOUNDS_IONIAN_SEA = [14, 22]

# lat and lon bounding box bounds for southern US States near the Gulf of Mexico
# this area is of interest because it was in the path of Hurricane Ida's landfall
LAT_BOUNDS_IDA_LANDFALL = [29, 35]
LON_BOUNDS_IDA_LANDFALL = [-94, -86]