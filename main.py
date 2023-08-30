
talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

total_grams = float(talents * 20 * 32 + pounds * 32 + lots) * 13.3
total_kilograms = int(total_grams/1000)
remainder_grams = total_grams - total_kilograms*1000


print(f"Converting the total weight into modern units: {total_kilograms:.0f} kilograms {remainder_grams:.2f} grams")





