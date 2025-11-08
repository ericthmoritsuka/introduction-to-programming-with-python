print("Exercise 4.9")
print("\n")

installationType = input("Enter the installation type (R for residential, I for industrial, and C for commercial): ").upper()
energyConsumption = float(input("Enter the energy consumption in kWh: "))
installation = ""

rate = 0.0
if installationType == "R":
   installation = "Residential"
   if energyConsumption <= 500:
      rate = 0.4
   else:
      rate = 0.65
elif installationType == "I":
   installation = "Industrial"
   if energyConsumption <= 1000:
      rate = 0.55
   else:
      rate = 0.6
elif installationType == "C":
   installation = "Commercial"
   if energyConsumption <= 5000:
      rate = 0.55
   else:
      rate = 0.6

message = f"""
Your installation type is {installation}.
You comsumed {energyConsumption} kWh this month.
The rate for your consumption and installation type is R${rate}/kWh.
Your eletricity bill is R${rate*energyConsumption:5.2f}
"""

print(message)
