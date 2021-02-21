<p align = "center">
<img src = "https://github.com/JoseCalucag/WokeRUs/blob/main/resources/WokeRUsLogo.png" width='500' height='100'>
 </p>

LendingClub is a company that enables people looking to apply for unsecured personal loans by supplying details about themselves and the loans that they would like to request (between 1K-40K). On the basis of the borrower’s credit score, credit history, employment history, desired loan amount and the borrower’s debt-to-income ratio, LendingClub determined whether the borrower was creditworthy and allowed the loan or not. The team at WokeRUs looked to investigate if it was possible to predict the approval of any loan based upon features listed.

## Presentation Deck Link

https://docs.google.com/presentation/d/1wxTUs8_m18508qBnELvGLtDMG5xyXyQ7KO01LL08q00/edit#slide=id.gba2577a18d_0_158

## Project Outline:

The following is the project outline, with more details on each of the steps discussed further down in the different sections:

- Dataset was retrieved from Kaggle for accepted and rejected loans.
- Data was first cleaned up to make sure the same required columns for accepted and rejected data were present in a single file.
- The two datasets were merged with only the required columns included into a consolidated dataset.
- Machine learning (Decision Tree with ADABOOT) was used to predict if a loan will be accepted or rejected based on features.
- Data for accepted loans was looked into with more detail to determine what columns are correlated with interest rates.
- Data was cleaned up with all unnecessary columns removed. (Leaving us with 96 of the 151 columns)

Resources:
- Also Please refer our requirements.txt file for libraries and installations.
- Data Extracted kaggle dataset - [Lending Club loan data](https://www.kaggle.com/wordsforthewise/lending-club)
- Data dictionary kaggle - [Dictionary](https://www.kaggle.com/jonchan2003/lending-club-data-dictionary)
- VS Code v1.52.1
- Jupyter Notebooks v6.0.3
- Python v3.7.9
- GitHub
- Zoom Client for Meetings v5.4.9

## Dataset Exploratory Analysis

- The dataset was available to us in a.csv file, and since only two tables were present an ERD was not necessary
- The datasets were large and importing the datasets into our repository was fairly straightforward and less daunting than expected.
- Since our datasets were classified into two main categories one being accepted for loan and the other rejection, we did analyze the columns (a run through) to find relational contents of both datasets.
- There are about 27 million data points on the rejected data, and 2 million data points with the accepted datasets. (highly skewed or biased towards rejections of loan applications)
- The features were way too detailed when looking at the accepted dataset (151 features) when compared to the rejected dataset (9 features)
- After discussion data points or features from applicants that were rejected, were deemed important and considered for our initial learning model.
- The data contained many missing values in regards to the rejected dataset, this amounted to 18 million data points being dropped. (slightly reducing the imbalance)
- In further exploratory analysis, cleaning data was carried out where most of our features were having characters paired with numerics.
- After a thorough run with data preprocessing and cleaning, we have achieved criteria that seem to play a vital role in deciding or rejecting a loan application.
- This dataset will be tied into our analysis further. (maybe consider other valuable features and also predict an individual's chance of securing a loan)

## Database

- Since the data we possess do not have any relational features that we could use or create an ERD, the datasets we have were merged into one big consolidated dataset.
- Since there is no schema, we collectively decided to use MongoDB as this was the easiest way to store our data.
- We Decided to sample our large dataset, 5% of the raw data, was sampled to stay within the limits of our allocated space and memory usage on the cloud (MongoDB Atlas)
- Hence, our main raw or original dataset is still available locally to ensure we are using our resources to its maximum potential. (All original dataset is available in kaggle)

# Machine Learning for Lending Prediction

The project implements Machine Learning in two progressive stages:

## Stage 1: Binary Classification

The first Machine Learning Algorithm trains a binary classifier to predict if the applicant should be accepted or rejected.
The following algorithm was selected mainly of two key elements after trial with various algorithms:

1. Class imbalance correction
2. optimizing number of selectors in our algorithm
3. iterate over different models and sampling.
4. Decision tree with SMOTE method bringing an accuracy of classification at 94.3%.

<p align = "center">
<img src = "https://github.com/JoseCalucag/WokeRUs/blob/main/resources/smote_ml.png" width = "500" height = "300">
 </p>

## Stage 2: Interest Prediction

The second Machine Learning Algorithm trains a regression model to predict the interest rate that should be provided to an accepted loan borrower.
The following key takeaways bought about a model with r2 score of 0.98 and mean square error of 1.00:

1. group by target variable
2. Ridge and Lasso regression
3. optimize alpha values
4. feature selection

<p align = "center">
<img src = "https://github.com/JoseCalucag/WokeRUs/blob/main/resources/regression.png" width = "500" height = "300">
 </p>

## Web App (Flask -screenshots)

<p align = "center">
<img src = "https://github.com/JoseCalucag/WokeRUs/blob/main/resources/main_page.png" width = "500" height = "300">
 </p>

 <p align = "center">
<img src = "https://github.com/JoseCalucag/WokeRUs/blob/main/resources/reject_main.png" width = "500" height = "300">
 </p>

 ## Stage 2: Interest Prediction

 <p align = "center">
<img src = "https://github.com/JoseCalucag/WokeRUs/blob/main/resources/int_predict.png" width = "500" height = "300">
 </p>

## Conclusion & Recommendations

1. As a team we would love to find more updated data as this one only goes to 2018.
2. Further use NLP or a different method to try and classify the rejected dataset taking into consideration the feature Loan Titles.
3. There was a lot learnt, practiced and implemented during this collaboration.


 <p align = "center">
<img src = "https://github.com/JoseCalucag/WokeRUs/blob/main/resources/images.jpeg" width = "500" height = "300">
 </p>