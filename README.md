# 🌟 Rent Madrid

<div style="text-align: center;">
  <img src="assets/home_for_rent.jpg" alt="Project Cover" />
</div>

## 📝 Project Overview

**Rent Madrid** is a machine learning project aimed at predicting rental prices for properties in Madrid using a detailed dataset of property features. This project bridges the fields of real estate and data science, providing insights and predictions that can support stakeholders such as real estate agents, landlords, and renters in decision-making processes.

### 🚀 Features

The steps to complete this project consist of:

1. **Data Cleaning:** Preparation of data for EDA.
2. **Exploratory Data Analysis (EDA):** Extraction of insights to drive modelling thought process.
3. **Pipeline preprocessing:** Preprocessing via Sklearn Piplines to promote robustness and avoid data-leakage.
4. **Model Evaluation:** ML models and their configurations. Featuring MLflow for model tracking.
5. **Streamlit App:** A user-friendly interface to allow for simulation of rent prices by generating predictions from user input.

## 🏢 Context and Problem Statement

The real estate market is highly dynamic and influenced by numerous factors, including location, property attributes, and broader economic conditions. Accurate rental price predictions can be a powerful tool for various stakeholders, enabling better pricing strategies and decisions. This project dives into the complexities of the real estate market by analyzing a dataset of rental properties in Madrid and leveraging machine learning to build a predictive model.

### 📊 Dataset Description

The dataset contains 40 columns of detailed property information, including:

- **Key Attributes:**
  - `propertyCode`: Unique identifier for each property.
  - `price`: Target variable—property rental price in euros.
  - `propertyType`: Property type (e.g., apartment, penthouse, chalet).
  - `size`: Property size in square meters.
  - `rooms`: Number of bedrooms.
  - `bathrooms`: Number of bathrooms.
  - `district` and `neighborhood`: Location-based attributes.

- **Additional Features:**
  - `latitude` and `longitude`: Geographical coordinates.
  - `address`: Approximate property address.
  - `exterior`, `hasLift`: Boolean flags for additional features.
  - `priceByArea`: Price per square meter.
  - `description`: Textual description of the property.

The dataset also includes indicators such as `hasVideo`, `has3DTour`, and `newDevelopment`, providing detailed insights into property listings.


## 📁 Project Structure

```bash
project-name/
├── assets/                 # Images or other assets
├── datos/                  # Raw or preprocessed data files
├── mlruns/                 # MLflow experiment tracking
├── model_tr/               # Trained models
├── model_tracking/         # Files for model tracking
├── notebooks/              # Jupyter notebooks for various stages
│   ├── 0_cleaning.ipynb        # Data cleaning
│   ├── 1_exploration_v1.ipynb  # Initial exploration
│   ├── 2_preprocessing_v1.ipynb # Preprocessing version 1
│   ├── 2_1_preprocessing_v2.ipynb # Preprocessing version 2
│   ├── 3_modelling.ipynb       # Modeling notebook
├── src/                    # Core project scripts
├── streamlit/              # Streamlit app files
│   ├── main.py                 # Main app
├── Pipfile                 # Pipenv configuration file
├── Pipfile.lock            # Lock file for environment dependencies
└── README.md               # Project documentation
```

## 🛠️ Installation and Requirements

This project requires Python 3.11 and the following tools and libraries to run:

- [scipy](https://docs.scipy.org/doc/scipy/)  
- [pandas](https://pandas.pydata.org/docs/)  
- [numpy](https://numpy.org/doc/)  
- [scikit-learn](https://scikit-learn.org/stable/documentation.html)  
- [seaborn](https://seaborn.pydata.org/)  
- [matplotlib](https://matplotlib.org/stable/users/index.html)  
- [tqdm](https://tqdm.github.io/)  
- [statsmodels](https://www.statsmodels.org/stable/index.html)  
- [mlflow](https://mlflow.org/docs/latest/index.html)  
- [scikit-optimize](https://scikit-optimize.github.io/)  
- [xgboost](https://xgboost.readthedocs.io/)  
- [scikit-posthocs](https://scikit-posthocs.readthedocs.io/)  
- [pingouin](https://pingouin-stats.org/)    
- [category-encoders](https://contrib.scikit-learn.org/category_encoders/)  
- [streamlit](https://streamlit.io/)  

### Setting up the Environment

Clone this repository and set up the environment with Pipenv:

```bash
git clone https://github.com/username/project-name
cd project-name
pipenv install
pipenv shell
```

If Pipenv is not installed, you can install it using pip:

```bash
pip install pipenv
```

This will create a virtual environment and install all required dependencies as specified in the `Pipfile.lock`.


## 🔄 Next Steps
1. Add an analysis set of pages to streamlit.
2. Develop a double model to predict a. Rent prices for municipality of Madrid b. Remaining cities in the province
3. Add additional characteristics like median income per district or neighborhood, characteristics from description, etc.


## 🤝 Contributions

Contributions are welcome. If you wish to improve the project, open a pull request or an issue.

## ✒️ Authors

Miguel López Virués - [GitHub Profile](https://github.com/MiguelLopezVirues)

## 📜 License

This project is licensed under the MIT License.