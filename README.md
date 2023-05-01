# ANN for Surface Precipitatioon Rate Estimation

Train a Multilayer Perceptrons (MLP) Neural Network model:
- The model predicts the surface rain rate (RR) given a set 13 channels for Brightness Temperature (TB) measurements.
- The model represents a simple Neural Network (NN) with two hidden layers and a final layer which is used to predict the target label.

## Area of Interest
The Area of Interest (AOI) is the Ionian Sea, as shown in Figure 1:

![AOI: The Ionian Sea.](/figures/fig1_aoi_ionian_sea.png)
**Figure 1: The area of interest for this experiment is the Ionian Sea.**

## Resources
- [ECMWF MOOC Machine Learning in Weather and Climate](https://github.com/ecmwf-projects/mooc-machine-learning-weather-climate/blob/main/tier_3/observations/mooc_tier3_1_ml_sat_panegrossi_v5.ipynb).
- [File Specification for GPM Products](https://gpm.nasa.gov/resources/documents/file-specification-gpm-products).
- [NASA PPS Storm website](https://storm.pps.eosdis.nasa.gov/storm/) to access the GPM products.

## Appendix: Getting Started
Instruction on how to install the application to train and apply the denoiser autoencoder model. Training images are not provided.

### Installation
Install the virtual environment:
```bash
pip install virtualenv
virtualenv venv
```

Activate the virtual environment in Linux:
```bash
source venv/bin/activate
```

In Windows:
```
.\venv\Scripts\activate
```

Install the application's Python package dependencies:
```
pip install -r requirements.txt
```

Deactivate the virtual environment:
```bash
deactivate
```

### Execution
Activate the virtual environment and execute the Python code.

Download the data products:
```bash
python 00_download_products.py
```

Visualize the GMI data on map:
```bash
python 01_map_products.py
```

Train a Multilayer Perceptrons (MLP) Neural Network model that predicts the surface rain rate (RR) given a set 13 channels for Brightness Temperature (TB) measurements.
```bash
python 02_train_ann.py
```