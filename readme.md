# FEAST Feature Store Customer churn for scaling ML model

## Project Overview

### Business Overview

Feast (Feature Store) is a vital component of operational data systems, designed to manage and serve machine learning features to models in production. It addresses significant challenges in machine learning projects, such as ensuring consistent data access for modeling, deploying new features to production, maintaining point-in-time data correctness, and reusability of features across projects. Feast achieves these goals through an operational data system that serves feature data to models from both low-latency online stores and scalable offline stores.

---

### Aim

The primary objectives of this project is to predict customer churn using the Feast Feature Store for scaling ML model.

---

### Data Description

The dataset used for this project contains information about customer churn, with 8 distinct features. The dataset comprises data from 891 customers and includes the following features:

1. Created_at
2. Customer_id
3. Churned
4. Category
5. Sex
6. Age
7. Order gmv
8. Credit type

---

### Tech Stack

- Language: `Python`
- Libraries: `Feast`, `Pandas`, `Scikit-learn`, `Flask`, `Pickle`

---

### Approach

The project follows these key steps:

1. Feast installation and setup
2. Offline store and retrieval
3. Online store and retrieval
4. Training data creation using Feast
5. Model training with Random Forest and Gradient Boosting
6. Real-time predictions using Feast
7. Interactive model deployment using Feast

---

## Modular Code Overview

1. `src`: This folder contains all the modularized code for each project phase, including feature engineering, model training, and deployment. It includes Python scripts such as `ML_pipeline`, `Engine.py`, and `Deploy_postman.py` for different functionalities.

2. `output`: The "output" folder contains the trained models used for predictions. These prebuilt models can be quickly loaded for future use, saving time on model training.

3. `feast_repo`: This folder is used for Feast-related files and configuration. It includes data, `example.py` for feature store creation, `feature_store.yaml` for configuring the feature store, and the "Feast - Feature Store.ipynb" notebook for exploring Feast.

4. `requirements.txt`: The file lists all the required libraries and their respective versions for easy installation using `pip`.

---

### Key Concepts Explored

1. Introduction to Feast and its role in machine learning projects
2. Installation and setup of Feast for feature management
3. Understanding Feast entities, feature views, and architecture
4. Online store and offline store concepts
5. Data retrieval in Feast and available commands
6. Training data creation using Feast for machine learning models
7. Model training using both Random Forest and Gradient Boosting
8. Real-time predictions using Feast
9. Deployment of Feast using Postman for interactive use cases

---


