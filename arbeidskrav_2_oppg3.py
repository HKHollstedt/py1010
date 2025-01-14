#Oppg 3 arbeidskrav 2

import numpy as np

def grad_rad (g):
    formel = g * np.pi/180
    return formel 

v_grad = float(input("Skriv inn gradtallet: "))

v_rad = grad_rad (v_grad)

print ("Det blir da", v_rad, "i radianer")



#print("Dette blir da ", v_rad, "i radianer")
