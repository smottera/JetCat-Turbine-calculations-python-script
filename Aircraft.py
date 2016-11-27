#jetcat P300RX
engineThrust = 30.590269 #Kilograms
SamuWeight = 75 #Kilograms
engineWeight = 2.630 #Kilograms
fuelTankWeight = 10 #Kilograms
aircraftWeight = 10 #Kilograms , includes servos, aluminium body, battery
netWeight = SamuWeight+engineWeight*4 + fuelTankWeight +aircraftWeight
netThrust = engineThrust*4
netForce = netThrust-netWeight
twRatio = netThrust/netWeight

print("Engine Output:",netThrust,'Kilograms')
print("Weight of everything:",netWeight,"Kilograms")
print("Remaining Force:",netForce,"Kilograms")
print("T/W ratio: ",twRatio)

#Fuel consumption
density = 0.840 #Kilogram/L Kerosene
consumption = 0.98 #litre/minute
consumption_s = consumption / 60.00 #per second
tenMinFlightConsumption = 4 * 3 * 0.98
print("10 Minute Flight:", tenMinFlightConsumption, "L")
weightF = tenMinFlightConsumption * density
print("Weight of Fuel in Kg:", weightF)
