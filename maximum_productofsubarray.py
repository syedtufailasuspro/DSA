
def maxProduct(nums):
    pro = nums[0]   # 2, -5 , -2 , -6
    neg_pro = nums[0]
    max_pro = nums[0]
    print(pro,neg_pro)
    for i in range(1, len(nums)):
        if nums[i] < 0:
            pro, neg_pro = neg_pro, pro  # Swap when encountering a negative number
            print(pro,neg_pro)
        pro = max(nums[i], pro * nums[i])
        neg_pro = min(nums[i], neg_pro * nums[i])
        
        print(pro,neg_pro)

        max_pro = max(max_pro, pro)
    
    return max_pro

nums = [0,0,0,2]
print(maxProduct(nums))