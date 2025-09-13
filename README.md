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
- RandomForest, DecisionTree and XGBoost – For building and evaluating machine learning models to classify bird species into conservation concern levels.

## Data Cleaning/Preprocessing
##### 1 *Drop unwanted columns:* Unwanted columns were dropped to focus on relevant features for modeling. The removed columns include:
##### Serial Number, Common Name (India Checklist), Scientific Name (India Checklist), Common Name (eBird 2018), Order, Family, Distribution Range Size (units of 10,000 sq. km.), Distribution Range Size CI (units of 10,000 sq. km.), Diet Composite, Assessed Primarily Based On, Waterbirds Composite and Raptors Composite.

<img width="614" height="274" alt="image" src="https://github.com/user-attachments/assets/cee22e37-6459-4c70-bc5f-f6619e16c4ad" />

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

##### 3. *Sorting Dataset:* we sort the birds_name 

<img width="507" height="253" alt="image" src="https://github.com/user-attachments/assets/b5a5b10c-ba87-41a7-986f-c4ed47679dfb" />

##### 4. *Cleaning Birds Name:* To ensure consistency across datasets, bird names were cleaned and standardized by:
- Removing extra spaces
- Converting all names to lowercase
- Replacing hyphens with spaces
- Ensuring consistent formatting across birds_df and birds_name

  <img width="789" height="105" alt="image" src="https://github.com/user-attachments/assets/262a5050-fca0-4bcf-b7a8-43ac90148138" />


###### Output : <img width="243" height="209" alt="image" src="https://github.com/user-attachments/assets/d71d9936-bc77-4f89-b80e-81a051c6fe6f" />

<img width="1020" height="89" alt="image" src="https://github.com/user-attachments/assets/d8166e5f-480a-4847-a69f-9992f489e7a1" />

##### 5 *Duplicate Value:* Dataset doesn't contain any duplicate value

##### 6 *Missing value handling:*
- Filled numerical columns with 0.
  
<img width="350" height="247" alt="image" src="https://github.com/user-attachments/assets/f69a4763-276e-403c-8a51-ced90f9433fe" />

- Filled categorical columns with mode of each column.
<img width="503" height="204" alt="image" src="https://github.com/user-attachments/assets/3127fb82-8d5e-4684-aff1-eea10dbdde37" />

##### 7 *Data Type Conversion:*
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

## EDA (Exploratory Data Analysis)
##### Perfomed EDA to visualize the dataset

- Top 10 Bird Group
<img width="846" height="444" alt="image" src="https://github.com/user-attachments/assets/3f749a32-8f31-45e6-ad4f-2c185efd55bc" />

###### Old World Flycatchers have the highest proportion and Watefowl, Tree-Babblers, Scimitar-Babblers and Allies have the lowest proportion

- Bird Endemicity Type Distribution by Conservation Concern
<img width="555" height="295" alt="image" src="https://github.com/user-attachments/assets/74e24f10-658c-4944-8e1a-10a641bd9e96" />
  
###### Over half of the species (52%) fall into the Unknown endemicity category.
###### Among known categories, Resident-Non-Endemics are most common.
###### Across groups, most species are in Low or Moderate conservation concern, while relatively few are categorized as High concern.

- IUCN Status vs WLPA Schedule
<img width="856" height="524" alt="image" src="https://github.com/user-attachments/assets/c48a170e-618e-4f89-b23d-0faca3e11bef" />

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
- Decision Tree → ~91% accuracy on validation.

<img width="398" height="200" alt="image" src="https://github.com/user-attachments/assets/d2858779-7943-43ba-b23b-13239585ecc6" />

<img width="437" height="292" alt="image" src="https://github.com/user-attachments/assets/6ebb7553-72d2-4e2c-9691-32d15868ef2b" />


- Random Forest → ~95% accuracy (better/stabler).
<img width="416" height="289" alt="image" src="https://github.com/user-attachments/assets/d49ebc6e-7aad-4bf7-93c4-b666d7a39ea1" />

- XGBoost → ~97% accuracy.
<img width="427" height="291" alt="image" src="https://github.com/user-attachments/assets/821d491c-f351-4470-92a9-34a5706698c4" />


##### Prediction
<img width="565" height="356" alt="image" src="https://github.com/user-attachments/assets/3a9b3e2b-b97f-4643-8503-f1739c4ed8ce" />

<img width="699" height="378" alt="image" src="https://github.com/user-attachments/assets/33859f54-5e58-4704-9735-cd5e752a6286" />

<img width="475" height="33" alt="image" src="https://github.com/user-attachments/assets/786dec5c-3d59-47a4-a183-baa63522c29b" />

##### Interpretation:
- High accuracies indicate the model captures strong signals from population trends and ecological features.
- Still validate with confusion matrix per-class metrics to ensure High concern species are not missed.

  

## Dashboard 
###### A Streamlit dashboard was developed for:
- Predicting conservation concern based on user inputs.
- Exploring interactive visualizations such as IUCN Status distribution, WLPA Schedule Distribution, Migratory Status Distribution, Current Status, Long-term Trend Vs Current Annual Change, Endemic Vs Non-endemic Species etc.
- Downloading summary tables and CSVs.


<img width="1653" height="766" alt="image" src="https://github.com/user-attachments/assets/57d03f40-c57d-4838-aa1e-d551b0ca4fd6" />

<img width="826" height="853" alt="image" src="https://github.com/user-attachments/assets/e5ac50be-73b0-43ca-9fb5-e643f169598c" />

<img width="369" height="791" alt="image" src="https://github.com/user-attachments/assets/0fe65a44-525c-4644-9ffc-044543d81781" />



###### The dataset contains bird information and bird names categorized state-wise. The Streamlit app code is in birds1.py, while the visualization and machine learning logic are in the main file.






  
