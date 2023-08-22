from operator import itemgetter
records = [["Harry", 37.21], ["Berry", 37.21], ["Tina", 37.2], ["Akriti", 41], ["Harsh", 39]]
    
records = sorted(records, key=itemgetter(1))
lowest = records[0][1]
end = len(records)
i = 0
while end > i:
    if records[0][1] == lowest: records.pop(0)
    i += 1
sec_lowest = records[0][1]
records = sorted(records, key=itemgetter(0))

for item in records:
    if item[1] == sec_lowest: print(item[0])
