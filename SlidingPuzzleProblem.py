import heapq
import copy
import time

class Board:
    def __init__(self, gcheck, hslot, moves=0, previous=None):
        self.gcheck = gcheck
        self.hslot = hslot
        self.moves = moves
        self.previous = previous
        self.blank_pos = self.blankfinding()

        if self.blank_pos is None:
            raise ValueError("Oops, no blank tile! Board’s messed up.")

    def blankfinding(self):
        for index in range(len(self.gcheck)):
            if self.gcheck[index] == 0:
                return index // self.hslot, index % self.hslot
        return None

    def goalcheck(self, target_state):
        return self.gcheck == target_state

    def movegen(self):
        neighbors = []
        row, col = self.blank_pos
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < self.hslot and 0 <= new_col < self.hslot:
                new_state = copy.deepcopy(self.gcheck)
                new_index = new_row * self.hslot + new_col
                blank_index = row * self.hslot + col
                new_state[blank_index], new_state[new_index] = new_state[new_index], new_state[blank_index]
                neighbors.append(Board(new_state, self.hslot, self.moves + 1, self))
        return neighbors

    def __lt__(self, other):
        return self.moves < other.moves

# Manhattan Distance Heuristic
def manhattan_dist(curr_state, target_state, hslot):
    dist = 0
    for i in range(hslot * hslot):
        if curr_state[i] != 0:
            target_index = target_state.index(curr_state[i])
            curr_row, curr_col = i // hslot, i % hslot
            target_row, target_col = target_index // hslot, target_index % hslot
            dist += abs(curr_row - target_row) + abs(curr_col - target_col)
    return dist

def astar_search(start_board, target_state, hslot, max_moves):
    open_list = []
    closed_set = set()
    heapq.heappush(open_list, (0, start_board))

    while open_list:
        _, current_board = heapq.heappop(open_list)

        if current_board.goalcheck(target_state):
            return pathtrace(current_board), current_board.moves

        if current_board.moves >= max_moves:
            continue

        closed_set.add(tuple(current_board.gcheck))

        for neighbor in current_board.movegen():
            if tuple(neighbor.gcheck) in closed_set:
                continue

            cost = neighbor.moves + manhattan_dist(neighbor.gcheck, target_state, hslot)
            heapq.heappush(open_list, (cost, neighbor))

    return None, 0

def pathtrace(board):
    path = []
    while board:
        path.append(board)
        board = board.previous
    return path[::-1]

def puzzleload(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        hslot = int(lines[0].split()[0])
        max_moves = int(lines[0].split()[1])
        start_state = list(map(int, lines[1].split()))
        target_state = list(map(int, lines[2].split()))
        return hslot, max_moves, start_state, target_state

def solutiondisplay(path, total_moves):
    print(f"Moves you gotta make: {total_moves}")
    for board in path:
        print(f"Step {board.moves}:")
        for row in range(board.hslot):
            print(board.gcheck[row * board.hslot:(row + 1) * board.hslot])
        print()

def main():
    start_time = time.time()

    hslot, max_moves, start_state, target_state = puzzleload("puzzle_input.txt")

    try:
        start_board = Board(start_state, hslot)
    except ValueError as e:
        print(e)
        return

    solution_path, total_moves = astar_search(start_board, target_state, hslot, max_moves)

    if solution_path:
        print("Found a solution:")
        solutiondisplay(solution_path, total_moves)
    else:
        print(f"Couldn’t find a solution within {max_moves} moves.")

    end_time = time.time()
    print(f"Took {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    main()
