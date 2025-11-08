print("Exercise 4.9")
print("\n")

houseValue = float(input("Enter the value of the house: R$ "))
salary = float(input("Enter your salary: R$ "))
loanTerm = int(input("Enter the loan term (in years): "))

loanTermInMonths = loanTerm*12
monthlyPayment = houseValue/loanTermInMonths

if monthlyPayment > salary*0.3:
   print(f"The monthly payment cannot be higher than 30% of your salary")
   print(f"Monthly Payment = R${monthlyPayment:5.2f}")
   print(f"30% of your salary = R${salary*0.3}")
   print("You shouldn't take this loan!")
else:
   print(f"You can take the loan!")
   print(f"Monthly Payment = R${monthlyPayment:5.2f}")
   print(f"30% of your salary = R${salary*0.3}")