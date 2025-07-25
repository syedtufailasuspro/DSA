crossword = [
    '++++++-+++',
    '++------++',
    '++++++-+++',
    '++++++-+++',
    '+++------+', 
    '++++++-+-+',
    '++++++-+-+',
    '++++++++-+',
    '++++++++-+',
    '++++++++-+'
    
]
words = 'ICELAND;MEXICO;PANAMA;ALMATY'

def crosswordPuzzle(crossword, words):
    # Write your code here

    def can_place_hor(crossword,word,row,col):
        if len(word) + col > 10:
            return False
        for i in range(len(word)):
            if crossword[row][col + i] not in {'-',word[i]}:
                return False
        if col + len(word) < 10 and crossword[row][col + len(word)] != '+':
            return False
        if col > 0 and crossword[row][col-1] != '+':
            return False
        return True

    def can_place_ver(crossword,word,row,col):
        if len(word) + row > 10:
            return False
        for i in range(len(word)):
            if crossword[row + i][col] not in {'-',word[i]}:
                return False
        if row + len(word)<10 and crossword[row+len(word)][col] != '+':
            return False
        if row > 0 and crossword[row - 1][col] != '+':
            return False
        return True

    def place_hor(crossword, row,col,word):
        positions = []
        for i in range(len(word)):
            if crossword[row][col + i] == '-':
                crossword[row][col + i] = word[i]
                positions.append((row,col+i))
        return positions
    
    def place_ver(crossword,row,col,word):
        positions = []
        for i in range(len(word)):
            if crossword[row + i][col] == '-':
                crossword[row + i][col] = word[i]
                positions.append((row+i,col))
        return positions

    def un_place(crossword, place):
        for i in range(len(place)):
            row = place[i][0]
            col = place[i][1]
            crossword[row][col] = '-'


    def solvecrossword(crossword,words,index):
        if index == len(words):
            return True
        
        word = words[index]
        
        for row in range(10):
            for col in range(10):
                if can_place_hor(crossword,word,row,col):
                    place = place_hor(crossword,row,col,word)
                    if solvecrossword(crossword,words,index + 1):
                        return True
                    un_place(crossword, place)
                
                if can_place_ver(crossword,word,row,col):
                    place = place_ver(crossword,row,col,word)
                    if solvecrossword(crossword,words,index + 1):
                        return True
                    un_place(crossword, place)
        return False
    for i in range(10):
        crossword[i] = list(crossword[i])
    words = words.split(';')    
    
    solvecrossword(crossword,words,0)
    for i in range(10):
        crossword[i] = ''.join(crossword[i])
    return crossword
    
crosswordPuzzle(crossword,words)

for i in range(10):
    print(crossword[i])