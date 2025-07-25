arr = [-10,-2,-5,-1]
sum = arr[0]
max_sum = arr[0]
for i in range(1,len(arr)):
    if sum<0 :
            sum = 0
    sum+= arr[i]
    max_sum  = max(sum,max_sum)
        
    

print(arr)
print(max_sum)