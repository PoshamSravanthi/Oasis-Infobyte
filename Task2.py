def calculate_bmi(weight, height):
    """Calculate BMI and classify it into categories."""
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obesity"
    return bmi, category

def main():
    print("Welcome to the BMI Calculator!")
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        
        if weight <= 0 or height <= 0:
            print("Weight and height must be positive numbers.")
            return

        bmi, category = calculate_bmi(weight, height)
        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Category: {category}")
    except ValueError:
        print("Please enter valid numerical values for weight and height.")

if __name__ == "__main__":
    main()