### Roles and responsibilities 
As part of the Woke-R_Us team, I took ownership of building and deploying a machine learning code to accomplish our classification goals to approve loan worthy customers and build on the classification model to deliver another regression model to predict an interest rate for the customer. 
To accomplish the above objective the following was completed:
 - Import multiple datasets as dataframes and analyse the raw input data
 - Determine independent and dependent features 
 - Clean the dataset to remove null values and change datatypes
 - Visualize independent features against the dependent variable to determine correlations and get insights into the data
 - Plot correlation matrix to determine collinearity between the independent features
 - Preprocess and bin the independent features by changing categorical values to numerical values and normalize the numerical dataset
 - Perform feature scaling and resampling of data to address class imbalance
 - Run multiple machine learning algorithms to determine accuracy and performance metrics
 - Optimize machine learning models by feature scaling and feature selection to achieve better accuracy and f1 values and as well as reduce the error for the regression models. 

In addition to the role above, I also supported the database and webpage deployment roles by helping provide clean data for storage and future retrieval. I also helped by providing the flask app with the pickle model file to run the prediction model that predicts loan approval status and potential interest rates based on customer input. 

#### Challenge
The biggest challenge in the project was the large data size that was not conducive to multiple reruns. Also, the data set has 151 features will most of them uncorrelated with each other which made the feature selection a challenge since the number of features needed to be optimized to present the customer who would input the data a pleasant experience. These challenges were overcome by brainstorming with teammates on the applicability of the features and which features provide the most predictive value. 

#### Team Organization
The team primarily communicated via Slack Google Meets to collaborate on their roles. 
The team faced challenges in merging git branches and a few code conflicts. This challenge was overcome by following a merge protocol and working in our respective branches on specific aspects of the project and not using `git add .` for all `push` procedures. 
One of the strengths of the team was that all the members were proficient in not only their roles but also the technical details of their teammates. This helped immensely in bringing the different parts of the project together smoothly. 

#### Project Summary 
The project analyses historical lending data to determine the most important parameters that are needed to be accepted for a loan and their influence on final interest rates. The project successfully deals with both categorical and numerical data of both quantitative and qualitative nature to present an accurate model with a high degree of precision and recall. 

