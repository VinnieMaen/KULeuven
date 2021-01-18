# IN DEZE CODE IS ONDERAAN EEN SIMULATIE VAN GEGEVENS GEIMPLEMENTEERD OMDAT DE ORIGINELE GEGEVENS NIET GEGEVEN ZIJN. 
# DEZE CODE IS WAARSCHIJNLIJK NIET 100% CORRECT MAAR KAN EEN BEELD GEVEN OVER DE JUISTE METHODE

def printGegevensOverPeriode(firstDay, lastDay, maxTInWave, minTInWave):
    averageT = 0
    index = -1

    for t in maxTInWave:
        index += 1
        averageT += (t + minTInWave[index])/2
        
    print(f"There was a heatwave in the year {1901 + int(lastDay/365)} with a max temperature of {max(maxTInWave)} and a min temperature of {min(minTInWave)}. The average temperature of the heatwave was {int(averageT/len(maxTInWave))}.")

def zoekHitteGolven(minT,maxT):
    heatWave = False
    minTInWave = []
    maxTInWave = []
    firstDay = 0
    lastDay = 0
    index = -1

    for maxTemp in maxT:
        index += 1
        if maxTemp >= 25:
            if heatWave:
                maxTInWave.append(maxTemp)
                minTInWave.append(minT[index])

            else:
                heatWave = True
                firstDay = index
                maxTInWave.append(maxTemp)
                minTInWave.append(minT[index])

        else:
            if heatWave:
                heatWave = False
                lastDay = index - 1
                counter = 0

                if len(maxTInWave) >= 5:
                    for t in maxTInWave:
                        if t >= 30:
                            counter += 1

                    if counter >= 2:
                        printGegevensOverPeriode(firstDay, lastDay, maxTInWave, minTInWave)
                
                maxTInWave = []
                minTInWave = []

AANTAL_DAGEN = 36500
minimumTemperaturen = [.0]*AANTAL_DAGEN
maximumTemperaturen = [.0]*AANTAL_DAGEN

import random
minimumTemperaturen = []
for i in range(0,AANTAL_DAGEN):
    n = random.randint(1,25)
    minimumTemperaturen.append(n)

maximumTemperaturen = []
for i in range(0,AANTAL_DAGEN):
    n = random.randint(1,10)
    maximumTemperaturen.append(minimumTemperaturen[i] + n)

zoekHitteGolven(minimumTemperaturen, maximumTemperaturen)
