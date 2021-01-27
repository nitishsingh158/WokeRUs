<h1 align = "center"> </h1>

<p align = "center">
<img src = "https://theme.zdassets.com/theme_assets/680652/3abc1fe11ed0a385b1298f0a1e44a7d7d5f78fc1.png" width='500' height='100'>
 </p>

LendingClub is a company that enables people looking to apply for unsecured personal loans by supplying details about themselves and the loans that they would like to request (between 1K-40K). On the basis of the borrower’s credit score, credit history, employment history, desired loan amount and the borrower’s debt-to-income ratio, LendingClub determined whether the borrower was creditworthy and allowed the loan or not. The team at WokeRUs looked to investigate if it was possible to predict the approval of any loan based upon features listed. This was explored in the various branches on the repository as follows:

* X Role <br>
Lists the technologies that were used in the project and how they were implemented.
<br>

* Circle Role <br>
Explores the process of how the database was created before modelling.
<br>

* Triangle Role <br>
Investigates the data by running it through a machine learning model.
main

CircleRole
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

<p align = "center">
<img src = "https://github.com/JoseCalucag/WokeRUs/blob/CircleRole/resources/database.png" width = "700" height = "300">
 </p>


## Database Setup, working Branch and Communication

- Our search for a more refined or clean data was not successful, and the lending club dataset being the most comprehensive.
- The dataset was uploaded into GitHub as a large file transfer.
- Using the data uploaded on to GitHub, data was then wrangled for optimizing our dataset to suit our needs and the initial machine learning algorithm.
- 4 branches were initialized and setup on Github to ensure that the database and contents do not be overwritten (just because the sheer size)
- Main communication is through zoom client for meetings software and slack for progress tracking and deliverables time line.
=======