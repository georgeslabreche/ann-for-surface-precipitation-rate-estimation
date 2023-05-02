#!/usr/bin/env python

import os
import pandas as pd
import numpy as np
import xarray as xr
import warnings

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras import optimizers
from tensorflow.keras import utils
import tensorflow as tf

import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
warnings.filterwarnings("ignore")

from constants import *
from plot_utils import plot_learning_curves

'''
Train a Multilayer Perceptrons (MLP) Neural Network model
  - The model predicts the surface rain rate (RR) given a set 13 channels for Brightness Temperature (TB) measurements
  - The model represents a simple Neural Network (NN) with two hidden layers and a final layer which is used to predict the target label.

The comments that explains the process in this source code are taken from:
https://github.com/ecmwf-projects/mooc-machine-learning-weather-climate

The dataset used for training and test of the NN is built from 10 GMI orbits (from 9th March 2014):
  - The 13 features correspond exactly to the 13 GMI channels.
  - The rainfall rate represents the target variable and has been obtained from the NASA GMI/DPR Level 2 precipitation product (2B-CMB).

This algorithm combines GMI measurements with the reflectivity profiles measured by the Dual-frequency Precipitation Radar (DPR) on board the GPM Core Observatory.
The Observatory is the first spaceborne radar operating at Ka and Ku band and provides vertical profiles of liquid and solid precipitation microphysics, and precipitation rate near the surface.
Some details on the 2B-CMB algorithm can be found in GMI/DPR Level 2 Algorithm Theoretical Basis Document (ATBD):
https://gpm.nasa.gov/resources/documents/gpmdpr-level-2-algorithm-theoretical-basis-document-atbd

The GMI TBs and the DPR rainfall rates (from 2B-CMB) have been matched to build the dataset using a nearest neighbour approach.
Only pixels over ocean and sea where rainfall has been observed (2B-CMB rainfall rate > 0 mm/h) are selected to build the dataset (for a total of 61,906 pixels).

The training dataset is built from 10 orbits of March 2014.
'''

# the model hyperparameters

# the learning rate is the step size at each iteration while moving toward a minimum of a loss function
LEARNING_RATE = 0.001

# an epoch in machine learning means one complete pass of the training dataset through the algorithm
EPOCHS = 1600

# the batch size is the number of training examples utilized in one iteration
# a large batch size should make the training faster but may lead to memory saturation
BATCH_SIZE = 8000

# Create the models directory if it doesn't exist
if not os.path.exists(MODELS_DIR):
  os.makedirs(MODELS_DIR)


# splitting the dataset
def split_dataset(dataset, label_dataset):
  ''' this function splits the dataset between training and test datasets

  'X' represents training data and 'y' represents the target label
  opt for 50% split between training and test set because the the training set is quite small
  '''

  choice = np.mod(range(0, len(tensor_df)), 2) == 0 # this variable is true for even positions in the obseravtions sequence
  X_train = dataset[choice == 0]
  X_test = dataset[choice]
  y_train = label_dataset[choice == 0]
  y_test = label_dataset[choice]

  # return the split dataset
  return X_train, X_test, y_train, y_test


# training phase with the training dataset
def train():
  '''create a simple model architecture given the small training dataset

  construct a MLP model with two hidden layers:
    - the first layer contains 10 perceptrons
    - the second is made of 20 perceptrons

  use a sigmoid activation function (transfer function used in both hidden layers)
  use the mean squared error (MSE) as loss function to be minimised
  display the mean average error (MAE) for each training iteration (epoch)
  '''

  # here the network achitecture is defined: it is a feed forward neural network with 2 hidden layers
  # 20 perceptrons in the fisrt hidden layer and 10 in the second.
  # sigmoids are used as transfer function in both hidden layers
  model = Sequential()
  model.add(Dense(20, input_dim=input_shape, kernel_initializer='normal', activation='sigmoid')) # first hidden layer
  model.add(Dense(10, kernel_initializer='normal', activation='sigmoid')) # second hidden layer
  model.add(Dense(1, kernel_initializer='normal', activation='linear')) # output
  model.summary()

  # the optimizer is the algorithm used for the training.
  # Adam is a standard choice, but Scale conjugate gradient (SGD), is also very efficient.
  optimizer = optimizers.Adam(lr=LEARNING_RATE)
  #optimizer = optimizers.experimental.SGD(learning_rate=LEARNING_RATE1)

  # here the model optimzer and the loss function to be minimized during training (mean squared error, MSE) are defined
  # the mean absolute error (mae) is also computed as additional metrics
  model.compile(optimizer=optimizer, loss='mean_squared_error', metrics=['mae'])

  # the training dataset, the batch size and the number of epochs to be used re defined
  # validation is also carried out
  # monitoring loss and metrics on the test dataset
  # at the end of each epoch
  history = model.fit(
    X_train_scaled,
    y_train,
    batch_size = BATCH_SIZE,
    epochs = EPOCHS,
    validation_data = (X_test_scaled, y_test),)

  # the model is saved at the end of the training phase in an HFD5 output file
  model.save(f'{MODELS_DIR}/{MODEL_FILENAME}')

  # retuurn the mode and history
  return model, history


# path of the nc data file with training data (TBs) and target labels (surface rain rates)
# the training dataset is built from 10 orbits of March 2014
data_filepath = f'{DATA_DIR}/{DATA_FILENAME_GMI_DPR_RR}'

# read the dataset
ds = xr.open_dataset(data_filepath)

# the training data (the TBs)
train_df = ds['tb'].to_dataframe().unstack()

# the target labels (the surface rain rate)
target = ds['rr'].to_dataframe()

# that amount of data that we're dealing with
print('The shape of the TB features data is', train_df.shape)
print('The shape of the surface rain rate label data is', target.shape)

# conver the dataframes into tensors
tensor_df = tf.convert_to_tensor(train_df, dtype=np.float)
label_df = tf.convert_to_tensor(target, dtype=np.float)

X_train, X_test, y_train, y_test = split_dataset(tensor_df, label_df)

# scaling: standardize features by removing the mean and scaling to unit variance
scaler = StandardScaler()

# mean and variance are calculated on the training dataset and applied to the training dataset
X_train_scaled = scaler.fit_transform(X_train)

# mean and variance (previously calculated) are applied to the test dataset
X_test_scaled = scaler.transform(X_test)

# print the result of splitting the dataset
print('The shape of the training dataset is', X_train.shape)
print('The shape of the test dataset is', X_test.shape)

# set the input shape
input_shape = X_train.shape[1]
print(f'Feature shape, i.e. number of TB channels: {input_shape}')

# for trainig with CPU (Slower)
model, history = train()

# for trainig with GPU (Faster) uncomment next 2 lines.
#with tf.device("/device:GPU:0"):
#  model, history = train()

# plot the training's learning curve
plot_learning_curves(history,
  #show = False,
  #filepath = "figures/fig6_ann_sea_learning_curves.png"
)