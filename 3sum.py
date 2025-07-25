nums = [0,0,0,0]

res = []

nums.sort()
print(nums)
for i in range(len(nums)-2):
    if i>0 and nums[i-1] == nums[i]:
        continue
    else:
        
        j = i+1   
        k=len(nums) -1
        while j < k:
            if nums[i] + nums[j] + nums[k] == 0:
                
                res.append([nums[i],nums[j],nums[k]])
                k-=1
                while nums[k+1] == nums[k] and k>j:
                    k-=1
                    
            elif nums[i] + nums[j] + nums[k] >0:
                k -= 1
            
            else:
                print(nums[i],nums[j],nums[k])
                j += 1
print(res)