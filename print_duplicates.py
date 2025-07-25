from collections import defaultdict

def print_duplicates(str):
    count = defaultdict(int)
    for i in range(len(str)):
        count[str[i]] += 1  #effeicent
    for i in count.keys():
        if count[i] > 1:
            print(f"{i} : {count[i]}")



# Example usage
str = 'gogo'
print_duplicates(str)