# ...existing code...
print("Exercise 4.10")
print()

installationType = input("Enter the installation type (R for residential, I for industrial, and C for commercial): ").upper()
energyConsumption = float(input("Enter the energy consumption in kWh: "))

# config: type -> (name, thresholdKwh, rateIfBelowOrEqual, rateIfAbove)
configs = {
    "R": ("Residential", 500, 0.4, 0.65),
    "I": ("Industrial", 1000, 0.55, 0.6),
    "C": ("Commercial", 5000, 0.55, 0.6),
}

data = configs.get(installationType)
if not data:
    print("Invalid installation type. Use R, I or C.")
else:
    installation, thresholdKwh, rateIfBelowOrEqual, rateIfAbove = data
    rate = rateIfBelowOrEqual if energyConsumption <= thresholdKwh else rateIfAbove
    bill = rate * energyConsumption

    message = f"""
Your installation type is {installation}.
You consumed {energyConsumption} kWh this month.
The rate for your consumption and installation type is R${rate:.2f}/kWh.
Your electricity bill is R${bill:5.2f}
"""
    print(message)
