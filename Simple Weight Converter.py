weight = int(input("Enter your weight: "))                    # Enter weight
unit = input("Select from kg, g, lbs or t: ")                 # Select from the given units such as kg, g, lbs or t
new_unit = input("Convert to kg, g, lbs or t: ")              # Select a unit to convert to the weight to

if unit.lower() == "kg" and new_unit.lower() == "kg":         # Converts uppercase values to lowercase if user entered KG or LBS instead
    print(f'You are {weight} kilograms')
elif unit.lower() == "lbs" and new_unit.lower() == "kg":
    weight_kg = weight / 2.205                                # Converts the weight to kg if the user chose lbs
    print(f'You are {weight_kg} kilograms')                   # Display the converted weight(kg)
elif unit.lower() == "t" and new_unit.lower() == "kg":
    weight_kg = weight * 1000
    print(f'You are {weight_kg} kilograms')
elif unit.lower() == "g" and new_unit.lower() == "kg":
    weight_kg = weight / 1000
    print(f'You are {weight_kg} kilograms')

elif unit.lower() == "g" and new_unit.lower() == "g":
    print(f'You are {weight} grams')
elif unit.lower() == "kg" and new_unit.lower() == "g":
    weight_g = weight * 1000
    print(f'You are {weight_g} grams')
elif unit.lower() == "lbs" and new_unit.lower() == "g":
    weight_g = weight * 453.6
    print(f'You are {weight_g} grams')
elif unit.lower() == "t" and new_unit.lower() == "g":
    weight_g = weight * 1000000
    print(f'You are {weight_g} grams')

elif unit.lower() == "lbs" and new_unit.lower() == "lbs":
    print(f'You are {weight} pounds')
elif unit.lower() == "kg" and new_unit.lower() == "lbs":
    weight_lbs = weight * 2.205                               # Converts the weight to lbs if the user chose kg
    print(f'You are {weight_lbs} pounds')                     # Display the converted weight(lbs)
elif unit.lower() == "g" and new_unit.lower() == "lbs":
    weight_lbs = weight / 453.6
    print(f'You are {weight_lbs} pounds')
elif unit.lower() == "t" and new_unit.lower() == "lbs":
    weight_lbs = weight * 2205
    print(f'You are {weight_lbs} pounds')

elif unit.lower() == "t" and new_unit.lower() == "t":
    print(f'You are {weight} tonnes')
elif unit.lower() == "kg" and new_unit.lower() == "t":
    weight_t = weight / 1000
    print(f'You are {weight_t} tonnes')
elif unit.lower() == "lbs" and new_unit.lower() == "t":
    weight_t = weight / 2205
    print(f'You are {weight_t} tonnes')
elif unit.lower() == "g" and new_unit.lower() == "t":
    weight_t = weight / 1000000
    print(f'You are {weight_t} tonnes')

else:
    print("Please try again with kg, g, lbs or t.")         # Try again message if the user enters values besides kg, g, lbs or t
