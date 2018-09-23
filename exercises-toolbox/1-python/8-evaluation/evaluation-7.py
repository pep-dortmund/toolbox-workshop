density_iron = 7.87
density_copper = 8.96

volumes_iron = [10.0, 16.7, 23.5, 28.5, 34.9]
volumes_copper = [10.0, 19.7, 28.6, 39.4, 50.1]


def calculate_metal_mass(volume, metal):
    if metal == "Fe":
        density = density_iron
    elif metal == "Cu":
        density = density_copper

    return density * volume

# In Fällen wie diesen,
# "durch eine Schleife über eine Liste wird eine neue Liste generiert",
# kann eine List-Comprehension¹ verwendet werden.

masses_iron = [calculate_metal_mass(volume, metal="Fe") for volume in volumes_iron]


masses_copper = [calculate_metal_mass(volume, metal="Cu")
                 for volume in volumes_copper]


print("Berechnete Massen für Eisen:")
print(masses_iron)

print("Berechnete Massen für Kupfer:")
print(masses_copper)


# ¹ Im deutschen würde man List-Comprehension mit Listen-Aussonderung übersetzen,
# dieser Begriff wird aber nicht verwendet.