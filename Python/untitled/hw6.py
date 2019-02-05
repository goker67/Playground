import numpy as np
import matplotlib.pyplot as plt

def is_valid_board(ndarray):

    ndarray_check = np.isin(ndarray,[0,1])
    if ndarray_check.all():
        return True
    else:
        return False


#matrix = np.array([[1,1,1,1],[0,1,0,1],[0,0,1,1],[1,0,1,0]])
#matrix2 = np.array([[1,1,2],[0,1,0],[1,0,0]])

#padd_array = np.pad(ndarray,1,"constant",constant_values = 0)
#print(padd_array)

"""
print(is_valid_board(first_matrix))
print(is_valid_board(first_matrix2))
"""
def gol_step(first_matrix):

    next_matrix = np.copy(first_matrix)
    padd_array = np.pad(first_matrix, 1, "constant", constant_values=0)
    #ones_indices = np.argwhere(padd_array)


    for i in range(1, padd_array.shape[0]-1):
        for j in range(1,padd_array.shape[1]-1):
            padd = padd_array[i-1:i+2, j-1:j+2]
            ones_total = padd.sum() - padd_array[i][j]
            if (padd_array[i,j] == 1):
                if ones_total < 2 or ones_total > 3: next_matrix[i-1][j-1] = 0
            else:
                if ones_total == 3:
                    next_matrix[i-1][j-1] = 1
    return next_matrix

#print(matrix)
#print("       ")
#print(gol_step(matrix))


def draw_gol_board(matrix):


    plt.imshow(matrix,cmap = 'binary')
    plt.colorbar()
    plt.show()

dead_matrix = np.zeros((100,100))
dead_matrix[[1,2,3,3,3],[2,3,1,2,3]] = 1

#draw_gol_board(dead_matrix)

gol_step(dead_matrix)
draw_gol_board(dead_matrix)

#draw_gol_board(first_matrix)
#draw_gol_board(matrix2)