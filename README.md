# Acorn Maze

This is a Maze Navigator assignment built in Python. To run the game choose a board from the boards folder (or submit your own) and run **python3 run.py "Board".** This will trigger the maze, you can navigate using the WASD keys, and the goal is to reach the Y.

There are two main extra components to this game. The W and F characters represent water buckets and Fire blocks. In order to pass through a Fire block, you must first pick up a water bucket, which then disappears from the map. The second component is teleporters. If you step onto a number, you are instantly moved to the location of it's match on the map. These two components allow for more complicated map development.

There is another way to test this assignment, also implemented is a BFS/DFS solver. When run it will find the fastest route through the board given, and output the solution to the screen. To run the solver choose a board and run **python3 solver.py "Board" "BFS/DFS"**.
