# CIND 820: Big Data Analytics Project

### Introduction

This repository includes all relevant documentation pertaining to CIND820: Big Data Analytics Project.
This project uses 4 machine learning algorithms to compare their performance in predicting future credit card default of borrowers using an open-source dataset.

### Methodology and Stages
The stages of this project are as follows:
- Abstract: Introduction to methodology and dataset and outlining goals of study
- Literature Review: Review of existing literature in this and closesly-related areas of study
- Data Processing: Open-source dataset is transformed and made fit for model intake
- Model Implementation: Each machine learning algorithm is trained, tested and evaluated on dataset
- Report: Results of model implementation are analyzed and contextualized. Summary, findings and limitations/next steps provided.

### Contents
The contents of this repository are provided below. All reports derived from Python code are included in both source and Jupyter Notebook format, where code results are embedded in each document.
- Abstract - Text Document
- Literature Review - Text Document
- Dataset - Microsoft Excel Document
- Cleaned Dataset - Preprocessed dataset - Microsoft Excel Document
- Code - Folder of .ipynb documents for each model and each dataset combination. Includes custom evaluation.py class for evaluating ML models
- Results - HTML versions of above code notebooks with results embedded in documents
- Table of Results - Human-readable table of results of performance of all algorithms

### Model Implementation
The high-level methodology for the implementation of each machine learning algorithm is as follows:
- Applied to pre-processed, randomly-split dataset and results recorded
- Applied to same dataset with cross validation and results compared
- Model-specific algorithm applied to limit the number of features included in model (for ex. Feature Importance for Decision Tree)
- Model reapplied to same dataset using limited features and random split
- Model cross-validated again using limited feature and performance compared
- For each model, the above steps are repeated, using the factorized version of the dataset sourced in the feature selection step. 
- Results are compared between numerical and factorized datset using same algorithm
