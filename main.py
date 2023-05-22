age = input("What is your current age?: ")
new_age = int(age)

age_in_days = 90 * 365
age_in_weeks = 90 * 52
age_in_months = 90 * 12


new_days = str(age_in_days - (new_age * 365))
new_weeks = str(age_in_weeks - (new_age * 52))
new_months = str(age_in_months - (new_age * 12))

print("You have "+ new_days +" days, " + new_weeks + " weeks," + new_months + " months left.")