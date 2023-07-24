import numpy as np
import json
from itertools import groupby
from nonograms_heuristic import generate_moves
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

def get_shape(line: np.array):
    clusters = [list(group) for key, group in groupby(line) if key != 0]

    return [np.sum(cluster) for cluster in clusters]

def is_equal(constraint: np.array, line: np.array):
    line_shape = get_shape(line=line)

    if len(constraint) != len(line_shape):
        return False

    if not np.all(np.equal(constraint, line_shape)):
        return False

    return True

def dfs(cur_state: np.ndarray, cur_idx: int, const_idx: int):
    # check if state is finished
    if is_finished(cur_state):
        return True, cur_state

    # stop dfs
    if cur_idx == len(ROWS):
        return False, []

    # current state variables
    row = cur_state[cur_idx]
    const = ROWS[cur_idx]

    # init index
    start_idx = np.where(row == 1)[-1]
    if len(start_idx) == 0:
        start_idx = 0
    else:
        start_idx = start_idx[-1] + 2

    max_len = len(COLS) - sum(const[const_idx:]) - len(const[const_idx:]) + 2

    # dfs branching
    for pos in range(start_idx, max_len):
        new_state = np.copy(cur_state)

        end_idx = pos + const[const_idx]
        new_state[cur_idx, pos:end_idx] = 1

        if const_idx == len(const) - 1:
            is_solved, finished_state = dfs(cur_state=new_state, cur_idx=cur_idx + 1, const_idx=0)
        else:
            is_solved, finished_state = dfs(cur_state=new_state, cur_idx=cur_idx, const_idx=const_idx + 1)

        if is_solved:
            return True, finished_state

    return False, []

def main():
    global ROWS
    global COLS

    file = open("gameplays/15x15/game_1.json")
    data = json.load(file)

    COLS = data['cols']
    ROWS = data['rows']

    init_state = np.zeros((len(ROWS), len(COLS)))

    # Record the start time before calling the function
    start_time = time.time()

    is_solved, results = dfs(init_state, 0, 0)

    # Record the end time after the function has completed execution
    end_time = time.time()

    if is_solved:
        print("SOLVED!")
        print(end_time - start_time)
        print(results)
    else:
        print("FAILED!")


if __name__ == "__main__":
    main()
