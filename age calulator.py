from datetime import datetime

def age_calculator():
    print("Welcome to the Age Calculator!")
    
    # Get user input
    birth_date_input = input("Enter your date of birth (YYYY-MM-DD): ")
    
    try:
        # Convert input to a date object
        birth_date = datetime.strptime(birth_date_input, "%Y-%m-%d")
        today = datetime.today()
        
        # Calculate the age
        age = today.year - birth_date.year
        
        # Adjust for the month and day
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
        
        print(f"Your age is: {age} years")
    except ValueError:
        print("Invalid date format! Please use YYYY-MM-DD.")

# Run the calculator
age_calculator()
