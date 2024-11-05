
Ant_km = 16000 # variabel for antall km kjørt i året (jeg kjører 16000 ca)

forsikring_EL = 5000 # variabel for forsikringskostnad EL-bil
forsikring_bens = 7500 # variabel for forsikringskostnad bensinbil

trafikk_forsikring = 8.38 * 365 #variabel for årlig trafikkforsikringsavgift: 8.38 pr dag * 365 dager

EL_pr_KM = 0.2 * 2
# variabel for drivstoffkostnad pr km for el-bil: 0.2 kWh pr km * 2 kr pr kWh = 0.4 kr pr KM
bens_pr_KM = 1.0
# variabel for drivstoffkostnad pr km for bensinbil

bom_EL = 0.1 # bomavgift pr KM for el-bil
bom_bens = 0.3 # bomavgift pe KM for bensinbil

#utregning totalkostnad pr år for EL-bil: 
    #legger sammen årlige kostnader, og deretter ganger sammen km kostnader med antall km
tot_EL =  forsikring_EL + trafikk_forsikring + Ant_km*EL_pr_KM + Ant_km*bom_EL

#utregning totalkostnad pr år for bensinbil:
    #legger sammen årlige kostnader, og deretter ganger sammen km kostnader med antall km
tot_bens = forsikring_bens + trafikk_forsikring + Ant_km + bens_pr_KM + Ant_km*bom_bens 

#skriver ut i konsollen  totalkostnad pr biltype, samt tilhørende tekst-strenger
print("årlig avgifter for min kjøring med el-bil = ", tot_EL, "kr")

print("årlige avgifter for min kjøring med bensinbil =", tot_bens, "kr" )

