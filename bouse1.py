# Ask user for weight and height
weight = float(input("Please enter your weight in kilograms: "))
height = float(input("Please enter your height in meters: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Print BMI result
print(f"Your BMI is: {bmi:.2f}")

# Give advice based on BMI
if bmi >= 25:
    print("You are overweight")
elif bmi >= 18.5:
    print("You are fit & healthy")
else:
    print("You are underweight")
