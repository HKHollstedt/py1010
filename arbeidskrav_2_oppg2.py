#Oppg 2

antall_elever = int(input("Skriv inn antall elever: "))

antall_pizzaer = antall_elever/4


kjopsbehov = int(antall_pizzaer) + (antall_pizzaer % 1>0)# dette kan erstatte if setning

print("du trenger å kjøpe ", kjopsbehov, "pizzaer")