def mergeOverlap(arr):
    nums = arr[:]
    final = []
    nums.sort()
    new = nums[0]
    
    
    for i in range(1,len(nums)):
        if nums[i][0]<=new[1]:
            if i<len(nums)-1:
                new = [new[0] ,max(new[1], nums[i][1])]
            else:
                new = [new[0] ,max(new[1], nums[i][1])]
                final.append(new)
        else:
            if i<len(nums)-1:
                
                final.append(new)
                new = nums[i]
            else:
                final.append(new)
                new = nums[i]
                final.append(new)
    return final

arr = [[1,0],[6,11]]

print(mergeOverlap(arr))