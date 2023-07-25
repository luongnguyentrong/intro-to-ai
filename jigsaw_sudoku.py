import time

map1 = [
    [[0, 0], [0, 1], [0, 2], [0, 3], [1, 1]],
    [[1, 0], [2, 0], [3, 0], [4, 0], [2, 1]],
    [[0, 4], [1, 4], [1, 3], [1, 2], [2, 2]],
    [[3, 1], [3, 2], [4, 1], [4, 2], [4, 3]],
    [[2, 3], [2, 4], [3, 3], [3, 4], [4, 4]]
]
S1 = [
    [0, 1, 5, 0, 0],
    [0, 2, 0, 0, 0],
    [5, 0, 0, 0, 3],
    [0, 0, 0, 4, 0],
    [0, 0, 4, 1, 0]
]
map2 = [
    [[0, 0], [1, 0], [2, 0], [3, 0], [3, 1], [2, 1], [1, 1]],
    [[0, 1], [0, 2], [0, 3], [1, 3], [1, 2], [2, 2], [3, 2]],
    [[0, 4], [0, 5], [0, 6], [1, 6], [2, 6], [1, 5], [1, 4]],
    [[2, 3], [2, 4], [2, 5], [3, 5], [3, 6], [4, 6], [5, 6]],
    [[6, 6], [6, 5], [6, 4], [6, 3], [5, 3], [5, 4], [5, 5]],
    [[6, 0], [6, 1], [6, 2], [5, 2], [5, 1], [5, 0], [4, 0]],
    [[4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [3, 4], [3, 3]]
]
S2 = [
    [0, 0, 4, 3, 0, 0, 0],
    [0, 7, 0, 0, 0, 0, 5],
    [4, 0, 7, 0, 3, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 0, 5, 0, 4],
    [3, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 7, 2, 0, 0],
]
map3 = [
    [[0, 0], [0, 1], [1, 0], [1, 1], [1, 2], [2, 0], [3, 0], [4, 0], [5, 0]],
    [[6, 0], [7, 0], [8, 0], [8, 1], [8, 2], [8, 4], [8, 3], [7, 3], [7, 2]],
    [[3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [6, 2], [5, 2], [5, 3], [6, 3]],
    [[8, 8], [8, 7], [8, 6], [8, 5], [7, 5], [7, 4], [6, 4], [6, 5], [6, 6]],
    [[7, 8], [7, 7], [7, 6], [6, 8], [6, 7], [5, 7], [5, 6], [5, 5], [5, 4]],
    [[5, 8], [4, 8], [3, 8], [2, 8], [1, 8], [0, 8], [2, 7], [2, 6], [3, 7]],
    [[0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [1, 7], [1, 6], [1, 4]],
    [[1, 3], [2, 3], [2, 2], [2, 1], [3, 2], [4, 2], [4, 3], [3, 3], [3, 4]],
    [[2, 4], [2, 5], [1, 5], [3, 5], [3, 6], [4, 7], [4, 6], [4, 5], [4, 4]]
]
S3 = [
    [0, 0, 0, 0, 8, 9, 0, 0, 0],
    [2, 0, 0, 0, 0, 0, 7, 0, 0],
    [0, 0, 0, 3, 0, 2, 0, 0, 0],
    [0, 8, 0, 0, 0, 0, 4, 0, 0],
    [0, 0, 0, 8, 7, 6, 0, 0, 0],
    [0, 0, 6, 0, 0, 0, 0, 4, 0],
    [0, 0, 0, 7, 0, 3, 0, 0, 0],
    [0, 0, 2, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 9, 4, 0, 0, 0, 0]
]
map4 = [
    [[0, 0], [0, 1], [1, 1], [1, 0], [1, 2]],
    [[2, 0], [2, 1], [3, 0], [4, 0], [4, 1]],
    [[0, 2], [0, 3], [0, 4], [1, 4], [2, 4]],
    [[3, 4], [3, 3], [4, 4], [4, 2], [4, 3]],
    [[1, 3], [2, 3], [2, 2], [3, 2], [3, 1]]
]
S4 = [
    [3, 0, 0, 0, 0],
    [0, 0, 0, 4, 0],
    [0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0],
    [0, 0, 0, 0, 1]
]
map5 = [
    [[0 , 0], [0 , 1], [0 , 2], [0 , 3], [0 , 4], [1 ,4 ], [1 , 5]],
    [[3 , 0], [2 , 0], [1 , 0], [1 , 1], [1 , 2], [1 , 3], [2 , 3]],
    [[2 , 1], [2 , 2], [3 , 1], [3 , 2], [3 , 3], [3 , 4], [4 , 2]],
    [[4 , 0], [4 , 1], [5 , 0], [5 , 1], [6 , 0], [6 , 1], [6 , 2]],
    [[5 , 2], [5 , 3], [6 , 3], [6 , 4], [6 , 5], [6 , 6], [5 , 5]],
    [[5 , 4], [4 , 3], [4 , 4], [4 , 5], [3 , 5], [2 ,5 ], [2 , 4]],
    [[0 , 5], [0 , 6], [1 , 6], [2 , 6], [3 , 6], [4 , 6], [5 , 6]]
]
S5 = [
    
    [2, 3, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [1, 4, 0, 0, 0, 0, 5],
    [0, 0, 0, 3, 0, 0, 0],
    [7, 0, 0, 0, 0, 4, 3],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 7, 6]
]
map6 = [
    [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [1, 1], [1, 2], [1, 3]],
    [[1, 0], [2, 0], [3, 0], [2, 1], [2, 2], [3, 1], [3, 2], [4, 1], [4, 2]],
    [[4, 0], [5, 0], [5, 1], [5, 2], [5, 3], [6, 2], [7, 2], [7, 3], [7, 4]],
    [[6, 0], [6, 1], [7, 0], [7, 1], [8, 0], [8, 1], [8, 2], [8, 3], [8, 4]],
    [[2, 3], [3, 3], [3, 4], [4, 3], [4, 4], [5, 4], [6, 3], [6, 4], [6, 5]],
    [[8, 8], [8, 7], [7, 8], [7, 7], [8, 6], [8, 5], [7, 6], [7, 5], [6, 6]],
    [[6, 8], [6, 7], [5, 8], [5, 7], [4, 7], [4, 8], [4, 6], [5, 6], [5, 5]],
    [[4, 5], [3, 5], [3, 6], [2, 7], [2, 6], [2, 5], [2, 4], [1, 4], [1, 5]],
    [[0, 6], [0, 7], [0, 8], [1, 6], [1, 7], [1, 8], [2, 8], [3, 8], [3, 7]]
]
S6 = [
    [0, 5, 2, 8, 7, 3, 0, 6, 0],
    [0, 4, 0, 0, 0, 0, 0, 0, 0],
    [0, 6, 0, 0, 3, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 3],
    [8, 0, 0, 0, 0, 0, 0, 0, 6],
    [2, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 9, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 4, 0],
    [0, 3, 0, 4, 2, 5, 7, 8, 0]
]
def find_in_map(local, map):
    leng = len(map)
    for i in range(leng):
        for j in range(leng):
            if (map[j][i][0] == local[0]) and (map[j][i][1] == local[1]):
                return j, i


def in_sudoku(s, map):

    leng = len(s)
    for d in range(leng):
        print('----', end='')
    print('')
    for d in range(leng):
        print(end=' ')
        for c in range(leng):
            if c < leng - 1:
                x, o = find_in_map([d, c], map)
                y, k = find_in_map([d, c+1], map)
                if x != y:
                    a = s[d][c] if s[d][c] != 0 else ' '
                    print(a, '| ', end="")
                else:
                    a = s[d][c] if s[d][c] != 0 else ' '
                    print(a, '  ', end="")
            else:
                a = s[d][c] if s[d][c] != 0 else ' '
                print(a, "|")
        for c in range(leng):
            if d < leng - 1:
                x, o = find_in_map([d, c], map)
                y, k = find_in_map([d+1, c], map)
                if x != y:
                    print('--- ', end="")
                else:
                    print('    ', end="")
            else:
                print('----', end="")
        print("")



def find_zero_s(s):
    leng = len(s)
    for x in range(leng):
        for y in range(leng):
            if s[x][y] == 0:
                return x, y
    return None

def minGroup(s, map):
    leng = len(map)
    min = leng
    re = []
    for x in range(leng):
        a=b=c=0
        arr= []
        brr=[]
        crr= []
        for y in range(leng):
            if a< min and s[map[x][y][0]][map[x][y][1]] == 0:
                a +=1
                arr.append(map[x][y])
            if b< min and s[x][y] == 0:
                b +=1
                brr.append([x,y])
            if c<min and s[y][x] == 0:
                c +=1
                crr.append([y,x])
        if a>0 and a < min: 
            min = a
            re = arr
        if b> 0 and b < min: 
            min = b
            re = brr
        if c>0 and c < min: 
            min = c
            re = crr   
        if min ==1:
            break    
    return re



def ListOfCase(s, map, x, y):
    # print('check:',x,y,vals)
    leng = len(map)
    row = 0
    for i in range(leng):
        for j in range(leng):
            if map[i][j] == [x, y]:
                row = i
    re = []
    for val in range(1, 1+leng):
        ck = True
        for i in range(leng):
            a = map[row][i][0]
            b = map[row][i][1]
            if (s[i][y] == val) or (s[x][i] == val) or s[a][b] == val:
                ck = False
                break
        if ck:
            re.append(val)
    return re


def DFS_JIGSAW_SUDOKU(s, map, result):
    found = find_zero_s(s)
    if not found:
        return True
    else:
        x, y = found
    a = ListOfCase(s, map, x, y)
    for i in a:
        s[x][y] = i
        # print('=> add [',x,y,'] = ',i)
        result.append([x, y, i])
        if DFS_JIGSAW_SUDOKU(s, map, result):
            return True
        else:
            result.remove([x, y, i])
            # print('=> move [',x,y,'] = ',i)
            s[x][y] = 0
    return False
def Heuristic_JIGSAW_SUDOKU(s, map, result, list):
    if list == []:
        list = minGroup(s,map)
    if list == []:
        return True
    else:
        [x,y] =list[0]
        a = ListOfCase(s, map, x,y)
        list = list[1:]
        for i in a:
            s[x][y] = i
            # print('=> add [',x,y,'] = ',i)
            result.append([x, y, i])
            if Heuristic_JIGSAW_SUDOKU(s, map, result, list):
                return True
            else:
                result.remove([x, y, i])
                # print('=> move [',x,y,'] = ',i)
                s[x][y] = 0
    return False

if __name__ == '__main__':
    
    result = []
    s = [ S1 , S4 , S2 , S5 , S3 , S6 ]
    map = [ map1 , map4 , map2 , map5 , map3 , map6 ]
    x = int(input("1. 5x5\n2. 5x5\n3. 7x7\n4. 7x7\n5. 9x9\n6. 9x9\nPlease typing number test: "))
    while x<1 or x > len(s):
        x =int(int(input("Typing again number test(ex: 1,2,3,4,5,6.): ")))
    if x > 0 and x <= len(s):
        re = []
        in_sudoku(s[x-1], map[x-1])
        
        b = int(input("1. BFS \n2. Heuristic \n"))
        while b<1 or b>2:
            b = int(input("1. BFS \n2. Heuristic \n"))
        
        start = time.time()
        if b == 1:
            DFS_JIGSAW_SUDOKU(s[x-1], map[x-1], re)
            print('BFS ',end='')
        else:
            Heuristic_JIGSAW_SUDOKU(s[x-1], map[x-1], re,[])
            print('Astar ',end='')
        end = time.time()
        
        print('step by step [ row, column, value]: ',re)
        print('Solution: ')
        in_sudoku(s[x-1], map[x-1])

    
    print('Run time: ',end - start)
