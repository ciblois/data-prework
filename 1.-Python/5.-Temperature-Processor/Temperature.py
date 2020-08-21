# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 12:49:03 2020

@author: Cinthya Blois
"""

temperatures_C = [33, 66, 65, 0, 59, 60, 62, 64, 70, 76, 80, 81, 80, 83, 90, 79, 61, 53, 50, 49, 53, 48, 45, 39]

#temperatures_C[0] == 00am
#print(len(temperatures_C))

min_temp_day = min(temperatures_C)
max_temp_day = max(temperatures_C)
print("The minimum temperature of the day was",min_temp_day,"ºC and the maximum was",max_temp_day,"ºC.")
#Any temperature is above 80ºC
if max_temp_day >80:
    print("The cooling system needs to be change bacause it was registered temperature above 80ºC.")
else:
    print("The cooling system is ok because it was not registered temperature above 80ºC.")

high_temperatures = []

for i in range(0,len(temperatures_C)):
    x = temperatures_C[i]
    if x >= 70:
        high_temperatures.append(x)
    else:
        pass

print("It was registered",len(high_temperatures),"temperatures greater than or equal to 70ºC.")

#More than 4 temperatures are greater than or equal to 70ºC
if len(high_temperatures) > 4:
    print("So the cooling system needs to be replaced for a new one.")
else:
    print("The cooling system is ok.")

average_temperature = sum(temperatures_C)/len(temperatures_C)
#print("The average temeprature in this day was",average_temperature)

#The average temperature exceeds 65ºC
if average_temperature > 65:
    print("the cooling system needs to be replaced for a new one, beacuse of the average temperature was",average_temperature)
else:
    print("The average temperature wasn't above 65ºC, so the cooling system is ok.")

#Considering the value 0 as a missing recorded.

for i in range(0,len(temperatures_C)):
    x = temperatures_C[i]
    if x == 0:
        temperatures_C[i] = 23
        print("The temperature record was missing at",i,"o'clock and it was placed for room temperature of 23ºC.")
    else:
        pass

#-------------------------------------------------------------------------------------------------------------------
#another way is using dictionary
list_time = []

for i in range(0,24):
    list_time.append(i)

time_temperature = dict(zip(list_time,temperatures_C))
#print(time_temperature)

#print(time_temperature.items())
#print(time_temperature.keys())
#print(time_temperature.values())

# function to return key for any value 
def get_key(val): 
    for key, value in time_temperature.items(): 
         if val == value: 
             return key 
  
    return "key doesn't exist"

for i in range(0,24):
    if 0 in time_temperature.values():
        x = get_key(i)
        time_temperature.update({x: '23'}) #room temperature
        print("The temperature record was missing at",x,"o'clock and it was placed for room temperature of 23ºC.")
    else:
        pass

#print(time_temperature)
#print(time_temperature.get(3,"ok"))

high_temperatures_consec = []

for i in range(0,len(temperatures_C)):
    try:
        number_1 = temperatures_C[i]
        a = i+1
        number_2 = temperatures_C[a]
        b = i+2
        number_3 = temperatures_C[b]
        c = i+3
        number_4 = temperatures_C[c]
        if (number_1 > 70) & (number_2 > 70) & (number_3 > 70) & (number_4 > 70):
            x = 0 #0 means yes for the consecutive
            high_temperatures_consec.append(x)
        else:
            pass
    except:
        break

if (max_temp_day > 80) | (len(high_temperatures_consec) > 0) | (average_temperature > 65):
    print("The cooling system needs to be change.")
else:
    print("The cooling system is ok.")

#same exercise but in Fahrenheit
print("Analysing the same after convert Celsius in Fahrenheit:")
temperatures_C = [33, 66, 65, 0, 59, 60, 62, 64, 70, 76, 80, 81, 80, 83, 90, 79, 61, 53, 50, 49, 53, 48, 45, 39]
temperatures_F = []

for i in range(0,len(temperatures_C)):
    C = temperatures_C[i]
    F = (C*1.8)+32
    temperatures_F.append(F)

#print(temperatures_F)

F_80 = 80*1.8 + 32
F_70 = 70*1.8 + 32
F_65 = 65*1.8 + 32
F_zero = 0*1.8+32
F_room = 23*1.8+32

min_temp_day = min(temperatures_F)
max_temp_day = max(temperatures_F)
print("The minimum temperature of the day was",min_temp_day,"ºF and the maximum was",max_temp_day,"ºF.")

if max_temp_day > F_80:
    print("The cooling system needs to be change bacause it was registered temperature above.",F_80,"ºF.")
else:
    print("The cooling system is ok because it was not registered temperature above.",F_80,"ºF.")

high_temperatures_F = []

for i in range(0,len(temperatures_F)):
    x = temperatures_F[i]
    if x >= F_70:
        high_temperatures_F.append(x)
    else:
        pass

print("It was registered",len(high_temperatures_F),"temperatures greater than or equal to",F_70,"ºF.")
if len(high_temperatures_F) > 4:
    print("So the cooling system needs to be replaced for a new one.")
else:
    print("The cooling system is ok.")

average_temperature_F = sum(temperatures_F)/len(temperatures_F)
#print("The average temeprature in this day was",average_temperature)
if average_temperature > F_65:
    print("the cooling system needs to be replaced for a new one, beacuse of the average temperature was",average_temperature_F,"ºF.")
else:
    print("The average temperature wasn't above",F_65,"ºF so the cooling system is ok.")

#Considering the value 0ºC as a missing recorded.

for i in range(0,len(temperatures_F)):
    x = temperatures_F[i]
    if x == F_zero:
        temperatures_F[i] = F_room
        print("The temperature record was missing at",i,"o'clock and it was placed for room temperature of",F_room,"ºF.")
    else:
        pass