# Capstone Project: Real Estate Transaction Analysis in Japan

Streamlit app link(Cloud hosted): https://japan-real-estate-price-prediction-app-2023.streamlit.app/

Dataset link: https://drive.google.com/drive/folders/13jdFIeTlVA9fCj06bkrgu9X9e6v5k5Zo?usp=sharing

Author: Aditi Namboodiripad

Date: 11/26/2023

Contact: chittooradi@gmail.com


## Project Overview

### Problem Area
The Capstone project aims to analyze real estate transaction data in Japan, covering the period from 2005 to 2019. This dataset was surveyed by the Ministry of Land, Infrastructure, Transport, and Tourism of Japan (MLIT). The primary goal is to gain insights into the trends and factors influencing real estate prices in Japan over this 15-year period. For now I will be dealing with Pre-owned condos,etc. real-estate type.

### Those Affected
The analysis of this dataset can benefit various stakeholders, including real estate investors, developers, city planners, and anyone interested in understanding the dynamics of the Japanese real estate market. By identifying trends and factors affecting property prices, this analysis can provide valuable information for making informed decisions in the real estate sector.

### Proposed Data Science Solution
This capstone will mainly focus on the prediction of Trade prices of real estate. The proposed data science solution involves the following key components:

1. Data Exploration: Exploring and understanding the dataset, including data cleaning, feature selection, and preprocessing.

2. Descriptive Analysis: Analyzing basic statistics, distributions, and trends in real estate transaction prices, regions, and more.

3. Time Analysis: Investigating how real estate prices have evolved over time, identifying yearly and quarterly trends.

4. Spatial Analysis: Examining prefecture level variations in property prices, identifying high-performing prefectures, and assessing whether there's a difference in property prices between Tokyo (the capital) and other areas.

5. Factors Affecting Prices: Investigating the factors influencing property prices, such as property type, proximity to transportation, building structure, land shape, and more.

6. Predictive Modeling: Developing predictive models to estimate future property prices based on historical data and identified factors.
   
Further for predictions different models can be used:

1.Regression Models like Linear regression,Decision Trees.

2.Gradient Boosting: XGBoost Regressor for improving predictive accuracy.

3.Evaluation Metrics: Mean Absolute Percentage Error (MAPE) or R2 to assess model performance.
 
### Impact of the Solution
The analysis of this real estate dataset can have several potential impacts:

- **Market Insights:** It can provide valuable insights into how the Japanese real estate market has evolved, helping stakeholders make informed investment decisions.
- **Investment Decisions:** Investors can use the predictive models to estimate future property prices and make data-driven investment decisions.
- **Regional Comparisons:** Understanding price variations between Tokyo and other prefectures areas can guide property buyers and sellers.

Japan saw its population peak in 2008 and is aging quickly. The old-age dependency ratiov was 47 in 2019. As aggregate housing supply exceeds housing demand, the national vacancy rate reached 13.6% for all housing types and 18.5% for rental housing in 2018. Wealthy individuals motivated by tax advantages supply small apartment units, but do not lower rents to fill vacant units because low-rent tenants will sit in the apartment for an extended period. At the same time, owners try to avoid renting to families because of low turnover.

5% improvement in predicting trade prices can contribute to more affordable housing options for buyers.Market efficiency, it might lead to a 10% increase in the overall effectiveness of property transactions.

### Dataset Description
The dataset consists of the following fields:

- **Type:** Real Estate Type (e.g., Residential Land, Agricultural Land, Condominiums).
- **Region:** Characteristics of surrounding areas (e.g., Residential Area, Commercial Area).
- **MunicipalityCode:** City code of Japan.
- **Prefecture:** Prefecture name of Japan.
- **Municipality:** City name.
- **DistrictName:** District name.
- **NearestStation:** Nearest station name.
- **TimeToNearestStation:** Time to the nearest station (in minutes).
- **TradePrice:** Transaction prices in Japanese Yen.
- **FloorPlan:** Property floor plan (e.g., 3LDK, 2DK).
- **Area:** Surveyed area in square meters.
- **UnitPrice:** Unit Land Price (Yen) per square meter.
- **PricePerTsubo:** Unit Land Price (Yen) per Tsubo.
- **Frontage:** Frontage in meters.
- **BuildingYear:** Construction year of the building.
- **PrewarBuilding:** Buildings built before 1945.
- **Structure:** Building structure (e.g., Steel frame reinforced concrete, Wooden).
- **Use:** Current property usage (e.g., House, Office, Factory).
- **Purpose:** Purpose of future use (e.g., House, Shop, Office).
- **Direction:** Frontage road direction.
- **Classification:** Frontage road classification (e.g., City Road, National Highway).
- **Breadth:** Frontage road breadth in meters.
- **CityPlanning:** Use districts designated by the City Planning Act.
- **CoverageRatio:** Maximum Building Coverage Ratio (%).
- **FloorAreaRatio:** Maximum Floor-area Ratio (%).
- **Period:** Time of transaction.
- **Year:** Time of transaction year.
- **Quarter:** Time of transaction year-quarter.
- **Renovation:** Renovation status.
- **Remarks:** Additional notes and remarks.

## Flowchart
1. **Data Collection:**
   - Retrieve the dataset 
   
2. **Data Preprocessing:**
   - Handle missing values.
   - Address data quality issues.
   - Perform feature engineering.
   
3. **Exploratory Data Analysis:**
   - Analyze distributions of variables.
   - Visualize patterns and correlations.
   - Formulate initial questions for further investigation.
4. **Baseline Modeling :**
   - Linear regression, random forest model, XGBoost(Regressor).
   - Evaluation of model performance using MAPE and R-squared.
   - Interpret model coefficients for insights.

5. **Advanced Modeling (Sprint 3):**
   - Cross validation
   - Fine-tune hyperparameters.
   - Advanced models
- Gradient Boosting Regressor:Try models like Gradient Boosting Regressor, which can capture complex relationships in the data.
- Random Forest Regressor: Experiment with Random Forest for regression (SVR) to capture non-linear patterns.

6. **Business Implications and Future Work:**
   - Discuss the practical implications of model performance.
   - Outline limitations and potential improvements.
   - Try other different advanced models.
   - Productizing work
   
 ## Repository Navigation Instructions 

 Folders:
 1. **Docs** : Sprint1, Sprint2, Sprint3 presenations.
 2. **Notebooks** :
    
    a.PartI_Initial_Dataset_merging_and_splitting.ipynb
    
    b.PartII__PreliminaryEDA_AdvancedEDA.ipynb
    
    c.PartIII_Basic_Modelling.ipynb
    
    d.PartIV_Advanced_Modelling.ipynb
    
    e.**Data** : All the dataset CSVs
    
3. **References** : Readme file with link to the original dataset from Kaggle.
4. **Streamlit** :
5. 
    a.Contains datasets to run the streamlit app.
   
    b.**Japan_app.py** is the app python file.
   
    c.**xgboost_model.pkl** is the model pickle file.
   
    d.It also contains requirements text file.
   
7. **readme.md** : Details about this project.
8. **packages.txt** : Required to support locales in cloud.
     
## Notebook Usage Instructions

**Execution Order**

To run this entire project download all the files in the **Notebooks** folder into one single folder and run each notebook in this order: 

1. PartI_Initial_Dataset_merging_and_splitting.ipynb
2. PartII__PreliminaryEDA_AdvancedEDA.ipynb
3. PartIII_Basic_Modelling.ipynb
4. PartIV_Advanced_Modelling.ipynb

The data files(CSVs) for each of these notebboks is present in the **'Data'** folder:
Part I: PartI_Initial_Dataset_merging_and_splitting.ipynb

* There are 47 csv files ranging from 01.csv to 47.csv
* These have been merged into a single dataset called Japan_dataset.csv and split into 5 other datasets based on the Real Estate type ,namely 'Agricultural Land.csv', 'Forest Land.csv', 'Residential Land(Land and Building).csv', 'Residential Land(Land Only).csv', 'Pre-owned Condominiums, etc..csv' (Here this project has dealt with 'Pre-owned Condominiums, etc..csv')

Part II: PartII_PreliminaryEDA_AdvancedEDA.ipynb

* Load the dataset 'Pre-owned Condominiums, etc..csv'.
* Basic and advanced exploratory data analysis (EDA) has been done to understand the dataset's structure, to visualize key features, to check for missing values, to explore basic statistics,to identify outliers and potential correlations.
* Further for modelling the the categorical values has been converted to dummies(one hot encoding) and a dummy variable dataset has been created called 'dummies.csv' 

Part III: PartIII_Basic_Modelling.ipynb

* Load the dataset 'dummies.csv'
* Vanilla modelling of Linear regression, Random Forest and XGBoost Regressor has been performed
* The models has been evaluated using standard metrics Mean Absolute Percentage Error(MAPE) and R2.
  
Part IV: PartIV_Advanced_Modelling.ipynb

* Load the dataset 'dummies.csv'
* Random Forest and XGBoost Regressor has been performed with cross-validation and hyperparameter tuning to improve model performance.
* The models has been evaluated using standard metrics Mean Absolute Percentage Error(MAPE) and R2.

Streamlit

* To run locally run Japan_app.py file and change the paths of the datasets and pickle file accordingly.


## Acknowledgements and Source
**Source:** https://www.kaggle.com/datasets/nishiodens/japan-real-estate-transaction-prices

This dataset is a slightly cleaned-up version of the one published by MLIT.
