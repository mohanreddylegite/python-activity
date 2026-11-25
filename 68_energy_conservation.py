# Case Study 68: Energy Conservation Before-and-After Analysis

print("ENERGY CONSERVATION ANALYSIS")
appliances = ["Air Conditioner", "Refrigerator", "Fan"]
before = [120, 90, 30]
after = [90, 85, 24]

results = []

for i in range(len(appliances)):
    saving = before[i] - after[i]

    if before[i] > 0:
        percentage = saving / before[i] * 100
    else:
        percentage = 0

    results.append((appliances[i], saving, percentage))

    if saving < 0:
        print(appliances[i], "consumption increased")

# Sort records by energy saved, highest first.
for i in range(len(results)):
    for j in range(i + 1, len(results)):
        if results[j][1] > results[i][1]:
            temp = results[i]
            results[i] = results[j]
            results[j] = temp

print("Ranking by Energy Saved:")
for item in results:
    name, saving, percentage = item
    print(name, "Saved:", saving, "kWh |", round(percentage, 2), "%")
