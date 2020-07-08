# Starbucks Capstone Project
## Udacity Machine Learning Nanodegree Program

1. Description
2. Installation
3. Project Objectives
4. Data Sets

## Description
This Capstone Project is a requirement under Udacity DSND Program. We get the dataset from the program that creates the data simulates how people make purchasing decisions and how those decisions are influenced by promotional offers. I am trying to "Measure Marketing Campaign Effectiveness" using a data from the Starbucks Reward mobile App data for the customers' behavior on Starbucks electronic advertisement. Customers using Starbucks mobile app receive random offers from Starbucks, the offer might range from merely an informational offer advertising about a drink, to an discount offer that a customer can avail on their spending's at Starbucks, or a BOGO (Buy One Get One) offer. All these offers are time bound with a designated expiry. The customers are rewarded based on their cumulative spend activity during the period in which offer was active. The offers are sent to customers in no particular order, some customers might not receive any offer, while not all user receive the same offer.

## Installion
This repository is built on Google Colab. You may need to change few minor codes if running on other platform. There should be no necessary libraries to run the code here beyond the Anaconda distribution of Python. The code should run with no issues using Python versions 3.*.

## Project Objectives
We are interested to answer the following two questions:

Which offer should be sent to a particular customer to let the customer buy more?

Which demographic groups respond best to which offer type?

Which model can explain the custeromers' behaviour better?

## Data sets
The data is contained in three files:

portfolio.json - containing offer ids and meta data about each offer (duration, type, etc.)

profile.json - demographic data for each customer

transcript.json - records for transactions, offers received, offers viewed, and offers completed

Here is the schema and explanation of each variable in the files:


**portfolio.json**
id (string) - offer id

offer_type (string) - type of offer ie BOGO, discount, informational

difficulty (int) - minimum required spend to complete an offer

reward (int) - reward given for completing an offer

duration (int) - time for offer to be open, in days

channels (list of strings)


**profile.json**
age (int) - age of the customer
became_member_on (int) - date when customer created an app account
gender (str) - gender of the customer (note some entries contain 'O' for other rather than M or F)
id (str) - customer id
income (float) - customer's income


**transcript.json**
event (str) - record description (ie transaction, offer received, offer viewed, etc.)
person (str) - customer id
time (int) - time in hours since start of test. The data begins at time t=0
value - (dict of strings) - either an offer id or transaction amount depending on the record

## Materials
Starbucks_Data_ELT_and_EDA.ipynb: Notebook containing the ETL and EDA steps

Starbucks_Models.ipynb: Notebook containing the modeling codes

build_main_df_py.py: Notebook containing the functions of combining the dataframes

clean_portfolio_py.py: Notebook containing the fuctions of cleaning the portfolio dataset

clean_profile_py.py: Notebook containing the fuctions of cleaning the profile dataset

clean_transcript_py.py:Notebook containing the fuctions of cleaning the transcript dataset

main_df.csv: csv file conatining the cleaned transcript data

Data: folder containing the original datasets
