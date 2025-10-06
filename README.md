# Mini Project for Data Science 1, by Bálint Décsi
（￣︶￣）↗　Welcome!
## Intro
This is my submission for the *ECBS5293 - Data Science 1* class in 2025/26 Fall term. Here is every info needed for the usage of code and data and reproduction of results.

## Data
The dataset includes information on price and features of hotels in Vienna for one date. It was scraped from a price comparison website. It was anonymized and slightly altered to ensure confidentiality. The dataset's README can be found [here](https://gabors-data-analysis.com/datasets/hotels-vienna/).

## Folder structure
I use a `cookiecutter`-like structure. The tree is as follows:
```
├── code
├── data
│   ├── derived
│   └── raw
└── reports
    └── figures
```

## Getting started
I've added the output data and figures for illustrations purposes. They can be reproduced like so:
```bash
git clone https://github.com/balintdecsi/ceu-ds-1-mini-project
cd ceu-ds-1-mini-project
conda env create -f environment.yaml
conda activate ceu-ds-1-mini-project
python3 code/analyse_hotels.py
```
