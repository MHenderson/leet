def can_place_one_flower(flowerbed):
    result=False
    m=len(flowerbed)
    if((flowerbed[0] == 0 and flowerbed[1] == 0) or (flowerbed[m - 1] == 0 and flowerbed[m - 2] == 0)):
        result=True
    for i in range(m):
        if(flowerbed[i]==0 and flowerbed[i+1]==0 and flowerbed[i+1]==0):
            result=True
            break
    return(result)

flowerbed = [1,0,0,0,1]

print(can_place_one_flower(flowerbed))