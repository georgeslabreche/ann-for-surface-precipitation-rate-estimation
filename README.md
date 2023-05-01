# ANN for Surface Precipitatioon Rate Estimation

## Motivation
TODO

## Area of Interest
The Area of Interest (AOI) is the Ionian Sea, as shown in Figure 1:

![AOI: The Ionian Sea.](/figures/fig1_aoi_ionian_sea.png)
**Figure 1: The area of interest for this experiment is the Ionian Sea.**

## Resources
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

Activate the environment in Linux:
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

Run the application
```bash
python train.py
```

Deactivate the environment:
```bash
deactivate
```

### Execution
TODO

