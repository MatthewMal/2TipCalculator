print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? "))
tip = int(input("How much would you like to tip? %"))/100 + 1
people_to_split = int(input("How many people is the bill split across? "))

pay_per_person = "{:.2f}".format(round(bill/people_to_split * tip, 2))
print(f"Each person should pay: ${pay_per_person}")
