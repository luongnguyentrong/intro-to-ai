from nonograms_heuristic import main as heuristic_solution
from nonograms_dfs import main as dfs_solution
from prettytable import PrettyTable
import time
import tracemalloc
import json

def write_to_file(stats, filename):
    with open(filename, 'w', newline='') as file:
        for key in stats:
            file.write(f"[{key}]\n")

            table = PrettyTable(["Time (s)", "Memory"])

            table.add_rows(stats[key])

            file.write(str(table))
            file.write("\n")

if __name__ == "__main__":
    algo = input("Chọn thuật toán muốn thống kê (dfs, heuristic): ")

    
    board_types = ["5x5", "15x15"]

    if algo == "heuristic":
        stats = {}

        for board_type in board_types:
            stats[board_type] = []

            print(f"Testing board game of size {board_type}...")

            for i in range(1, 6):
                file = open(f"gameplays/{board_type}/game_{i}.json")
                data = json.load(file)

                COLS = data['cols']
                ROWS = data['rows']

                # Record the start time before calling the function
                start_time = time.time()

                # starting the monitoring
                tracemalloc.start()

                heuristic_solution(ROWS, COLS)
                print(f"\tFinished gameplays/{board_type}/game_{i}.json!")

                # Record the end time after the function has completed execution
                end_time = time.time()

                stats[board_type].append((round(end_time - start_time, 4), tracemalloc.get_traced_memory()[1]))

                # stopping the library
                tracemalloc.stop()
        
            write_to_file(stats, f"{algo}.stats")

    elif algo == "dfs":
        board_type = "5x5"
        stats = {}
        stats[board_type] = []

        print(f"Testing board game of size {board_type}...")
        for i in range(1, 6):
            file = open(f"gameplays/{board_type}/game_{i}.json")
            data = json.load(file)

            COLS = data['cols']
            ROWS = data['rows']

            # Record the start time before calling the function
            start_time = time.time()

            # starting the monitoring
            tracemalloc.start()

            dfs_solution(ROWS, COLS, print_result=False)
            print(f"\tFinished gameplays/{board_type}/game_{i}.json!")

            # Record the end time after the function has completed execution
            end_time = time.time()

            stats[board_type].append((round(end_time - start_time, 4), tracemalloc.get_traced_memory()[1]))

            # stopping the library
            tracemalloc.stop()
    
        write_to_file(stats, f"{algo}.stats")






    