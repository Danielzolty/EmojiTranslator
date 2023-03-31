'''
Based on the column for which a piece might be dropped, a certain value is 
assiciated to it. For example, a piece dropped in the middle column is a lot 
stronger than a chip dropped in one of the side columns because there are 
more possible 4-in-a-row possibilities. So, each column has a respective value 
attached to it. 
'''
def value_of_col(col):
    if col == 0 or col == 6:
        return 1
    if col == 1 or col == 5:
        return 3
    if col == 2 or col == 4:
        return 5
    return 7

'''
For each column, there are other columns that are a possibly included for a 4-
in-a-row. This is to find all other columns involved for potential horizontal
4-in-a-rows. So, for each column, it returns the respective columns that could
be included in the 4-in-a-rows.
'''
def possible_col_points(col):
    if col == 0:
        return [1,2,3]
    if col == 1:
        return [0,2,3,4]
    if col == 2:
        return [0,1,3,4,5]
    if col == 3:
        return [0,1,2,4,5,6]
    if col == 4:
        return [1,2,3,5,6]
    if col == 5:
        return [2,3,4,6]
    if col == 6:
        return [3,4,5]

'''
For each row, there are other rows that are a possibly included for a 4-
in-a-row. This is to find all other rows involved for potential vertical
4-in-a-rows. So, for each row, it returns the respective rows that could
be included in the 4-in-a-rows.
'''
def possible_row_points(row):
    if row == 0:
        return [1,2,3]
    if row == 1:
        return [0,2,3,4]
    if row == 2:
        return [0,1,3,4,5]
    if row == 3:
        return [0,1,2,4,5]
    if row == 4:
        return [1,2,3,5]
    if row == 5:
        return [2,3,4]

'''
For each right diagonal, there are other squares that are a possibly included 
for a 4-in-a-row. This is to find all other squares involved for potential 
right diagonal 4-in-a-rows. So, for each square, it returns the respective 
squares in the right diagonal that could be included in the 4-in-a-rows.
'''
def right_diag_points(row, col):
    pts = []
    for i in range(6):
        if row == i or abs(row - i) > 3:
            continue
        if i < row:
            diff = row - i
            if col - diff < 0:
                continue
            else:
                pts.append((i, col-diff))
        else:
            diff = i - row
            if col + diff > 6:
                continue
            else:
                pts.append((i, col+diff))
    if len(pts) < 3:
        return None
    return pts

'''
For each left diagonal, there are other squares that are a possibly included 
for a 4-in-a-row. This is to find all other squares involved for potential 
left diagonal 4-in-a-rows. So, for each square, it returns the respective 
squares in the left diagonal that could be included in the 4-in-a-rows.
'''
def left_diag_points(row, col):
    pts = []
    for i in range(6):
        if row == i or abs(row - i) > 3:
            continue
        if i < row:
            diff = row - i
            if col + diff > 6:
                continue
            else:
                pts.append((i, col+diff))
        else:
            diff = i - row
            if col - diff < 0:
                continue
            else:
                pts.append((i, col-diff))
    if len(pts) < 3:
        return None
    return pts

'''
This function returns the differet scores that a certain scenario for 
placing a chip in the column would be. If there were already 3 in a row, so it
would get the highest score of 1000 points. If there were 2 in a row, it's the 
second highest score. 
'''
def winning_move_points(tiles):
    if tiles.count(1) == 3:
        return 10000000
    if tiles.count(1) == 2 and tiles.count(0) == 1:
        return 50
    if tiles.count(1) == 1 and tiles.count(0) == 2:
        return 20
    if tiles.count(0) == 3:
        return 1
    else:
        return 0

'''
This is a method returning points to determine whether the opponent should be 
blocked.
'''
def blocking_move_points(tiles):
    if tiles.count(2) == 3:
        return 999
    if tiles.count(2) == 2 and tiles.count(0) == 1:
        return 49
    if tiles.count(2) == 1 and tiles.count(0) == 2:
        return 19
    else:
        return 0

'''
This will calculate the total score of a square. It receives the score for
potential horizontal 4-in-a-rows, followed by, vertical, followed by right 
diagonal, and lastly left diagonal 4-in-a-rows. It then returns the total score.
'''
def tot_score(board, row, col):
    complete_score = 0
    col_values = possible_col_points(col)
    col_score = 0
    for i in range(len(col_values) - 2):
        same_tiles = [board[row, col_values[i]], board[row, col_values[i+1]], board[row, col_values[i+2]]]
        score = max(winning_move_points(same_tiles), blocking_move_points(same_tiles))
        col_score = max(score, col_score)
    complete_score += col_score
    row_score = 0
    row_values = possible_row_points(row)
    for i in range(len(row_values) - 2):
        same_tiles = [board[row_values[i], col], board[row_values[i+1], col], board[row_values[i+2], col]]
        score = max(winning_move_points(same_tiles), blocking_move_points(same_tiles))
        row_score = max(score, row_score)
    complete_score += row_score
    right_score = 0
    right_values = right_diag_points(row, col)
    if right_values is not None:
        for i in range(len(right_values) - 2):
            same_tiles = [board[right_values[i][0], right_values[i][1]], board[right_values[i+1][0], right_values[i+1][1]], board[right_values[i+2][0], right_values[i+2][1]]]
            score = max(winning_move_points(same_tiles), blocking_move_points(same_tiles))
            right_score = max(score, right_score)
    complete_score += right_score
    left_score = 0
    left_values = left_diag_points(row, col)
    if left_values is not None:
        for i in range(len(left_values) - 2):
            same_tiles = [board[left_values[i][0], left_values[i][1]], board[left_values[i+1][0], left_values[i+1][1]], board[left_values[i+2][0], left_values[i+2][1]]]
            score = max(winning_move_points(same_tiles), blocking_move_points(same_tiles))
            left_score = max(score, left_score)
    complete_score += left_score
    return complete_score