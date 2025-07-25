def characterReplacement(s, k) -> int:
    result = 0
    left = 0
    right = 0
    seti = set(s)
    final_sub = ''
    count_dic = dict.fromkeys(seti, 0)
    print(count_dic)
    for right in range(len(s)):
        length = right+1 - left
        count_dic[s[right]] +=1
        most_freq = max(count_dic.values())
        print(most_freq)
        formula = length - most_freq
        if formula<=k:
            result = max(result,length)
        else:
            left = left+1
    return result







s='ABBB'
k=1
print(characterReplacement(s,k))