#Albert
#Magic Square

def fillSquare(n, sqArr):
    '''
    This procedure prompts the user for n^2 inputs to populate a
    2D square array which has alreay been declared
    precondition:  sqArr has been declared with a size of nxn
    '''

    #note: I could have used len(sqArr) instead of passing n in as a parameter
    # but I thought it would be easier for you to understand if it was passed...
    for r in range(n):
        print("----ROW " + str(r + 1) + "----")
        for c in range(n):
            sqArr[r][c] = int(input("Enter value: "))
    

def printSquare(n, sqArr):
    '''
    This procedure "pretty" prints a 2D square array of size n
    '''
    for r in range(n):
        for c in range(n):
            print(sqArr[r][c], end="\t")
        print("\n")
    
def checkRow(n, sqArr, mNum):
    
#This procedure will return true if every row of sqArr has a sum of mNum
    

    
    for row in sqArr:
        row_sum = 0

        for column in row:
            row_sum = row_sum + column
        
        if mNum != row_sum:
            return False
                
    return True

def checkCol(n, sqArr, mNum):
     
#This procedure will return true if every column of sqArr has a sum of mNum

    
    for column in range(n):

        col_sum = 0
    
        for row in range(n):
            col_sum = col_sum + sqArr[row][column]

        if mNum != col_sum:
            return False

    
    return True

def checkDiag1(n, sqArr, mNum):
    '''
    This procedure will return true if diagonal(left to right) of sqArr has
    a sum of mNum
    '''
    sum_diag = 0

    for row in range(n):
        sum_diag = sum_diag + sqArr[row][row]
        
    if mNum != sum_diag:
        return False

        
    return True

def checkDiag2(n, sqArr, mNum):
    '''
    This procedure will return true if diagonal(right to left) of sqArr has
    a sum of mNum
    '''
    
    sum_diag = 0
    count = n - 1

    for row in range(n):
        sum_diag = sum_diag + sqArr[row][count]
        count = count - 1
        

        
    if mNum != sum_diag:
        return False
    
    return True

def checkUnique(n, sqArr):
    '''
    This procedure will return true if each number in the 2D arrary is unique,
    meaning there are no repeating numbers.
    '''
    check = []
    
    for row in sqArr:

        for column in row:

            if column in check:
                return False
                
            else:
                check.append(column)
          
    return True

def checkSquare(size, square):
    '''
    Returns True if inputed square is magic, and False if not.
    '''
    magicNum = size * (size ** 2 + 1) / 2

    if(checkRow(size, square, magicNum) and  \
       checkCol(size, square, magicNum) and  \
       checkDiag1(size, square, magicNum) and  \
       checkDiag2(size, square, magicNum) and   \
       checkUnique(size, square)):
       return True
    else:
       return False



# ---MAIN---
s = int(input("Enter square side length:  "))
sq = [[0 for x in range(s)] for y in range(s)]
fillSquare(s, sq)

'''
if you get tired of typing in the square multiple times,
for testing purposes, you may want to comment out the 3 lines above and
uncomment the 2 lines below.  It will make your testing life *much* easier :)
'''
#s = 3
#sq = [[2,7,6], [9,5,1], [4,3,8]]

printSquare(s, sq)
print(checkSquare(s, sq))
