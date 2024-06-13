# Exercise1_get_max_over_kernel
k = 3
num_list = [3,4,5,1,-44,5,10,12,33,1]
result = []
for i in range(len(num_list) + 1 - k):
    result.append(max(num_list[i:i+k]))

print(result)