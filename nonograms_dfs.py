import numpy as np
import json
from nonograms_heuristic import generate_moves, is_equal, get_user_input
from display import draw_nonogram
import tracemalloc
import time

# Global variables
ROWS = None
COLS = None

def is_finished(state: np.ndarray):
    # check rows
    for cons, row in zip(ROWS, state):
        if not is_equal(cons, row):
            return False

    # check cols
    for cons, col in zip(COLS, state.T):
        if not is_equal(cons, col):
            return False

    return True

def dfs(cur_state: np.ndarray, row_idx: int):
    # check if state is finished
    if is_finished(cur_state):
        return True, cur_state

    # stop dfs
    if row_idx == len(ROWS):
        return False, []

    # all possible moves 
    moves = generate_moves(ROWS[row_idx], len(COLS))

    # dfs branching
    for move in moves:
        new_state = np.copy(cur_state)

        new_state[row_idx, :] = move

        is_solved, finished_state = dfs(cur_state=new_state, row_idx=row_idx + 1)
        if is_solved:
            return True, finished_state

    return False, []

def main(ROWS_VALS, COL_VALS, print_result = True):
    global ROWS
    global COLS

    COLS = COL_VALS
    ROWS = ROWS_VALS

    init_state = np.zeros((len(ROWS), len(COLS)))

    is_solved, results = dfs(init_state, 0)

    if print_result:
        if is_solved:
            draw_nonogram(ROWS, COLS, results)
        else:
            print("FAILED!")

if __name__ == "__main__":
    board_type, level = get_user_input()

    file = open(f"gameplays/{board_type}/game_{level}.json")
    data = json.load(file)

    COLS = data['cols']
    ROWS = data['rows']
    
    # Record the start time before calling the function
    start_time = time.time()

    # starting the monitoring
    tracemalloc.start()

    main(ROWS_VALS=ROWS, COL_VALS=COLS)

    # Record the end time after the function has completed execution
    end_time = time.time()

    print(f"FINISHED IN {round(end_time - start_time, 3)}s!")
    print(f"Memory usage: {tracemalloc.get_traced_memory()[1]}")