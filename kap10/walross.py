zahlenliste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3]

# Ohne den Walrus-Operator:
positive_sum = 0
for num in zahlenliste:
    if num > 0:
        positive_sum += num

print("Summe der positiven Zahlen (ohne Walrus-Operator):", positive_sum)

# Mit dem Walrus-Operator:
positive_sum = 0
for num in zahlenliste:
    if (positive_num := num) > 0:
        positive_sum += positive_num

print("Summe der positiven Zahlen (mit Walrus-Operator):", positive_sum)
