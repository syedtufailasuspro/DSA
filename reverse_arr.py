def rev(arr):
    arr.reverse()
    return arr

def rev2(arr):
    list =[]
    for i in range(len(arr)-1,-1,-1):
        list.append(arr[i])
    return list

arr=[1,3,2,5,8,4,3]
i = float('inf')
print(rev(arr))
print(10000000000<i)
