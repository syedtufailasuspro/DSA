from collections import defaultdict
nums = [4,5,0,-2,-3,1]
freq = defaultdict(int)
freq[0] = 1
k = 5
prefix_sum = 0
count = 0


for i in range(len(nums)):
    prefix_sum += nums[i]
    remainder  = prefix_sum % k

    if remainder < 0:
        remainder += k # turn - to  +

    count += freq[remainder]
    
    freq[remainder] += 1

print(freq, count)
