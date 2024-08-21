data = [1, 'A', 2, 'B']
for i in data:
    match i:
        case int(x):
            print(f'Gefundene Zahl: {x}')
        case _:
            pass  # Wir ignorieren alles andere


