gandalf = [10, 11, 13, 30, 22, 11, 10, 33, 22, 22]
saruman = [23, 66, 12, 43, 12, 10, 44, 23, 12, 17]

results = []

gandalf_wins = 0
saruman_wins=0

print("Let's assuming that they can choose which spell they want to use. So we can explore all the combinations possible.")

for i in range(0,10):
    for y in range(0,10):
        if gandalf[i] > saruman[y]:
            results.append("Gandalf")
            gandalf_wins+=1
        elif gandalf[i] < saruman[y]:
            results.append("Saruman")
            saruman_wins+=1
        else:
            results.append("Tie")
#print(results)
spells = len(results)
print(spells)

print("Gandalf score:",gandalf_wins)
print("Saruman score:",saruman_wins)

if gandalf_wins > saruman_wins:
    print("Gandalf won the battle.")
elif gandalf_wins < saruman_wins:
    print("Saruman won the battle.")
else:
    print("Tie.")