#! /usr/local/bin/python3
import sys

def uniquePaths(m, n):
    memo = {}
    return uniquePathsImpl(n-1, m-1, memo)

def uniquePathsImpl(row, col, memo):
    if row < 0 or col < 0:
        return 0
    if row == 0 and col == 0:
        return 1
    if (row, col) in memo:
        return memo[(row, col)]
    
    memo[(row, col)] = uniquePathsImpl(row-1, col, memo) + uniquePathsImpl(row, col-1, memo)
    
    return memo[(row, col)]

def main(argv):
    a = [[0,1,2],[3,4,5]]
    print(a[1][2])
    print(uniquePaths(3,2))
    

if __name__ == "__main__":
    main(sys.argv)