import random

random.seed()

print("punkt a")
print(random.random()) 

print("punkt b")
if ("trefl" in random.sample(["trefl", "inna"], counts=[13, 39], k=3))==True:
    print("wylosowany trefl")
else:
    print("wylosowana inna karta niż trefl")

print("punkt c")
i=0 #ilość wylosowanych trefli
j=0 #ilość losowań
k=0.0 #prawdopodobieństwo 

while (k<0.413 or k>0.414):
    j+=1
    if ('trefl' in random.sample(['trefl', 'inna'], counts=[13, 39], k=3))!=True:
        i+=1
    k=i/j

print("otrzymano oczekiwane prawdopodobieństo po", j, "losowaniach")