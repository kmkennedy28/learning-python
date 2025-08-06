import random

numberStreaks = 0
numberExperiments = 10000

for experiment_number in range(numberExperiments):  # Run 10,000 experiments 

    #holds heads/tails values
    results = []

    #list of 100 H or T
    for i in range(100):
        val = random.randint(0,1)
        if val == 0:
            results.append('H')
        elif val == 1:
            results.append('T')

    # Code that checks if there is a streak of 6 heads or tails in a row
    streak = 0
    for i in range(1, 100):
        #if the value matches the next one adds to the streak
        if results[i] == results[i-1]:
            streak += 1
            #once the streak is 6 add one to the count
            if streak == 6:
                numberStreaks += 1
                streak = 0
                break
        else:
            streak = 0

#print result
print('Chance of streak: %s%%' % (numberStreaks / (numberExperiments) * 100))