from init_pfinance import MonthlyBudget, csv_read, csv_write


def main():
	# Initializing the MonthlyBudget object where expenses (Item objects) will be written to
	Mar_2023 = MonthlyBudget("March_2023")

	# Using the input csv (Mar2023.csv) to write expenses to MonthlyBudget object
	# Printing the Item expenses that are tied to the MonthlyBudget object
	mBudget = csv_read("Mar2023.csv", Mar_2023)
	print(mBudget)

	# csv_write will take the Items written and return a CSV file in 'budget' format
	csv_write(mBudget)

	
if __name__ == "__main__":
	main()