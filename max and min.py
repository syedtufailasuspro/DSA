def set_mini(input):
    k = 999
    for i in input:
        if i<k:
            k=i
    return k

def set_max(input):
    k = -999
    for i in input:
        if i>k:
            k=i
    return k

input= [1,5,6,8]

print(set_max(input))