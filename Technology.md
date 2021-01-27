<h1 align = "center"> X ROLE </h1>

# Technologies Used

## Data Cleaning and Analysis
Pandas was used to clean the data and perform an exploratory analysis. We converted the csv files for the accepted and rejected data to dataframes using Pandas. Further analysis will be completed using Python and Jupyter Notebook. 

## Machine Learning
SciKitLearn is the ML library we'll be using to create a classifier. Our training and testing setup uses the merged accepted and rejected loan datasets after selecting the relevant columns. Using a regression model, our initial train/test run produced results at an accuracy of 88.5%. F1 scores were 93% for rejected and 66% for accepted. Further analysis will be required to determine how to improve the predictions. This will be completed in the coming week.

## Next Steps
Our next steps will be to employ NLP to incorporate the loan titles in our decision making, as WokeRUs Believes that this will help improve predictions. Once we are satisfied with the prediction of accepting and rejecting loans, further analysis will be done for accepted loan data to be able to predict an interest rate for the loan. 
