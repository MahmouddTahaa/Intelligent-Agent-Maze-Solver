from PyMaze_Module.pyMaze import *
import numpy as np


def dijkstra(graph, *weights):
    initial_state = (graph.rows, graph.cols)
    goal = (1, 1)
    unexplored = {node: np.inf for node in graph.grid}
    unexplored[initial_state] = 0
    explored = {}
    node_weights = [(i.position, i.cost) for i in weights]
    directions = ['E', 'S', 'N', 'W']
    searching_path = [initial_state] 
    reversed_path = {}
    shortest_path = {}

    while len(unexplored) > 0:
        current_node = min(unexplored, key=unexplored.get)
        explored[current_node] = unexplored[current_node]
        searching_path.append(current_node)
        if current_node == goal:
            break

        for direction in directions:
            if graph.maze_map[current_node][direction] == 1:
                if direction == 'E':
                    next_node = (current_node[0], current_node[1]+1)
                elif direction == 'N':
                    next_node = (current_node[0]-1, current_node[1])
                elif direction == 'S':
                    next_node = (current_node[0]+1, current_node[1])
                elif direction == 'W':
                    next_node = (current_node[0], current_node[1]-1)

                if next_node in explored:
                    continue

                next_node_cost = unexplored[current_node] + 1
                for node_weight in node_weights:
                    if node_weight[0] == current_node:
                        next_node_cost += node_weight[1]

                if next_node_cost < unexplored[next_node]:
                    unexplored[next_node] = next_node_cost
                    reversed_path[next_node] = current_node

        unexplored.pop(current_node)

    trace_node = goal
    while trace_node != initial_state:
        shortest_path[reversed_path[trace_node]] = trace_node
        trace_node = reversed_path[trace_node]

    return explored[goal], searching_path, reversed_path, shortest_path


if __name__ == '__main__':
    # maze creation
    maze_size = (10, 10)
    Maze = maze(maze_size[0], maze_size[1])
    maze.CreateMaze(Maze, loopPercent=40, saveMaze=True)

    # specifying the location and cost of some nodes (nodes with edge weight > 1)
    c1 = agent(Maze, 5, 4, color=COLOR.red)
    c2 = agent(Maze, 1, 2, color=COLOR.red)
    c3 = agent(Maze, 1, 5, color=COLOR.red)

    c1.cost = 50
    c2.cost = 10
    c3.cost = 20


    cost, seacrhing_path, reverse_path, shortest_path = dijkstra(Maze, c1, c2, c3)

    # agent creation, one for each value returned from the  
    a1 = agent(Maze, footprints=True, filled=True, shape='square', color=COLOR.blue)
    a2 = agent(Maze, 1, 1, goal=maze_size, footprints=True, filled=True, color=COLOR.yellow)
    a3 = agent(Maze, footprints=True, shape='arrow', color=COLOR.red)

    # labels
    search_label = TextLabel(Maze, "Searching Steps", len(seacrhing_path))
    shortest_path_label = TextLabel(Maze, "Shortest Path Steps", len(shortest_path)+1)
    cst = TextLabel(Maze, "Total Cost Of the Shortest Path", cost)

    # animating the searching path, reversed path, and shortest path
    Maze.tracePath({a1: seacrhing_path}, delay=150)
    Maze.tracePath({a2: reverse_path}, delay=150)
    Maze.tracePath({a3: shortest_path}, delay=200)

    Maze.run()