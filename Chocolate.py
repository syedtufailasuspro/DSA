import random

def chocolate(Arr,N,M):
    Arr.sort()
    min_diff = float('+inf')
    for i in range(N-(M-1)):
        if Arr[i+M-1] - Arr[i]<min_diff:
            min_diff = Arr[i+M-1] - Arr[i]
    return min_diff

packets = [3, 4, 1, 9, 56, 7, 9, 12]
N = len(packets)
students = 5

print(chocolate(packets,N,students))





