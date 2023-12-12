def f(array2D):
    isTrue=True
    for y in range(len(array2D)):
        sumRow=0
        sumColumn=0
        for x in range(len(array2D)):
            sumRow+=array2D[x][y]
            sumColumn+=array2D[y][x]
        if(sumColumn!=sumRow):
            isTrue=False

    return isTrue

if __name__=="__main__":
    print(f([[3,7,2],[4,2,5],[5,2,1]]))
    print(f([[3,7,2],[4,2,5],[9,2,1]]))