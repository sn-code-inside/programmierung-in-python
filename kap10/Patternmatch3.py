woerter = ["Apfel", "Banane", "Erdbeere", "Ananas", "Birne", "Pflaume"]

for w in woerter:
    match w:
        case "A":
            print(f"Das Wort beginnt mit 'A': {w[1:]}")
        case "Ba":
            print(f"Das Wort beginnt mit 'Ba': {w[2:]}")
        case _:
            print(f"Das Wort beginnt weder mit 'A' noch 'Ba': {w}")
