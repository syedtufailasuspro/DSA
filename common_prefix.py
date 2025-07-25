def longestCommonPrefix(strs) -> str:
        max_string = ''
        strs.sort()
        print(strs) 
        first = strs[0]
        last = strs[-1]
        for i in range(len(first)):
            if first[i]==last[i]:
                max_string +=first[i]
            else:
                break
        return max_string
print(longestCommonPrefix(["flower","flowerfgsfgsfisfd","flight",]))