from itertools import combinations
from nonograms_dfs import is_equal
import json
import time
import numpy as np

ROWS = None
COLS = None

def get_all_moves(consts, length):
    all_moves = []

    for const in consts:
        moves = generate_moves(const=const, length=length)

        all_moves.append(moves)

    return all_moves


def generate_moves(const, length):
    moves = []

    empty_slots = length - np.sum(const) + 1

    for p in combinations(range(empty_slots), len(const)):
        move = [[0]] * empty_slots

        for i, idx in enumerate(p):
            move[idx] = np.concatenate([np.ones(const[i]), np.zeros(1)])

        moves.append(np.concatenate(move)[:-1])

    return np.asarray(moves)


def get_fixed_cells(moves):
    def transform(line):
        return len(np.unique(line))

    unique_count =  np.apply_along_axis(transform, 0, moves)

    fixed_idx = np.where(unique_count == 1)[0]

    return fixed_idx


def main(_ROWS, _COLS):
    global ROWS
    global COLS

    # set global variables
    COLS = _COLS
    ROWS = _ROWS

    # generate all possible row moves and col moves
    all_rows_moves = get_all_moves(ROWS, len(COLS))
    all_cols_moves = get_all_moves(COLS, len(ROWS))

    # save finished status
    rows_done = np.zeros(len(ROWS))
    cols_done = np.zeros(len(COLS))

    # generate board game
    init_state = np.zeros((len(ROWS), len(COLS)))

    current_axis = False
    while not np.all(rows_done) and not np.all(cols_done):
        if current_axis == 0:
            all_moves = all_rows_moves
        else:
            all_moves = all_cols_moves

        # traverse all possible moves
        for idx, moves in enumerate(all_moves):
            # check if current axis is finished
            if current_axis == 0 and rows_done[idx]:
                continue
            elif current_axis == 1 and cols_done[idx]:
                continue

            # find must-filled cells
            fixed_cells = get_fixed_cells(moves=moves)

            if len(fixed_cells) > 0:
                values = moves[0, fixed_cells]

                if current_axis == 0:
                    # set row values
                    init_state[idx, fixed_cells] = values

                    # remove col moves that doesn't satisfy fixed cells
                    for i, cell in enumerate(fixed_cells):
                        col_moves = all_cols_moves[cell]

                        all_cols_moves[cell] = col_moves[col_moves[:, idx] == values[i]]

                    # check if row is finished
                    if is_equal(ROWS[idx], init_state[idx, :]):
                        rows_done[idx] = True
                else:
                    # set col values
                    init_state[fixed_cells, idx] = values

                    # remove row moves that doesn't satisfy fixed cells
                    for i, cell in enumerate(fixed_cells):
                        row_moves = all_rows_moves[cell]
                        all_rows_moves[cell] = row_moves[row_moves[:, idx] == values[i]]

                    # check if col is finished
                    if is_equal(COLS[idx], init_state[:, idx]):
                        cols_done[idx] = True

        # alternate axis
        current_axis = not current_axis

if __name__ == "__main__":
    board_types = ["5x5", "15x15"]
    file = open("gameplays/15x15/game_4.json")
    data = json.load(file)

    COLS = data['cols']
    ROWS = data['rows']

    # Record the start time before calling the function
    start_time = time.time()

    main(ROWS, COLS)

    # Record the end time after the function has completed execution
    end_time = time.time()

    print("SOLVED!")
    print(end_time - start_time)
