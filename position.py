position = tuple[int,int]

def position_create(row: int, col:int)->position:

    if not (type(row) is int and row>=0) or not (type(col) is int and col>=0)
        raise ValueError('position_create: invalid arguments')

    return row, col

def position_is(pos:position)->bool:


def position_row(pos:position)->int:

def position_col(pos:position)->int:

def position_equal(pos1:position, pos2:position)->bool:

def position_str(pos:position)->str:



