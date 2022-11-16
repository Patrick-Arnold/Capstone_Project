![](https://i.imgur.com/2HnC3w7.png)

This project was completed as part of the Data Science curriculum at the Flatiron School. I am not affiliated with any listed organizations.


## Objective
The PRAMS (Pregnancy Risk Assessment Monitoring System) network is a division of the Center for Disease Control and Prevention. They have collected data on over 80% of the births that occur in the United States in order to better understand the risks to mothers and infants during pregnancy and childbirth. PRAMS has asked me to analyze US natality data in order to predict whether infants will need emergency medical intervention at birth, and describe what could be done to improve those health outcomes.

![](https://i.imgur.com/7n16VAk.png)

## Methods and Technologies Used
* Machine Learning
* Data Visualization
* Predictive Modeling
* Python

## Data Understanding
Data Source: https://www.nber.org/research/data/vital-statistics-natality-birth-data 
For data usage restrictions, please visit [this page](https://www.cdc.gov/nchs/data_access/restrictions.htm). 

Due to the importance of maintaining the privacy of the mothers and children whose data was collected in the dataset, it was impossible to access detailed information about their true health outcomes. Therefore, it is necessary to use the APGAR score given 5 minutes after birth as a metric that can approximate the overall health of a child shortly after birth. The [APGAR score](https://www.hopkinsallchildrens.org/Patients-Families/Health-Library/HealthDocNew/What-Is-the-Apgar-Score) is a simple metric that scores five categories between 0 and 2. A higher score generally means that the newborn is more likely to be healthy, and vice-versa. Traditionally, a score of 6 or lower is considered "unhealthy" and medical assistance may be needed to protect the child's life. The target for this analysis will be predicting whether a newborn will have an unhealthy (0-6) APGAR score.

![](https://www.abclawcenters.com/wp-content/uploads/2016/06/Apgar-Scoring-System-Diagnosing-Birth-Injuries.jpg)
Source: ABC Law Centers

The dataset contained around 3.7 million rows, representing more than 80% of all births that occured in the USA during the 2019 survey! Of those entries, approximately 2% were labelled as having a low APGAR score. This is a fairly sizeable class imbalance, but thankfully the data's size opens up some options for potentially dealing with it. I chose to artificially balance the training data by randomly sampling an equal number of low and high APGAR score cases to improve model performance, but the sampling method used is definitely a factor that could be tweaked in future analysis. The Test data contained the same target distribution as the original dataset to better reflect how the model would need to predict in practice, sharing no duplicates with the training set. Due to hardware constraints, I limited my analysis to 20,000 total rows of data.

## Data Processing
The original dataset contained over 200 different features, many of which were not appropriate for the scope of this analysis. A full list of columns can be found in the data report located in this directory, and the 'functions.py' file contains detailed steps on how I initially cleaned the data. In general, I removed columns based on the following criteria:
* They are storing metadata about the collection of the dataset
* They were pre-processed for a specific purpose outside the scope of this analysis
* They are slight variations of existing columns which are more applicable to this project
* They represent events that happen after birth has already occurred

Additionally, many of the features used different labels to represent that an entry was missing. I examined each feature and replaced the missing values with a consistent label for later usage. To limit the eventual width of the data after one-hot encoding the categorical variables, I also binned some variables into broader categories at this stage.

After checking for multicolinearity, several features were dropped that had a high (> 0.7) correlation with other features.

In my initial exploratory data analysis, I found that rows containing some missing values tended to have a higher liklihood of low APGAR scores. I did not want to lose any potentially explanatory information, so I decided to impute the missing values based on the values of the rest of the dataset. This could be adjusted in future analysis to provide a more orbust recommendation. For numerical features, I imputed missing entries with the median of the column and then applied a [MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html). For categorical features, I imputed missing entries with the most frequent value of the column and then [one-hot encoded](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html) them.

## Featured Visualizations
For more, see the Main Notebook and presentation.

Health Conditions:
![](https://i.imgur.com/vfCnAAk.png)

Prenatal Care's Association with APGAR Score:
![](https://i.imgur.com/l1qoMOV.png)

## Modeling
The primary evaluation metric used for the modeling process was recall score. Recall is sensitive to the number of positive cases identified (in this case, emergencies) so it is appropriate for a case where the stakes are so high. Depending on how the model would be used by healthcare professionals, it may also be worthwhile to optimize the model for overall predictive performance in future analysis. For a more complete glimpse at the modeling process, see the Gridsearch notebook.

The first model tried was a logistic regression with default parameters. It scored a recall score of 57.6% on the test data, which is quite good for how rare the target is in the test distribution. It tended to overpredict emergencies, which might be good considering the potential severity of the classification but also might overburden medical professionals.

![](https://i.imgur.com/UswcPi5.png)

The finalized model was an XGBoost model with parameters optimized for locating the most emergencies. It produced a recall score of 65% on the test data. While it was able to capture more of the target than the others models, it also tended to overpredict a low APGAR score. The prediction threshold may need to be adjusted higher to filter out for cases where the model is more certain of emergencies, but of course the final say should still be in the hands of medical professionals.

![](https://i.imgur.com/rDqjdy6.png)

## Conclusions
During my analysis, I noted some features that were important to the model that the PRAMS organization could look into when researching how to improve infant health outcomes. I found one consistent pattern among indicators of socioeconomic status such as race, education, and access to prenatal care: lower income mothers tended to have significantly more newborns with low APGAR scores at birth. This might suggest that an aid program targetting this care gap between low and high income mothers would be fruitful in improving infant health outcomes.

When deploying the model, its predictions could be used as an alert system to notify healthcare professionals when a mother is likely to need additional medical support during and after birth. It might also be used in concordance with physician expertise to make recommendations to mothers about potential interventions that would improve the health of their newborns.

## Repository Navigation
The Gridsearch notebook contains records of the model optimization process, while the Main Notebook contains the bulk of the project's exploration and analysis. Functions.py contains a function that goes through the process of cleaning the dataset without cluttering the main notebook. The Natal User Guide is a document provided by the data source that describes an overview of the dataset. The presentation pdf is an image of the slides used during my presentation.
```                              
├── .gitignore
├── Gridsearch.ipynb
├── Main_Notebook.ipynb
├── README.md
├── functions.py
├── nataluserguide2019.pdf
└── presentation.pdf
```                              

## Contact
* LinkedIn: https://www.linkedin.com/in/patrick-t-arnold/ 
* Email: ptarnold10@gmail.com