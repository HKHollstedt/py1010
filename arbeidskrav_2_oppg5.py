#Oppg 5)

def funk_omkrets_areal (a,b):
    radius = a/2 #radis er diameter(a) delt på 2
    hypothenus = (a ** 2 + b **2) **0.5 #**0.5 er formel for kvadratrot fant jeg ut av, a** er a opphøyd i 2
    
    areal_trekant = (a*b)/2 #arealet på trekanten er sidene delt på 2
    areal_halvsirkel = (3.14 * radius **2)/2 #arealet på en sirkel er pi*radius opphøyd i 2, deler på 2 pga halvsirkel
    total_areal = areal_trekant + areal_halvsirkel #slår de sammen
    
    ytre_omkrets_halvsirkel = (2 * 3.14 * radius)/2  # formel for omkrets av sirkel delt på 2
    ytre_omkrets_trekant = b + hypothenus # b + hypothenus (tar ikke med A fordi ikke ytre)
    total_omkrets = ytre_omkrets_trekant + ytre_omkrets_halvsirkel
    
    return total_omkrets, total_areal #+ ytre_omkrets

a1 = int(input("Hvor lang er a? "))
b1 = int(input("Hvor lang er b? "))

total_omkrets, total_areal = funk_omkrets_areal(a1, b1)


print ("totalt areal er da",total_areal,"og total omkrets er da ",total_omkrets)