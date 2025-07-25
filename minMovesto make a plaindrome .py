
def minMovesToMakePalindrome(string):
    s = list(string)
    left = 0
    right = len(s) - 1
    res = 0
    
    while s:
        elm = s[-1]
        i = s.index(elm)

        if i == len(s) - 1:
            res += len(s)//2
            s.pop()
        else:
            res += i
            s.pop(i)
        
            s.pop()
    return res



print(minMovesToMakePalindrome("abcdabcddacadac"))
