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
##### 1 Drop unwanted columns:Unwanted columns were dropped to focus on relevant features for modeling. The removed columns include:
##### Serial Number, Common Name (India Checklist), Scientific Name (India Checklist), Common Name (eBird 2018), Order, Family, Distribution Range Size (units of 10,000 sq. km.), Distribution Range Size CI (units of 10,000 sq. km.), Diet Composite, Assessed Primarily Based On, Waterbirds Composite and Raptors Composite.

##### 2 Column Renaming:
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

##### 3.Duplicate Value: Dataset doesn't contain any duplicate value

##### 4 Missing value handling:
- Filled numerical columns with 0.
- Filled categorical columns with mode of each column.

##### 5 Data Type Conversion
- Converted the following columns to binary (0/1):
-- analysed_long_term (col 4)
-- analysed_current (col 5)

waterbirds (col 16)

raptors (col 17)

scavengers (col 18)

Converted the following columns to categorical:

group (col 1)

iucn_status (col 2)

wlpa_schedule (col 3)

long_term_status (col 10)

current_status (col 11)

distribution_status (col 12)

status_of_conservation_concern (col 13)

migratory_status (col 14)

diet (col 15)

waterbirds (col 16)

raptors (col 17)

scavengers (col 18)


  
