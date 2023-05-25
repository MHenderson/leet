nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 6
n = 3

def find_index(X, y):
    i = 0
    for i in range(len(X)):
        if X[i]>=y or X[i]==0:
            return(i)

def merge(nums1, m, nums2, n):
    for i in nums2:
        x = find_index(nums1, i)
        print(x)
        for j in range(5, -1, -1):
            if j == x:
                nums1[j] == i
            else:
                nums1[j] == nums1[j - 1]
    print(nums1)

print(merge(nums1, m, nums2, n))
