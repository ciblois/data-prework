print("Exercise 1")

days=0
well_height = 125
daily_distance = 30
nightly_distance = 20
snail_position = 0

while snail_position <= well_height:
    if snail_position < well_height:
        pass
    snail_position+=daily_distance-nightly_distance
    days+=1
else:
    print("The snail take", days, "days to get out.")
    
print("Bonus 1")
snail_position = 0
advance_cm = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]
#i=0
displacement = []

for i in range(0,10):
    displacement.append(advance_cm[i]-nightly_distance)
    if snail_position <= well_height:
        snail_position += advance_cm[i]-nightly_distance
    else:
        break
print("The snail take", i, "days to get out.")
#print(displacement)
print("The maximum displacement is",max(displacement))
print("The minimum displacement is",min(displacement))

average = sum(displacement)/len(displacement)
print("The average progress is",average)

import statistics
print("The standart deviation is",statistics.stdev(displacement))
