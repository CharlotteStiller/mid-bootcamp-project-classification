# Project 02 - Credit Card Classification
by Charlotte Stiller

![Hier sollte ein Bild zu sehen sein](https://st2.depositphotos.com/2704315/7774/v/600/depositphotos_77740328-stock-illustration-hand-holding-credit-card-vector.jpg)



## About the project


1 Executive Summary / Introdution
Project description
For the project we have data from a marketing study with 18.000 current bank customers. We want to understand the demographics and other characteristics of its customers that accept a credit card offer and that do not accept a credit card. . 

Objective
The goal of the binary classification project is to analyse the characteristics of the bank customers and to train a model to predict if a bank customer accept or reject a credit card offer.


|               Column |                                                                          Information  | Type     |
|---------------------:|--------------------------------------------------------------------------------------:|---------:|
|      customer_number |                                        A sequential number assigned to the customers. |    int64 |
|       offer_accepted |                               Did the customer accept (Yes) or reject (No) the offer. |   object |
|               reward |                                      The type of reward program offered for the card. |   object |
|          mailer_type |                                                                   Letter or postcard. |   object |
|         income_level |                                                                  Low, Medium or High. |   object |
|   bank_accounts_open |                           How many non-credit-card accounts are held by the customer. |    int64 |
| overdraft_protection | Does the customer have overdraft protection on their checking account(s) (Yes or No). |   object |
|        credit_rating |                                                                  Low, Medium or High. |   object |
|    credit_cards_held |                                          The number of credit cards held at the bank. |    int64 |
|          homes_owned |                                            The number of homes owned by the customer. |    int64 |
|       household_size |                                                  Number of individuals in the family. |    int64 |
|        own_your_home |                                        Does the customer own their home? (Yes or No). |   object |
|      average_balance |            Average account balance (across all accounts over time). Q1, Q2, Q3 and Q4 |  float64 |
|        q1-q4 balance |                                     Average balance for each quarter in the last year |  float64 |

Meaning of the columns: [Link](https://github.com/Ironhack-Data-0621-Remote/mid-bootcamp-project/blob/master/classification/project_details_classification.md)



### Workflow of your project?


1. **Apply agile Project Management to deliver results**
    - Delivery: Tab Projects 
    - Use a Kanban Board to self-manage my project
    - Create cards to manage my progress during the project 

2. **Get the data to SQL Database**
    - Files: Questions_SQL - Classification.md / Solutions SQL- Classification.ipynb
    - Connect the SQL database to Python and pull the datafram in Python
    - Write queries to extract the information I need

  
3.  **Perform Exploratory Data Analysis** 
    - Explore the data 
    - Fit the model
    - Check accuracy of the model (exploring *Variance vs. Bias* tradeoff)
    - Iterate on the model to get more optimized results.
  
4. **Present a professional project** 
    - Produce documentation to make the project accessible
    - Build engaging presentations
    - Include storytelling to your presentation!

### Findings / Results 

1. **Which model works for the dataset**
    - KNN works for the dataset, but 
    - Logistic 

### Project | Moduls I used 

### Dataset(s) 


### For code

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```
