import functools
from typing import Union
import csv
import sys


def validate_num(func):
	'''
	Overview:
		Setters for attributes that are ints/floats:
			1. Verifies prices for Item.expense are int/floats > 0
			2. Verifies prices for MonthlyBudget.totals (various categories)
				are int/floats > 0

	Class Appearances:
		1. Item (.price)
		2. MontlhyBudget (.sub_total, .invest_total, .travel_total, .fodd_total, .home_total,
		misc_total)
	'''

	@functools.wraps(func) # Introspection used to preserve Metadata
	def wrapper(instance, value):
		if not isinstance(value, (int, float)) or not value >= 0:
			raise ValueError("Price is supposed to be int/float >= 0")
		return func(instance, value)
	return wrapper

def validate_str(func):
	'''
	Overview:
		Setter for name attribute
		Verifies if the value of the name is a str

	Class Appearances:
		A) Item.name (name of object)
		B) MonthlyBudget.name (name of object)
	'''

	@functools.wraps(func) # Introspection used to preserve Metadata
	def wrapper(instance, value: str):
		if not isinstance(value, str):
			raise ValueError("Name is supposed to be string")
		return func(instance, value)
	return wrapper

class Item:
	def __init__(self, name: str, price: Union[int, float] = 0) -> None:
		'''
		Sets the name and price for each expense extracted from imported CSV
		If a price is not provided for the Item, then it is defaulted to 0
		'''
		self.name = name
		self.price = price

	def __str__(self) -> str:
		return f"{self._name} is worth ${self._price:.2f}"

	@property
	def name(self) -> str:
		return self._name

	@name.setter
	@validate_str
	def name(self, value: str) -> None:
		self._name = value

	@property
	def price(self) -> Union[int, float]:
		return self._price

	@price.setter
	@validate_num
	def price(self, value: Union[int, float]) -> None:
		self._price = value


class MonthlyBudget:
	def __init__(self, name: str, sub_total: Union[int, float]=0, invest_total: Union[int, float]=0, travel_total: Union[int, float]=0, food_total: Union[int, float]=0, home_total: Union[int, float]=0, misc_total: Union[int, float]=0, crypto_total: Union[int, float]=0) -> None:
		'''
		A) Initalizes prices of all categories for a given month
		if a price for a category within month is provided, then category total will be initalized (without the execution of self.categorize())

		B) Every category will have a list of various expenses (type Item) associated with it

		C) Every category will have a '_list' attribute that holds the name and price of each expense (within that specific category)

		The categories for each month are as follows:
		1. sub_total = Total price for all monthly subscription expenses
		2. invest_total = Total price for all investments
		3. travel_total = Total price for all travel expenses
		4. food_total = Total price for all food expenses
		5. home_total = Total price for all monthly home expenses
		6. misc_total = Total cost for all monthly miscellaneous expenses
		'''
		self.name = name

		self.sub_items = []
		self.sub_total = sub_total

		self.invest_items = []
		self.invest_total = invest_total

		self.travel_items = []
		self.travel_total = travel_total

		self.food_items = []
		self.food_total = food_total

		self.home_items = []
		self.home_total = home_total

		self.misc_items = []
		self.misc_total = misc_total

		self.crypto_total = crypto_total

	def __str__(self) -> str:
		return (
			f"{self.name} has the following details: \n"
			f"Total subscriptions are: ${round(self.sub_total ,2):02} \n"
			f"Subscription items include: {self.sub_items} \n"
			f"Total investments are: ${round(self.invest_total, 2):02} \n"
			f"Investment items include: {self.invest_items} \n"
			f"Total travel expenses are: ${round(self.travel_total, 2):02} \n"
			f"Travel items include: {self.travel_items} \n"
			f"Total food expenses are: ${round(self.food_total, 2):02} \n"
			f"Food items include: {self.food_items} \n"
			f"Total home expenses are: ${round(self.home_total, 2):02} \n"
			f"Home items include: {self.home_items} \n"
			f"Total misc expenses are: ${round(self.misc_total, 2):02} \n"
			f"Misc items include: {self.misc_items} \n"
		)


	''' Getters & Setters for each category '''

	@property
	def name(self) -> str:
		return self._name

	@name.setter
	@validate_str
	def name(self, value: str) -> None:
		self._name = value

	@property
	def sub_total(self) -> Union[int, float]:
		return round(self._sub_total, 2)

	@sub_total.setter
	@validate_num
	def sub_total(self, value: Union[int, float]) -> None:
		self._sub_total = value

	@property
	def invest_total(self) -> Union[int, float]:
		return round(self._invest_total, 2)

	@invest_total.setter
	@validate_num
	def invest_total(self, value: Union[int, float]) -> None:
		self._invest_total = value

	@property
	def travel_total(self) -> Union[int, float]:
		return round(self._travel_total, 2)

	@travel_total.setter
	@validate_num
	def travel_total(self, value: Union[int, float]) -> None:
		self._travel_total = value

	@property
	def food_total(self) -> Union[int, float]:
		return round(self._food_total, 2)

	@food_total.setter
	@validate_num
	def food_total(self, value: Union[int, float]) -> None:
		self._food_total = value

	@property
	def home_total(self) -> Union[int, float]:
		return round(self._home_total, 2)

	@home_total.setter
	@validate_num
	def home_total(self, value: Union[int, float]) -> None:
		self._home_total = value

	@property
	def misc_total(self) -> Union[int, float]:
		return round(self._misc_total, 2)

	@misc_total.setter
	@validate_num
	def misc_total(self, value: Union[int, float]) -> None:
		self._misc_total = value

	@property
	def crypto_total(self) -> Union[int, float]:
		return round(self._crypto_total, 2)

	@crypto_total.setter
	@validate_num
	def crypto_total(self, value: Union[int, float]) -> None:
		self._crypto_total = value


	def categorize(self, item: Item, itemcategory: str) -> None:
		'''
		Description:
		Method is used to categorize an expense ('Item' object)

		1. Method collects all 'Item' objects that fit into the categories below:
		['Subscription', 'Investment', 'Travel', 'Food', 'Home']
		2. Parameters are as follows:
		a) item - Item object
		b) category - One of the 5 listed above (will default to Misc if not categorized)
		'''

		if not isinstance(item, Item):
			raise ValueError("You must deal with Item types")

		try:
			itemcategory = itemcategory.capitalize()
		except AttributeError:
			raise AttributeError("Please utilize a string!")

		match itemcategory:
			case 'Sub':
				self.sub_total += item.price
				self.sub_items.append({"Item": item.name, "Price": item.price})
			case 'Invest':
				self.invest_total += item.price
				self.invest_items.append({"Item": item.name, "Price": item.price})
			case 'Travel':
				self.travel_total += item.price
				self.travel_items.append({"Item": item.name, "Price": item.price})
			case 'Food':
				self.food_total += item.price
				self.food_items.append({"Item": item.name, "Price": item.price})
			case 'Home':
				self.home_total += item.price
				self.home_items.append({"Item": item.name, "Price": item.price})
			case 'Crypto':
				# No attribute for crypto 'items'; you are only calculating the price
				self.crypto_total += item.price
			case _:
				self.misc_total += item.price
				self.misc_items.append({item.name, item.price})

	def summary(self) -> str:
		'''
			This methods takes the sums from each category and provides an overview of:
			1. Total Amount Spent, Total Income
			2. Total Net Cash (Income - $ Spent) + Total Investments
			3. Net Worth (Cash + Cash Owed + Crypto Balance + 401k + HSA)
			**I have records to assess Cash/Crypto; will increment 401k/HSA incrementally
		'''

		# Monthly Summary
		grand_total = self.sub_total + self.invest_total + self.travel_total + self.food_total + self.home_items + self._misc_total
			# Total Income Calculation
		try:
			paycheck1 = float(input("First paycheck for month was: "))
			paycheck2 = float(input("Second paycheck for month was: "))
		except ValueError:
			raise ValueError("Ensure that you are inputting ")
		total_income = paycheck1 + paycheck2

		# Investment Summary
		net_income = total_income - grand_total - self.crypto_total
		total_investments = float(input("Enter recurring investment contributions or enter 0.00 (no contributions)")) + self.crypto_total
		total_invest = net_income + total_investments

		# Net Worth
		try:
			bank_cash = float(input("First paycheck for month was: "))
			cash_owed = float(input("Enter $ that people owe you: "))
			crypto_portfolio = float(input("Ledger Live / Coinbase Totals: "))
			retire_acct = float(input("Enter balance in 401k: "))
			hsa_acct = float(input("Enter balance in HSA account: "))
		except ValueError:
			raise ValueError("Please enter a numerical datatype")
		total_networth = bank_cash + cash_owed + crypto_portfolio + retire_acct + hsa_acct

		#Print summary statement depicting financial activity for a given month
		return (
			f"In {self.name}:"
			f"\n"
			f"OVERVIEW:"
			f"You spent ${grand_total:02}"
			f"Your total income was ${total_income:02}"
			f"\n"
			f"INVESTMENT BREAKDOWN:"
			f"You saved ${net_income:02}"
			f"You invested ${total_investments:02}"
			f"You've added ${total_invest:02} to your net worth"
			f"Your current net worth is: ${total_networth:02}"
		)

def csv_read(input_file, MonthlyBudget):
	'''
		Takes CSV file, reads contents (line by line) and appends transaction (Item type) to category (key).

		1. Function checks if csv file is currently being assessed (system will exit if not)
		2. 
	'''
	variable_names = {}
	count = -1

	if input_file[-4:] != ".csv":
		sys.exit("Please ensure that you're working with a csv file!")

	try:
		with open(input_file) as file:
			reader = csv.reader(file)

			for row in reader:
				count += 1
				print()

				if row[0] == "":
					continue

				name = row[0]
				print(name)

				if row[1] != "":
					try:
						price = float(row[1])
						print(price)
					except ValueError:
						raise ValueError("You must work with a numerical type")
				else:
					try:
						price = float(input("Enter price of transaction: "))
					except ValueError:
						raise ValueError("You must work with a numerical type")


				break_loop = input("Do you want to stop auditing expenses? (Y/N): ").strip().upper()
				if break_loop == 'Y':
					break

				skip_line = input("Do you desire to skip line? (Y/N): ").strip().upper()
				if skip_line == 'Y':
					continue

				name_change = input("Do you want to change the name of this expense? (Y/N): ").strip().upper()

				if name_change == 'Y':
					name = input("Please enter the new name: ")
					print(name)

				print(variable_names.keys())
				variable_name = input("Enter name of Item instance (expense): ")

				if variable_name in variable_names:
					variable_names[variable_name].price += price
				else:
					variable_names[variable_name] = Item(name, price)
					category_name = input("Enter the category of Item instance (['Sub', 'Invest', 'Travel', 'Food', 'Home', 'Crypto'] - each category not set to list categories is categorized as 'Misc' by default): ")
					MonthlyBudget.categorize(variable_names[variable_name], category_name)


			print(f"You got to line {count}!")
			print()
		return MonthlyBudget
	except FileNotFoundError:
		raise FileNotFoundError("The file was not found. Please check the file path and try again.")

def csv_write(MonthlyBudget):

	category_directory = {
		'Subscriptions': [MonthlyBudget.sub_items, MonthlyBudget.sub_total],
		'Investments': [MonthlyBudget.invest_items, MonthlyBudget.invest_total],
		'Travel': [MonthlyBudget.travel_items, MonthlyBudget.travel_total],
		'Food': [MonthlyBudget.food_items, MonthlyBudget.food_total],
		'Groceries / Home Essentials': [MonthlyBudget.home_items, MonthlyBudget.home_total],
		'Misc': [MonthlyBudget.misc_items, MonthlyBudget.misc_total]
	}

	categories = list(category_directory.keys())
	blank_row = []

	try:
		mode = input("Please enter the writing mode for this file (a/w): ").strip().lower()

		if mode in ['a', 'w']:
			with open(input('Enter file_name.csv: '), mode, newline='') as csvfile:

				field_names = ['Item', 'Price']

				print_expenses = csv.DictWriter(csvfile, field_names)
				print_header = csv.writer(csvfile)

				append = input('Are you appending this file? (Y/N): ').strip().upper()

				# Do not write the header if you've already gotten started with the file
				if append == 'Y':
					pass
				else:
					print_header.writerow([input('Format - Month YYYY (ex. March 2023) ')])

				for i in range(len(categories)):

					# If you have already written to the file for a specific category, you can skip that category
					print(f"You are writing {categories[i]} to 'sample.csv'")

					skip = input('Do you wish to skip this category? (Y/N): ').strip().upper()
					if skip == 'Y':
						continue
					
					# Takes each category and lists related expenses
					print_header.writerow([categories[i]])
					print_expenses.writerows(category_directory[categories[i]][0])

					# I believe this should be a blank row
					print_header.writerow(blank_row)

					print_header.writerow(['Total', category_directory[categories[i]][1]])

					# I believe this should be a blank row (to seperate the expenses for categories within the CSV)
					print_header.writerow(blank_row)
					print_header.writerow(blank_row)
	except TypeError:
		raise TypeError("You ran into an issue while writing to the file")
