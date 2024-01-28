from itertools import combinations

hlist = []
for i in range(9):
    hlist.append(int(input()))

hlist = sorted(hlist)
hsum = 0

for choose in list(combinations(hlist, 7)):
    choose = list(choose)
    hsum = sum(choose)
    if hsum == 100:
        break

print(*choose, sep='\n')
