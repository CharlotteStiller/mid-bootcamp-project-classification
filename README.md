# Project 02 - Credit Card Classification
by Charlotte Stiller

![Hier sollte ein Bild zu sehen sein](https://st2.depositphotos.com/2704315/7774/v/600/depositphotos_77740328-stock-illustration-hand-holding-credit-card-vector.jpg)

The objective of this project was to is to build a model that will provide insight into why some bank customers accept credit card offers, as well as answer additional questions by top management related to the matter.

In ordert o to this, I used agile project planning in Github and made use of SQL, Python and Tableau. 

## About the project

Project description
For the project we have data from a marketing study with 18.000 current bank customers. We want to understand the demographics and other characteristics of its customers that accept a credit card offer and that do not accept a credit card. . 

Objective
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



### Workflow


1. **Exploring the data in SQL**
    - Files: Questions_SQL - Classification.md / Solutions SQL- Classification.ipynb
    - Write queries to extract demographics and other characteristics of its customers

  
2.  **Perform exploratory data analysis and fit the model in Python** 
    - Files: Questions_SQL - Classification.md / Solutions SQL- Classification.ipynb
    - Explore the data 
    - Fit the model

  
3. **Analyse and vizualize in Tableau** 
    - Files: Questions_SQL - Classification.md / Solutions SQL- Classification.ipynb


### Findings / Results 

2. **Which model works for the dataset**
- Logistic Regression with changed class weights fits best for this dataset. Highest Yes recall: 0.69.  
- Next step to evaluate this model: Cut the variables which do not improve the prediction and improve the weight/balance
- For the next marketing study I would recommend to change the questions which have no relationship to the target variable (Like shown in point 5.2.) and to build bins (For example house hold size 5-9) 


### Libaries 
from helper_v1 import *
import pandas as pd
from scipy.stats 
import seaborn as sns
from IPython import display
import matplotlib
import numpy as np
from imblearn
from sklearn
import warnings
