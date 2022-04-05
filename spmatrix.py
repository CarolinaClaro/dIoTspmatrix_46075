from asyncio.windows_events import NULL
from position import *

spmatrix = list[float, dict] 

def spmatrix_create(zero: float = 0.0) -> spmatrix:
    if (type(zero) == int):
        zero = float(zero)
    if (not(type(zero) == float)):
        raise ValueError('spmatrix_create: invalid arguments')
    return list((zero, dict()))

def spmatrix_is(mat: spmatrix) -> bool:
    if (not(type(mat) == list)):
       return False
    else:
        return True

def spmatrix_zero_get(mat: spmatrix) -> float:
    if (not(type(mat) == list)):
        raise ValueError('spmatrix_zero_get: invalid arguments')
    return mat[0]

def spmatrix_zero_set(mat: spmatrix, zero: float):
    if (type(zero) == int):
        zero = float(zero)
    if (not(type(mat) == list) or not(type(zero) == float)):
        raise ValueError('spmatrix_zero_set: invalid arguments')

    mat[0] = zero      

def spmatrix_value_get(mat: spmatrix, pos: position) -> float:
    if (not(type(mat) == list) or not(position_is(pos) == True)):
        raise ValueError('spmatrix_value_get: invalid arguments')
    return mat[1].get(pos)

def spmatrix_value_set(mat: spmatrix, pos: position, val: float):
    if (type(val) == int):
        val = float(val)
    if (not(type(mat) == list) or not(position_is(pos) == True) or not(type(val) == float)):
        raise ValueError('spmatrix_value_set: invalid arguments')
    mat[1].update({pos:val})

def spmatrix_copy(mat: spmatrix) -> spmatrix:
    if (not(type(mat) == list)):
        raise ValueError('spmatrix_copy: invalid arguments')
    return mat

def spmatrix_dim(mat: spmatrix) -> list([tuple[position, position], ()]):
    pos = position
    if (not(type(mat) == list)):
        raise ValueError('spmatrix_dim: invalid arguments')
    if(len(mat[1].items()) == 0):
        return ()
    else:
        rowList = list()
        colList = list()
        for pos in mat[1].keys():
            rowList.append(position_row(pos))
            colList.append(position_col(pos))
        minPos = position_create(min(rowList), min(colList))
        maxPos = position_create(max(rowList), max(colList))
        return minPos, maxPos

def spmatrix_sparsity(mat: spmatrix) -> float:
    if (not(type(mat) == list)):
        raise ValueError('spmatrix_sparsity: invalid arguments')
    dim = spmatrix_dim(mat)
    nrExistingElem = len(mat[1])
    totalElem = (position_row(dim[1])-position_row(dim[0])+1) * (position_col(dim[1])-position_col(dim[0])+1)
    return nrExistingElem/totalElem
  
def spmatrix_str(mat: spmatrix, format: str) -> str:
    if (not(type(mat) == list) or not(type(format) == str)):
        raise ValueError('spmatrix_str: invalid arguments') 

def spmatrix_row(mat: spmatrix, row: int) -> spmatrix:
    if (not(type(mat) == list) or not(type(row) == int)):
        raise ValueError('spmatrix_row: invalid arguments')

def spmatrix_col(mat: spmatrix, col: int) -> spmatrix:
    if (not(type(mat) == list) or not(type(col) == int)):
        raise ValueError('spmatrix_col: invalid arguments')

def spmatrix_diagonal(mat: spmatrix): 
    if (not(type(mat) == list)):
        raise ValueError('spmatrix_diagonal: invalid arguments')

# mat = spmatrix_create()
# spmatrix_value_set(mat, position_create(1,2), 12.5)
# spmatrix_value_set(mat, position_create(2,1), 5.0)
# spmatrix_value_set(mat, position_create(3,3), 8.0)
# spmatrix_zero_set(mat, 8.0)
# print(mat[0])
# print(' ||| ')
# print(mat[1])

