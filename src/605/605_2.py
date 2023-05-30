def can_place_n_flowers(X, N):
    m = len(X)
    print(X)
    if(N == 0):
        result = True
    elif(N == 1):
        if(m < 1):
            result = False
        if(m == 1):
            result = X[0] == 0
        if(m == 2):
            result = X[0] == X[1] == 0
        else:
            result = (X[0] == X[1] == 0 or X[m - 2] == X[m - 1] == 0) or any([X[i - 1] == X[i] == X[i + 1] == 0 for i in range(2, m - 2)])
    else:
        if(m < N):
            result = False
        else:
            result = can_place_n_flowers(X[1:m], N) or (can_place_n_flowers(X[1:m], N - 1) and X[0] == X[1] == 0)
    return(result)

#print(can_place_n_flowers([0, 0, 1], 2))
print(can_place_n_flowers([1,0,0,0,0,0,1], 3))
#print(can_place_n_flowers([1,0,0,0,1], 1))