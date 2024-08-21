
def treffer(data):
    match data:
        case (1, 2):
            print("Das Muster ist (1, 2)")
        case (x, _):
            print(f"Das Muster enthält {x} als erstes Element")
        case _:
            print("Kein Muster passt")
treffer((1,2))
treffer((7,5))
treffer((3,"Beliebiger Text"))
treffer((2,3,5,7,11))
treffer((1,3,5,7,11))
treffer((9,(3,5,7,11)))

