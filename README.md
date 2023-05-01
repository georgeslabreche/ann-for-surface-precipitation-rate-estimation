# ANN for Surface Precipitation Rate Estimation

Using data products from the Global Precipitation Measurement Mission (GPM) to train an Artificial Neural Network (ANN) for surface precipitation rate estimation. Train a Multilayer Perceptrons (MLP) Neural Network model:
- The model predicts the surface rain rate (RR), a.k.a. precipitation rate, given a set 13 channels for Brightness Temperature (TB) measurements.
- The model represents a simple Neural Network (NN) with two hidden layers and a final layer which is used to predict the target label.

This project is a follow up to the study done in [[1](https://github.com/ecmwf-projects/mooc-machine-learning-weather-climate), [2](https://www.sciencedirect.com/science/article/pii/S0169809522001600), [3](https://doi.org/10.1016/j.atmosres.2022.106174)]. Much of the source code and code comments are taken from [[1](https://github.com/ecmwf-projects/mooc-machine-learning-weather-climate)] and adapated or refactored for the purpose of furthering the model's prediction capabilities to cover land areas.

The model's estimation over land and coastal areas are not reliable because the training data does not include measurements over land. This project aims to tackle the complexities of precipitation retrieval over land and evaluate the resulting model's reliability over different land areas of interests.

Note that the models trained in this project use a small training dataset of 10 orbits and are thus unsuitable for operational applications.

The goals of this projects are to:
1. Familiarize with the [Global Precipitation Measurement Mission (GPM)](https://gpm.nasa.gov/missions/GPM) and the specification of its data products.
2. Understand the properties of the [GPM Microwave Imager (GMI)](https://gpm.nasa.gov/missions/GPM/GMI) channel frequencies and how to inrepret them into weather characteristics. For instance, at a central frequency of 36.5 GHz the Brightness Temperature (TB) measurements that are colder than background stem from the scattering by large and dense ice (e.g. hail – deep convection) [[3](https://doi.org/10.1016/j.atmosres.2022.106174)].
3. Understand how adding or removing some GMI channels from the training dataset affect the model's predictions. For instance, by removing or only considering the channels at a central frequency of 10.65 GHz since they are more directly impacted by surface precipitation where a TB warmer than background indicates emissions from large raindrops that are present in the lower rain layers [[3](https://doi.org/10.1016/j.atmosres.2022.106174)].
4. Appreciate the complexities of precipitation retrieval over land and how they hinder our ability to train a neural network for weather and climate predictions over land.

## Area of Interest
Two areas of interest (AOI) are selected to experiment with ANN for precipitation rate estimation over sea and land. The AOI over sea is taken from [[1](https://github.com/ecmwf-projects/mooc-machine-learning-weather-climate)]. The area over land is TBD.

### Over Sea
The AOI over sea is the Ionian Sea, as shown in Figure 1:

![Figure 1: Area of interest over the Ionian Sea.](./figures/fig1_aoi_ionian_sea.png)

**Figure 1: Area of interest over the Ionian Sea.**

### Over Land
The AOI over land is TBD. It will probably be over the Balkans in order to favor a study over Europe that has not benefited as much from past research.

**Figure 2: Area of interest over TBD.**

## Mapped Data Products
Map the measurements taken by GPM to better understand the distribution of measurements across the entire AOI.

### Brightness Temperature (TB)

![Figure 3: Vertically polarized GMI TB measurements over the Ionian Sea (September 16, 2020).](./figures/fig3_aoi_sea_gmi_v.png)

**Figure 3: Vertically polarized GMI TB measurements over the Ionian Sea (September 16, 2020).**

![Figure 4: Horizontally polarized GMI TB measurements over the Ionian Sea (September 16, 2020).](./figures/fig4_aoi_sea_gmi_h.png)

**Figure 4: Horizontally polarized GMI TB measurements over the Ionian Sea (September 16, 2020).**

### Surface Precipitation (Rainfall Rate)

![Figure 5: Surface preciptation (rainfall rate) over the Ionian Sea (September 16, 2020).](./figures/fig5_aoi_sea_rr.png)

**Figure 5: Surface preciptation (rainfall rate) over the Ionian Sea (September 16, 2020).**

## References
[1] [ECMWF MOOC Machine Learning in Weather and Climate](https://github.com/ecmwf-projects/mooc-machine-learning-weather-climate).

[2] Sanò, P., Panegrossi, G., Casella, D., Marra, A.C., D'Adderio, L.P., Rysman, J.F., & Dietrich, S. (2018). [The Passive Microwave Neural Network Precipitation Retrieval (PNPR) Algorithm for the CONICAL Scanning Global Microwave Imager (GMI) Radiometer](https://www.sciencedirect.com/science/article/pii/S0169809522001600). _Remote Sens_, 10, 1122.

[3] D'Adderio L.P., Casella D., Dietrich S., Sanò P., & Panegrossi G. (2022). [GPM-CO observations of Medicane Ianos: Comparative analysis of precipitation structure between development and mature phase](https://doi.org/10.1016/j.atmosres.2022.106174). _Atmospheric Research_, Volume 273.

[4] [File Specification for GPM Products](https://gpm.nasa.gov/resources/documents/file-specification-gpm-products).

[5] [NASA PPS Storm website](https://storm.pps.eosdis.nasa.gov/storm/).

[6] [GPM GPROF Algorithm Theoretical Basis Document (ATBD)](https://gpm.nasa.gov/resources/documents/gpm-gprof-algorithm-theoretical-basis-document-atbd).

## Appendix: Getting Started
Instructions on how to prepare the virtual environment and install the Python package dependencies.

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
python 01_map_products_gmi.py
```

Visualize the precipitation data on map:
```bash
python 02_map_products_precipitation.py
```

Train a Multilayer Perceptrons (MLP) Neural Network model that predicts the surface rain rate (RR) given a set 13 channels for Brightness Temperature (TB) measurements.
```bash
python 03_train_sea_ann.py
```