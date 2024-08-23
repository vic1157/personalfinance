# personalfinance

Current:

This project allows users to upload CSV files of credit card and bank statements to calculate expenses in a given month. This project is backend only at the moment. 

Coming Soon:

1. Front-End 
2. Net Worth Tracker

## Introduction

Keeping track of expenses can be daunting, however, there are solutions that exist to make budgeting 'seamless' (You Need A Budget, Mint, Monarch Money, etc). With everything in life, there are tradeoffs involved with the available decisions.

My preference lies in managing my money myself - renaming vendors (original transactions on statements may be ambigious), assessing the nuance of transactions (incorrectly charged, etc), updating prices based on subsidies/discounts and keeping tabs on unaccounted money that is on the way.

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
3. Total Investments (described above + employer match)
4. Misc Expenses (Insurance Deductions)
5. Money Spent
6. Net Cash (Total Cash Influx - Total Expenses)

These metrics allow me to calculate amount spent, saved and invested in percentages of my total cash influx.

## Purpose

Overall, different people manage money in different ways. I prefer to be granular with data, to ensure that I remain proactive with budgeting vs. taking a more passive approach. 

This project was inspired by my desire to maintain the quality of my accounting while facing the time constraints that life brings. I found myself so busy in April 2023, that after I missed that month, I never documented my expenses for the remainder of the year. For context, my original accounting process involves reviewing statements from my bank and credit cards (MANUALLY) to document expenses and net income at the end of the month. Doing this would take 1.5-3 hours every month, based on my spending activity. 

Faced with an excessive backlog, I understood catching up would require several hours that I didn't have. But I understood that I could export bank/credit card statements in CSV format and import them into this program. Not having to copy and paste transactions and semi-automate my budgeting workflow, while remaining proactive made implementing this program a no-brainer. 

## Features

Key Features of this project:
1. CSV Processing of Bank/Credit Card Statement
2. Ability to re-name transactions (ex. Fidelity Investments appears as 'ACH DEBIT FID BKG SVC LLC')
3. Ability to categorize transactions (Investments, Travel, Food, Home, Misc, Crypto) - feel to update the 'MonthlyBudget' class to include categories of your preference