from collections import defaultdict

  
database = ["hybibdsaf www.google.com 0",
"iiasdisd www.leetcode.com 1",
"asdasf www.golu.com 0"
]

request = ["hybibdsaf",
"hybibdsaf",
"iiasdisd"
]

#   return ["www.google.com 1", "www.google.com 2", "www.golu.com 3"]   {}
    

def ret_url_usercount(database, request):
    res = []
    dic = dict()
    user = dict() 
    count = defaultdict(int)

    for i in range(len(database)):
        string = database[i]
        database[i] = string.split(" ")
    print(database)

    for i in range(len(database)):
        dic[database[i][0]] = database[i][1]
        user[database[i][0]] = database[i][2]
    print(dic)

    for i in range(len(request)):
        short = request[i]
        actual = dic[short]

        count[user[short]] += 1

        out = actual + " " + f"{count[user[short]]}"
        res.append(out)
    return res

    


print(ret_url_usercount(database,request))