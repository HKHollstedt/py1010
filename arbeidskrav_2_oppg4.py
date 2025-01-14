#oppg 4

#a)
data = {
    "Norge": ["Oslo", 0.634], 
    "England":["London", 8.982],
    "Frankrike":["Paris",2.161], 
    "Italia":["Roma",2.873]
}


#4b)
data = {
    "Norge": ["Oslo", 0.634], 
    "England":["London", 8.982],
    "Frankrike":["Paris",2.161], 
    "Italia":["Roma",2.873]
}

fav_land = input ("Hvilket av:Norge, England, Frankrike og Italia er favorittlandet ditt?")

if fav_land in data:
    riktig_land = data[fav_land]
    print (f"Her er hovedstaden  {riktig_land[0]} og det er {riktig_land[1]} mill innbyggere i dette landet ")
#else:
 #   print(f"{fav_land} er ikke i listen")


#4c)

data = {
    "Norge": ["Oslo", 0.634], 
    "England":["London", 8.982],
    "Frankrike":["Paris",2.161], 
    "Italia":["Roma",2.873]
}

nytt_land = input("Kan du skrive et annet land enn Norge, England, Italia, Frankrike ? ")
ny_hovedstad = input ("Hvor er hovedstaden i dette landet? ")
nytt_innbyggertall = float(input("Hvor mange bor det der? "))

data [nytt_land] = [ny_hovedstad,nytt_innbyggertall]
print(data)
                  