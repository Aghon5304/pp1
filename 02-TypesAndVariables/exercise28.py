height=float(input("Enter your height in cm: "))
weight=float(input("Enter your weight in kg: "))
bmi_index=weight/(height/100)**2
print(f"your BMI index: {bmi_index}\nCorrect weight: {bmi_index>=18.5 and bmi_index<=24.9}")