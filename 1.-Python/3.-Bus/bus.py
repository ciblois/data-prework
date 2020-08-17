# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 18:05:29 2020

@author: Cinthya Blois
"""

#bus_stop = (in, out)

# Variables
stops = [(10, 0), (4, 1), (3, 5), (3, 4), (5, 1), (1, 5), (5, 8), (4, 6), (2, 3)]
stops_list = []

#print(stops[0])
#print(stops[1][0])

print(len(stops))

passengers_in = map(lambda x: x[0], stops)
passengers_in = list(passengers_in)
passengers_out = map(lambda x: x[1], stops)
passengers_out = list(passengers_out)

passengers = []

for i in range(0, len(passengers_in)):
    x = passengers_in[i] - passengers_out[i]
    passengers.append(x)

passengers_stops = []
fisrt_stop = passengers_in[0] - passengers_out[0]
passengers_stops.append(fisrt_stop)

for i in range(1,len(passengers)):
#while i < len(passengers):
    try:
        x = passengers_stops[i-1] + passengers[i]
        passengers_stops.append(x)
    except:
        break

#print(passengers_in)
#print(passengers_out)
#print(passengers)
print(passengers_stops)

print("The maximum occupation of the bus is", max(passengers_stops))
average = sum(passengers_stops)/len(passengers_stops)
print("The average occupation is", average)
import statistics
print("The standart deviation is", statistics.stdev(passengers_stops))