# runtime O(mn)
# m is the length of first string 
# n is the length of second string
def lcs(X , Y): 
    # find the length of the strings 
    m = len(X) 
    n = len(Y) 
  
    # declaring the array for storing the dp values 
    L = [[None]*(n+1) for i in range(m+1)] 
  
    # Buttom up 
    # Note: L[i][j] contains length of LCS of X[0..i-1] 
    # and Y[0..j-1]
    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0 : 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1]+1
            else: 
                L[i][j] = max(L[i-1][j] , L[i][j-1]) 
  
    # L[m][n] contains the length of LCS
    return L[m][n]   
  
X = "AGGTAB"
Y = "GXTXAYB"
print("Length of LCS is ")
print(lcs(X, Y) )
