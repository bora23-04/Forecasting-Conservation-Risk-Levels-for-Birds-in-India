# Feather Fall: Forecasting Conservation Risk Levels for Birds in India
## Problem Statement 
##### India is home to over 1,300 bird species, many of which are increasingly threatened by habitat loss, climate change, and human activity. With conservation resources limited, it's critical to prioritize efforts toward species that are most at risk. However, determining which species need immediate attention remains a significant challenge.
##### This project aims to build a machine learning model that classifies Indian bird species into three conservation concern levels — Low, Moderate, or High — using ecological traits, population trends, migratory behavior, diet, and other biological indicators. By leveraging data-driven predictions, this tool supports early identification of vulnerable species, enabling conservationists and policymakers to take targeted, proactive action. Through this approach, we seek to enhance the effectiveness of conservation planning and contribute to preserving India's avian biodiversity.

## Goal 
##### To support effective bird conservation in India by identifying species at higher conservation risk through predictive modeling, enabling early intervention and better resource allocation.

## Project Objective 
##### To build a machine learning model that classifies Indian bird species into conservation concern levels (Low, Moderate, High) using ecological features such as population trends, diet type, migratory behavior, and distribution range. This model will help prioritize species and regions for focused conservation action

## Data Source 
##### Dataset collected from the State of India’s Birds website via their API, containing ecological traits, population trends, migratory patterns, and habitat details for over 1,300 Indian bird species. This data forms the basis for building and training the conservation concern classification model.
- Pandas & NumPy – For data cleaning, preprocessing, and manipulation.
- Seaborn & Matplotlib – For static data visualization and exploratory data analysis (EDA).
- Plotly – For interactive and dynamic visualizations.
- Streamlit – To build an interactive dashboard for prediction and data exploration.
- RandomForest & DecisionTree – For building and evaluating machine learning models to classify bird species into conservation concern levels.

## Data Cleaning/Preprocessing
##### 1 *Drop unwanted columns:* Unwanted columns were dropped to focus on relevant features for modeling. The removed columns include:
##### Serial Number, Common Name (India Checklist), Scientific Name (India Checklist), Common Name (eBird 2018), Order, Family, Distribution Range Size (units of 10,000 sq. km.), Distribution Range Size CI (units of 10,000 sq. km.), Diet Composite, Assessed Primarily Based On, Waterbirds Composite and Raptors Composite.

##### 2 *Column Renaming:*
##### For consistency and easier handling in the machine learning pipeline, several columns were renamed as follows:

-  `'Common Name (eBird 2019)'` → `bird_name`
-  `'Group'` → `group`
-  `'IUCN Status'` → `iucn_status`
-  `'WLPA Schedule'` → `wlpa_schedule`
-  `'Analysed Long-term'` → `analysed_long_term`
-  `'Analysed Current'` → `analysed_current`
-  `'Long-term Trend (%)'` → `long_term_trend`
-  `'Long-term Trend CI (%)'` → `long_term_trend_ci`
-  `'Current Annual Change (%)'` → `current_annual_change`
-  `'Current Annual Change CI (%)'` → `current_annual_change_ci`
-  `'Long-term Status'` → `long_term_status`
-  `'Current Status'` → `current_status`
-  `'Distribution Status'` → `distribution_status`
-  `'Status of Conservation Concern'` → `status_of_conservation_concern`
-  `'Migratory Status'` → `migratory_status`
-  `'Diet'` → `diet`
-  `'Waterbirds'` → `waterbirds`
-  `'Raptors'` → `raptors`
-  `'Scavengers'` → `scavengers`
- `'Habitat Composite'` → `habitat_type`
-  `'Endemicity Composite'` → `endemicity_type`

##### 3 *Duplicate Value:* Dataset doesn't contain any duplicate value

##### 4 *Missing value handling:*
- Filled numerical columns with 0.
- Filled categorical columns with mode of each column.

##### 5 *Data Type Conversion:*
###### Converted the following columns to binary (0/1):
- analysed_long_term
-  analysed_current
- waterbirds 
- raptors
- scavengers 
###### Converted the following columns to categorical:
- group 
- iucn_status 
- wlpa_schedule 
- long_term_status
- current_status 
- distribution_status 
- status_of_conservation_concern
- migratory_status 
- diet 
- waterbirds
- raptors 
- scavengers

##### 6 *Data Cleaning & Statewise Mapping:*
- Standardized bird names in both master dataset and statewise dataset (lowercase, removed extra spaces, replaced hyphens with spaces).
- Removed unwanted whitespace from column names.
- Used fuzzy matching (fuzz.token_sort_ratio) to align statewise bird names with the master list, creating a correction dictionary for name mapping.
- Corrected mismatched names and built statewise unique bird sets.
- Added binary presence columns for each state in the master dataset (1 = present, 0 = absent).

## EDA (Exploratory Data Analysis)
##### Perfomed EDA to visualize the dataset
- Population Trend Category vs Conservation Concern
<img width="1403" height="423" alt="image" src="https://github.com/user-attachments/assets/167c26f6-e6f6-4ad5-9ff7-aa67379bf0d7" />

###### High conservation concern appears mostly for stable populations and rarely for decreasing populations, which could suggest that "concern" status isn’t solely based on population trend.

- IUCN Status vs WLPA Schedule
<img width="1030" height="634" alt="image" src="https://github.com/user-attachments/assets/323d128a-09b8-4e14-910a-7c351b5c2d1c" />

###### Most species regardless of migratory status fall under Least Concern, with Resident species making up the majority in all categories, including the most threatened ones.

- Distribution of long term trends
<img width="1133" height="474" alt="image" src="https://github.com/user-attachments/assets/0d7b323b-91a4-4248-9653-bd8506e105eb" />

###### Most bird species have stable populations, but declining trends are more common than strong increases, which is a concern for conservation.

- Diet Type Distribution Across Migratory Status
<img width="985" height="546" alt="image" src="https://github.com/user-attachments/assets/52fd1aec-fafe-4852-ae79-0341c98796c3" />

###### Regardless of migratory status, Invertebrate feeding is the most common diet type, but Resident species have a much more diverse diet compared to migratory species.


###### conclusion from EDA : The graphs collectively show that population decline, migratory behavior, specific bird groups (waterbirds, raptors), and certain geographic states are strongly associated with higher conservation concern levels — indicating where proactive conservation action should be prioritized.

## Machine Learning Models
##### 1. *Dataset Split* 
- Split into train (60%), validation (20%), and test (20%) sets.
<img width="572" height="164" alt="image" src="https://github.com/user-attachments/assets/fc434515-36d2-42fd-8b2f-33ab0db5000a" />

##### 2. *Encoding & Scaling* 
- Target encoded using LabelEncoder (Low, Moderate, High).
<img width="433" height="122" alt="image" src="https://github.com/user-attachments/assets/5944325e-efe8-4c07-8142-457b6ba1c1e8" />

- Scaled numeric features using MinMaxScaler.
<img width="505" height="137" alt="image" src="https://github.com/user-attachments/assets/4b6b9053-76f6-4ce5-a655-303434fe9960" />

- One-hot encoded categorical features (OneHotEncoder, handle_unknown='ignore').
<img width="751" height="288" alt="image" src="https://github.com/user-attachments/assets/ab5a5dbe-23c5-4f70-962c-ef9361a29918" />

##### 3. *Model Training*
- Decision Tree → ~94% accuracy on validation.

  <img width="420" height="229" alt="image" src="https://github.com/user-attachments/assets/59940a1b-a2fb-4cd7-815e-cc5942169bad" />


  <img width="443" height="316" alt="image" src="https://github.com/user-attachments/assets/2dd81e44-cd87-4bd5-af60-54101c0488e6" />

- Random Forest → ~95% accuracy (better/stabler).
<img width="434" height="224" alt="image" src="https://github.com/user-attachments/assets/610384e3-1ddd-4863-a1c3-b011c0590583" />


##### Prediction
<img width="639" height="558" alt="image" src="https://github.com/user-attachments/assets/d7f8d544-1bc6-4d10-8aa5-b8d87d475da2" />


##### Interpretation:
- High accuracies indicate the model captures strong signals from population trends and ecological features.
- Still validate with confusion matrix per-class metrics to ensure High concern species are not missed.

  

## Dashboard 
###### A Streamlit dashboard was developed for:
- Predicting conservation concern based on user inputs.
- Exploring interactive visualizations such as IUCN Status split, Migratory Status split, Diet vs Bird Type, and Top Threatened States.
- Downloading summary tables and CSVs.


<img width="1036" height="441" alt="image" src="https://github.com/user-attachments/assets/608913bb-16ca-47d9-913d-f9c6fb9a8bee" />


<img width="1869" height="700" alt="image" src="https://github.com/user-attachments/assets/46bb812b-3c00-4371-bf41-40361d681404" />


<img width="1269" height="277" alt="image" src="https://github.com/user-attachments/assets/d596a515-48bb-45cc-ab63-d9b5c674ed04" />


<img width="823" height="796" alt="image" src="https://github.com/user-attachments/assets/0d58aa98-8fdb-4322-ae0f-e333c9ab9fde" />




###### The dataset contains bird information and bird names categorized state-wise. The Streamlit app code is in birds.py, while the visualization and machine learning logic are in the main file.






  
