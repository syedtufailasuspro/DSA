def nextPeru(nums):
    N = len(nums) #length of nums
    pivot = -1 #last elemnt
    for i in range(N-2,-1,-1):
        if nums[i]<nums[i+1]:
            pivot = i
            k=N-1
            while(k>0):
                if nums[k]>nums[pivot]:
                    nums[k] , nums[pivot] = nums[pivot] , nums[k]
                    break
                k-=1
            nums[pivot+1:] = reversed(nums[pivot+1:])
            break
    else:
        nums.sort()


nums = [0,3,2,1]
nextPeru(nums)
print(nums)

