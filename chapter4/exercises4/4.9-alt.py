print("Exercise 4.9 - ALTERNATIVE SOLUTION")
print("\n")

houseValue = float(input("Enter the value of the house: R$ "))
salary = float(input("Enter your salary: R$ "))
loanTerm = int(input("Enter the loan term (in years): "))

loanTermInMonths = loanTerm*12
monthlyPayment = houseValue/loanTermInMonths
salaryLimit = salary * 0.3

# This adds a common message to the final print
commonMessage = f"""
Monthly Payment = R${monthlyPayment:5.2f}
30% of your salary = R${salaryLimit}"""

# This is a conditional message that depends on our condition
loanStatus = "The monthly payment cannot be higher than 30% of your salary\nYou shouldn't take this loan!" if monthlyPayment > salaryLimit else "You can take the loan!"

print(loanStatus + commonMessage)