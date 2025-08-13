arr = [4,3,5]
string = "PNPx"
n = 3

res = 0
for i in range(n):
    if string[i] == 'P':
        res += arr[i] 
    elif string[i] == 'N':
        res += -arr[i]

print(abs(res) * 100) 