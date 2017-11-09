def update(queen, row):
    for i in range(0,8,1):
        queen[row] = i
        if find_elements(queen, row):
            if row == 7:
                print(queen)
                globals()["solutions"] = globals()["solutions"] + 1
            else:
                update(queen, row+1)
            
def find_elements(queen, row):
    c = 0
    result = True
    for i in range(0,row,1):
        c = c+1
        current = queen[row]
        other = queen[row-i-1]
        if (current == other) or (current-c == other) or (current+c == other):
            result = False
            break
    return(result)

globals()["solutions"] = 0
queen = [4,4,4,4,4,4,4,4]

for i in range(0,8,1):
    queen[0] = i
    update(queen, 1)

print("\nNumber of solutions:",solutions)
