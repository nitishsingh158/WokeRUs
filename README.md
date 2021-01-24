<h1 align = "center"> Circle Role </h1>

## Resources

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

<p align = "center">
<img src = "https://github.com/JoseCalucag/WokeRUs/blob/CircleRole/resources/database.png" width = "700" height = "300">
 </p>


## Database Setup, working Branch and Communication

- Our search for a more refined or clean data was not successful, and the lending club dataset being the most comprehensive.
- The dataset was uploaded into GitHub as a large file transfer.
- Using the data uploaded on to GitHub, data was then wrangled for optimizing our dataset to suit our needs and the initial machine learning algorithm.
- 4 branches were initialized and setup on Github to ensure that the database and contents do not be overwritten (just because the sheer size)
- Main communication is through zoom client for meetings software and slack for progress tracking and deliverables time line.
