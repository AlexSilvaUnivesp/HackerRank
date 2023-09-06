def merge_the_tools(string, k):
    m = int(len(string) / k)
    substring = [''] * m
    for i in range(m):
        temp = string[i*k:i*k+k]
        for j in range(len(temp)):
            if temp[j] not in substring[i]:
                substring[i] += temp[j] 
        print(substring[i])

string = 'AAABCADDE'
k = 3

merge_the_tools(string, k)