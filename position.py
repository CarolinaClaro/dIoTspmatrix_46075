from sympy import false, true


position = tuple[int, int]

def position_create(row: int, col: int) -> position:
    if not(type(row) is int and row >= 0) or not(type(col) is int and col >= 0):
        raise ValueError('position_create: invalid arguments')
    return row, col

def position_is(pos: position) -> bool:
    return type(pos) is tuple

def position_row(pos: position) -> int:
    row = pos[0]
    if not(type(row) is int and row >= 0) or not(type(pos) is tuple):
        raise ValueError('position_row: invalid arguments')
    return row 
    
def position_col(pos: position) -> int:
    col = pos[1]
    if not(type(col) is int and col >= 0) or not(type(pos) is tuple):
        raise ValueError('position_col: invalid arguments')
    return col

def position_equal(pos1: position, pos2: position) -> bool:
    if not(type(pos1) is tuple) or not(type(pos2) is tuple):
        raise ValueError('position_equal: invalid arguments')
    return pos1 == pos2

def position_str(pos: position) -> str:
    if not(type(pos) is tuple):
        raise ValueError('position_str: invalid arguments')
    return '(' + str(pos[0]) + ', ' + str(pos[1]) + ')'

