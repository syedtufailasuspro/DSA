arr = [11, 15,6, 8, 9, 10]
target = 19

def pair_sum(arr,target):
    maxi = max(arr)
    mini = min(arr)
    n = len(arr)
    L = arr.index(maxi)  
    S = arr.index(mini)  

    print(arr)
    check = False

    while arr[L]!=arr[S] : 
        sum_pair = arr[L] + arr[S]

        if sum_pair == target:
            check = True
            print(arr[L] , arr[S])
            break
        elif sum_pair > target:
            print(arr[L] , arr[S],'big')
            L = (L - 1) % n
        else:
            print(arr[L] , arr[S])
            S = (S + 1) % n
    return check

print(pair_sum(arr,target))

        
        
