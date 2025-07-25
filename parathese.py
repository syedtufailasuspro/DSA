
def isValid(s: str) -> bool:
    for i in range(len(s)):
        if '()' in s:
            s=s.replace('()','')
        elif '{}' in s:
            s=s.replace('{}','')
        elif '[]' in s:
            s=s.replace('[]','')
    return len(s)==0

print(isValid('({(())})'))
    