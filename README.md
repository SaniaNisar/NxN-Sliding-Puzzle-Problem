# NxN-Sliding-Puzzle-Problem

### Problem
The 8 and 15 puzzle problems are classic problems used to test any intelligent state-space
search strategy. In this assignment we are going to implement A* algorithm to solve 3(2x2),
8(3x3), 15(4x4) and 24(5x5) puzzles.

These puzzle, also known as the sliding puzzle, are classic problem where the objective is to
arrange a set of numbered tiles in a specific order. Each puzzle consists of a 2x2, 3x3, 4x4 or
5x5 grids respectively with 3, 8, 15 and 24 numbered tiles and one empty space. Players can
move tiles adjacent to the empty space into that gap or equivalently move the space into a
horizontally or vertically adjacent location. The goal of this puzzle is to arrange the tiles in
some pre-specified order (typically sorted order).

### Solution
My program will be provided name of a text file containing a set of initial and final
configuration pairs and a limit L on the number of moves allowed. For each pair of
configurations and limit, my program generates a set of at most L valid moves needed
to transform the initial state into the final state or it must inform the user that no such
sequence of moves exists.

### Files
* Code (In Python)
* Documentation of code
* Description of all necessary implementation details like Heuristic(s) used
* Results and statistics like time used to solve puzzles of varying difficulty
