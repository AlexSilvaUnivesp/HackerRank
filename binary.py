n = 5
cons, maxcons = 0, 0
binary = bin(n)[2:]
for i in binary:
    if i == '1':
        cons += 1
        if cons > maxcons: maxcons = cons
    else:
        cons = 0
print(maxcons)