# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
print_greeting()


# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    # Your control flow logic goes here
  list_of_vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
  list_of_consonants = ["b", "B", "c", "C", "d", "D", "f", "F", "g", "G", "h", "H", "j", "J", "k", "K", "l", "L", "m", "M", "n", "N", "p", "P", "q", "Q", "r", "R", "s", "S", "t", "T", "v", "V", "w", "W", "x", "X", "y", "Y", "z", "Z"]
  x = input("Enter a letter:")
  if x in list_of_vowels:
    print(f"The letter {x} is a vowel")
  elif x in list_of_consonants:
    print(f"The letter {x} is a consonant")
  else:
    print(f"{x} is not a letter")
  
  
# Call the function
check_letter()


# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
    # Your control flow logic goes here
  x = input("Please enter your age:")
  if int(x) < 0:
    print("Not a valid age.")
  elif int(x) >= 18:
    print("You are old enough to vote.")
  else:
    print("You are not old enough to vote.")

# Call the function
check_voting_eligibility()


# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    # Your control flow logic goes here
  FIRST_YEAR = 10
  SECOND_YEAR = 10
  ANOTHER_YEAR = 7
  x = input("Input a dog's age:")
  if int(x) == 1:
    print(f"The dog's age in dog years is {FIRST_YEAR}")
  elif int(x) == 2:
    print(f"The dog's age in dog years is {(FIRST_YEAR + SECOND_YEAR)}")
  elif int(x) >= 3:
    print(f"The dog's age in dog years is {(FIRST_YEAR + SECOND_YEAR) + ((int(x) - 2) * ANOTHER_YEAR)}")
# Call the function
calculate_dog_years()


# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    # Your control flow logic goes here
  x = input("Is it cold? (yes/no):")
  y = input("Is it raining? (yes/no):")
  if x == "yes" and y == "yes":
    print("Wear a waterproof coat.")
  elif x == "yes" and y == "no":
    print("Wear a warm coat.")
  elif x == "no" and y == "yes":
    print("Carry an umbrella.")
  elif x == "no" and y == "no":
    print("Wear light clothing.")
# Call the function
weather_advice()


# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
    # Your control flow logic goes here
  WINTER_SEASONS = [ "Jan", "Feb"]
  SPRING_SEASONS = [ "Apr", "May"]
  SUMMER_SEASONS = [ "Jul", "Aug"]
  FALL_SEASONS = [ "Oct", "Nov"]
  month = input("Enter the month of the year (Jan - Dec):")
  day = input("Enter the day of the month:")
  if (month == "Dec" and (int(day) >= 21 and int(day) < 32)) or (month == "Mar" and int(day) <= 19) or (month == "Feb" and (int(day) > 0 and int(day) <= 29)) or (month in WINTER_SEASONS and (int(day) > 0 and int(day) <= 31 )):
    print(f"{month} {day} is in Winter.")
  elif (month == "Mar" and (int(day) >= 20 and int(day) < 32)) or (month == "Jun" and int(day) <= 20) or (month in SPRING_SEASONS and (int(day) > 0 and int(day) <= 31 )):
    print(f"{month} {day} is in Spring.")
  if (month == "Jun" and (int(day) >= 21 and int(day) < 32)) or (month == "Sep" and int(day) <= 21) or (month in SUMMER_SEASONS and (int(day) > 0 and int(day) < 31 )):
    print(f"{month} {day} is in Summer.")
  if (month == "Sep" and (int(day) >= 22 and int(day) < 32)) or (month == "Dec" and int(day) <= 20) or (month in FALL_SEASONS and (int(day) > 0 and int(day) < 31 )):
    print(f"{month} {day} is in Fall.")
# Call the function
determine_season()
