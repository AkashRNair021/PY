import datetime

# Get the current year
current_year = datetime.datetime.now().year

# Prompt the user to enter the final year
final_year_str = input("Enter the final year: ")

# Convert the user's input to an integer
final_year = int(final_year_str)

# Calculate the difference in years
years_difference = final_year - current_year

# Print the result
print(f"The number of years between {current_year} and {final_year} is {years_difference}.")
