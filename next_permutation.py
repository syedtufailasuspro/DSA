from typing import List
class Solution:
    def nextPermutation(self, arr: List[int]) -> None:
        for i in range(len(arr) -1 , -1 , -1):
            if i == 0:
                arr.sort()
                break
            if arr[i-1] < arr[i]:
                j = len(arr) - 1
                while arr[j] <= arr[i-1]:
                    j -= 1
                arr[i-1],arr[j] = arr[j],arr[i-1]
                arr[i:] = sorted(arr[i:])
                break
            
              
        