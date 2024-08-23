# personalfinance

Current:

This project allows users to upload CSV files of credit card and bank statements to calculate expenses and net worth in a given month. This project is backend only at the moment. 

Full webapp with frontend is coming soon!

**Disclaimer: You must have Python 3.10 or later to run this script!**

## Introduction

Keeping track of expenses can be daunting, however, there are solutions that exist to make budgeting 'seamless' ([You Need A Budget](https://www.ynab.com/), [Mint](https://www.creditkarma.com/lp/mint-to-credit-karma-net-worth-signup), [Monarch Money](https://www.monarchmoney.com/), etc). With everything in life, there are tradeoffs involved with the available decisions.

My preference lies in managing my money myself - renaming vendors (original transactions on statements may be ambigious), assessing the nuance of transactions (priced incorrectly, etc), updating prices based on subsidies/discounts and keeping tabs on unaccounted money that is on the way.

<ins> For example, there is a specific way that I calculate my expenses for the month: </ins>

Total Expenses = SUM(expenses) + After Tax Investments (BTC, ETH, Roth IRA)
(I categorize every dollar that leaves my account as an 'expense' even if I am investing)

<ins> I keep tabs on the net cash saved and invested: </ins>

Cash Saved = Salary (After Taxes) - Total Expenses (calculation above)


<ins> There is also a unique way that I calculate my net worth: </ins>

Net Worth = Cash (In Bank) + Cash Owed + Crypto Balance + 401k + HSA

<ins> Making a monthly report allows me to develop an end of year report that details: </ins>

1. Total Net Pay (from Employer)
2. Total Cash Influx (into bank account)
3. Total Investments
4. Misc Yearly Expenses (Insurance Deductions, Credit Card Annual Fees, etc)
5. Total Yearly Expenses
6. Net Cash (Total Cash Influx - Total Yearly Expenses)

These metrics allow me to calculate amount spent, saved and invested in percentages of my total cash influx.

## Purpose

Overall, different people manage money in different ways. I prefer to be granular with data to ensure that I remain proactive with budgeting vs. taking a more passive approach. 

This project was inspired by my desire to maintain the quality of my accounting while facing the time constraints that life brings. I found myself so busy in April 2023, that after I missed that month, I never documented my expenses for the remainder of the year. For context, my original accounting process involves reviewing statements from my bank and credit cards (MANUALLY) to document expenses and net income at the end of the month. Doing this would take 1.5-3 hours every month, based on my spending activity. 

Faced with an excessive backlog, I understood catching up would require several hours that I didn't have. But I understood that I could export bank/credit card statements in CSV format and import them into this program. Not having to copy/paste transactions and semi-automate my budgeting workflow while remaining proactive made implementing this script a no-brainer. 

## Features

<ins> High-Level Features of this project: </ins>

1. CSV Processing of Bank/Credit Card Statement
2. Ability to re-name transactions (ex. Fidelity Investments appears as 'ACH DEBIT FID BKG SVC LLC')
3. Ability to categorize transactions (Investments, Travel, Food, Home, Misc, Crypto) - feel to update the 'MonthlyBudget' class to include categories of your preference
4. Monthly Spending Report (Total Expenses / Cash Saved / Net Worth - explained above)

## Classes & Functions 

<ins> Functions: </ins>

**To get a high-level overview of csv_read and csv_write, assess the implementation of helper_pfinance.py**

1. csv_read - Takes CSV file and translates data from file into Item and MonthlyBudget objects. CSV Source Row --> Item Object --> Several Item Objects = MonthlyBudget Object (run csv_file multiple times and write to same MonthlyBudget object for multiple bank/credit card statement sources)
2. csv_write - Takes data from MonthlyBudget object and exports into CSV report for the month 

**Decorators**

3. validate_num - A setter for attributes of int/float datatype; ensures that non-numerical inputs are rejected when necessary
4. validate_str - A setter for attributes of string datatype; ensures that non-string inputs are rejected when necessary


<ins> Classes (and Methods): </ins>

1. Item (Class) - Object that sets the name and price for each expense extracted from imported CSV (each row in CSV = transaction name + price)

2. MonthlyBudget (Class) - Consolidates all expenses within a month into one object
	A. Initalizes prices of all categories for a given month 
	B. Every category will have a list of various expenses (type Item) associated with it
	C. Every category will have a '_list' attribute that holds the name and price of each expense (within that specific category)

3.  MonthlyBudget.categorize (Method) - Used to categorize an expense ('Item' object)

4. MonthlyBudget.summary (Method) - Gives an high-level overview of spending activity and provides an overview of:
	A. Total Amount Spent, Total Income
	B. Total Net Cash (Income - $ Spent) + Total Investments
	C. Net Worth (Cash + Cash Owed + Crypto Balance + 401k + HSA)
	


