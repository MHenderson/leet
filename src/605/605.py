def can_place_n_flowers(flowerbed, n):
    m = len(flowerbed)
    if(n == 0):
        result = True
    elif(m == 0):
        result = False
    elif(flowerbed[0] == flowerbed[1] == 0 and can_place_n_flowers(flowerbed[2:m], n - 1)):
        result = True
    elif(flowerbed[m - 2] == flowerbed[m - 1] == 0) and can_place_n_flowers(flowerbed[0:(m - 2)], n - 1):
        result = True
    elif(n == 1):
        for i in range(2, len(flowerbed) - 2):
            if(flowerbed[i - 1] == flowerbed[i] == flowerbed[i + 1] == 0):
                result = True
                break
    else:
        result = False
        for i in range(2, len(flowerbed) - 2):
            print("i: " + str(i))
            can_place_one = flowerbed[i - 1] == flowerbed[i] == flowerbed[i + 1] == 0
            print("can place one here: " + str(can_place_one))
            left_flowers = flowerbed[0:(i - 1)]
            print("left: " + str(left_flowers))
            right_flowers = flowerbed[(i + 2):(m + 1)]
            print("right: " + str(right_flowers))
            if(len(left_flowers) >= 3):
                can_place_left = can_place_n_flowers(left_flowers, n - 1)
            else:
                can_place_left = False
            print("can place left: " + str(can_place_left))
            if(len(right_flowers)>= 3):
                can_place_right = can_place_n_flowers(right_flowers, n - 1)
            else:
                can_place_right = False
            print("can place right: " + str(can_place_right))
            if(can_place_one and (can_place_left or can_place_right)):
                result = True
                break
        
    return(result)

#flowerbed = [1,0,0,0,0,1]

#print(can_place_n_flowers(flowerbed, 2))

#print(can_place_n_flowers([], 1))

#flowerbed = [1,0,0,0,1]
#print(can_place_n_flowers(flowerbed, 1))

#flowerbed = [1,0,0,0,0,0,1]
#print(can_place_n_flowers(flowerbed, 3))

print(can_place_n_flowers([0, 0, 1], 2))