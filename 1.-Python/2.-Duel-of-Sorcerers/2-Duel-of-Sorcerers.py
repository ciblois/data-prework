gandalf = [10, 11, 13, 30, 22, 11, 10, 33, 22, 22]
saruman = [23, 66, 12, 43, 12, 10, 44, 23, 12, 17]

spells = len(gandalf)

results = []

gandalf_wins = 0
saruman_wins=0

for i in range(0,spells):
    if gandalf[i] > saruman[i]:
        results.append("Gandalf")
        gandalf_wins+=1
    elif gandalf[i] < saruman[i]:
        results.append("Saruman")
        saruman_wins+=1
    else:
        results.append("Tie")
#print(results)
print("Gandalf score:",gandalf_wins)
print("Saruman score:",saruman_wins)

if gandalf_wins > saruman_wins:
    print("Gandalf won the battle.")
elif gandalf_wins < saruman_wins:
    print("Saruman won the battle.")
else:
    print("Tie.")

print("Bonus")

POWER = {
    'Fireball': 50, 
    'Lightning bolt': 40, 
    'Magic arrow': 10, 
    'Black Tentacles': 25, 
    'Contagion': 45
}

gandalf = ['Fireball', 'Lightning bolt', 'Lightning bolt', 'Magic arrow', 'Fireball', 
           'Magic arrow', 'Lightning bolt', 'Fireball', 'Fireball', 'Fireball']
saruman = ['Contagion', 'Contagion', 'Black Tentacles', 'Fireball', 'Black Tentacles', 
           'Lightning bolt', 'Magic arrow', 'Contagion', 'Magic arrow', 'Magic arrow']

gandalf_wins = 0
saruman_wins=0
sequence_wins = []

gandalf_power = []
saruman_power = []
tie = []

for i in range(0, spells):
    x = POWER[gandalf[i]]
    y = POWER[saruman[i]]
    gandalf_power.append(x)
    saruman_power.append(y)
    if x > y:
        gandalf_wins+=1
        sequence_wins.append("Gandalf")
    elif x < y:
        saruman_wins+=1
        sequence_wins.append("Saruman")
    else:
        tie[i]+=1
        sequence_wins.append("Tie")

#print(gandalf_power)
#print(saruman_power)
#print(sequence_wins)
#print(gandalf_wins)
#print(saruman_wins)
#print(tie)

for i in range(0,spells):
    try:
        a = sequence_wins[i]
        b = i+1
        c = sequence_wins[b]
        d = i + 2
        e = sequence_wins[d]
        if (a == c) & (c == e):
            print("The winner of the battle is",sequence_wins[i])
            break
        else:
            pass
    except:
        break
    
average_gandalf = sum(gandalf_power)/len(gandalf_power)
average_saruman = sum(saruman_power)/len(saruman_power) 
print("The average of Gandalf spells is",average_gandalf)
print("The average of Saruman spells is",average_saruman)

import statistics
print("The standart deviation of Gandalf spells is",statistics.stdev(gandalf_power))
print("The standart deviation of Saruman spells is",statistics.stdev(saruman_power))