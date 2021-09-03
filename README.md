# Classification project

The objective of this project was to is to build a model that will provide insight into why some bank customers accept credit card offers, as well as answer additional questions by top management related to the matter.

In ordert o to this, I used agile project planning in Github and made use of SQL, Python and Tableau. 

![Hier sollte ein Bild zu sehen sein](https://st2.depositphotos.com/2704315/7774/v/600/depositphotos_77740328-stock-illustration-hand-holding-credit-card-vector.jpg)


## About the project

For the project we have data from a marketing study with 18.000 current bank customers. We want to understand the demographics and other characteristics of its customers that accept a credit card offer and that do not accept a credit card. . 

The goal of the binary classification project is to analyse the characteristics of the bank customers and to train a model to predict if a bank customer accept or reject a credit card offer.

## Dataset 
For the project we have data from a marketing study with 18.000 current bank customers with the following columns:  

|               Column |                                                                          Information  |
|---------------------:|--------------------------------------------------------------------------------------:|
|      customer_number |                                        A sequential number assigned to the customers. |
|       offer_accepted |                               Did the customer accept (Yes) or reject (No) the offer. |
|               reward |                                      The type of reward program offered for the card. |
|          mailer_type |                                                                   Letter or postcard. |
|         income_level |                                                                  Low, Medium or High. |
|   bank_accounts_open |                           How many non-credit-card accounts are held by the customer. |
| overdraft_protection | Does the customer have overdraft protection on their checking account(s) (Yes or No). |
|        credit_rating |                                                                  Low, Medium or High. |
|    credit_cards_held |                                          The number of credit cards held at the bank. |
|          homes_owned |                                            The number of homes owned by the customer. |
|       household_size |                                                  Number of individuals in the family. |
|        own_your_home |                                        Does the customer own their home? (Yes or No). |
|      average_balance |            Average account balance (across all accounts over time). Q1, Q2, Q3 and Q4 |
|        q1-q4 balance |                                     Average balance for each quarter in the last year |



## Workflow


1. **Exploring the data in SQL**
    - Files: Solutions_SQL- Classification.ipynb / Questions_SQL - Classification.md /
    - Write queries to extract demographics and other characteristics of bank customers

  
2.  **Logistic regression in Python** 
    - Files: Solutions_Python - Classification.ipynb / helper.py / Questions_Python - Classification.md
    - EDA
    - Data processing, feature engineering
    - Model evaluation
    - Overview - model results

  
3. **Analyse and visualize the data in Tableau** 
    - Files: Solutions_Tableau- Classification.ipynb / Tableau.twb / Questions_Tableau- Classification.md
    - Extract demographics and other characteristics of bank customers and visualize them 


## Conclusions
Note: For futher details, please refer to the related files


1. **Exploring the data in SQL**
- Properties: Credit rating medium or high, Credit cards held 2 or less, Owns their own home, Household size 3 or more
- There are only 167 customers with the following properties who accepted the offer. So I would give the hint, that this customers are under 1% of all customers and that is worth addressing this customer group.

2.  **Logistic regression in Python** 
- Logistic Regression with changed class weights fits best for this dataset. Highest Yes recall: 0.69.  
- Next step to evaluate this model: Cut the variables which do not improve the prediction and improve the weight/balance
- For the next marketing study I would recommend to change the questions which have no relationship to the target variable (Like shown in point 5.2.), target people who live in a household of the size 3 or 4, and to build bins (For example house hold size 5-9) 


3. **Analyse and vizualize the data in Tableau** 
- There is a huge jump in average balance from Q1 to Q2 for households with size 8.
- The jump is caused by the fact that only one out of 18.000 customers has a household size of 8 and this particular person has an unusually high balance in this quarter. 

## Libaries 
- helper_classification 
- IPython
- pandas as pd
- scipy
- seaborn as sns
- matplotlib
- numpy as np
- imblearn
- sklearn
- warnings
