arr = [100, 200, 300, 350, 400, 401, 402]
k = 3
arr = sorted(arr)
unfairness = arr[-1]
for i in range(len(arr) - k + 1):
    sub_arr = arr[i:i+k]
    if unfairness > max(sub_arr) - min(sub_arr): unfairness = max(sub_arr) - min(sub_arr)
print(unfairness)

