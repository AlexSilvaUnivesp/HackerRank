a = [3, 2, 1]

totalSwaps = 0
for i in range(len(a)):
    roundSwaps = 0
    for j in range(len(a)-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            roundSwaps += 1
            totalSwaps += 1
    if roundSwaps == 0: break

    
print(f'Array is sorted in {totalSwaps} swaps')
print(f'First Element: {a[0]}')
print(f'Last Element: {a[-1]}')
