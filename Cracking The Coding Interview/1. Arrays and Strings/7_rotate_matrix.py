# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

def rotate_matrix(arr1):
    transposed = transpose_matrix(arr1)
    
    for i in range(len(transposed)):
        transposed[i].reverse()
    
    return transposed


def transpose_matrix(arr2):
    for i in range(len(arr2)):
        for j in range(i+1,len(arr2)):
            if i == j:
                continue
            else:
                arr2[i][j], arr2[j][i] = arr2[j][i], arr2[i][j]
    return arr2
arr = [[1,2,3],[4,5,6],[7,8,9]]
# arr = [[7,4,1],[8,5,2],[9,6,3]]
print(rotate_matrix(arr))