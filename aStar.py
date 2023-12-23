from PyMaze_Module.pyMaze import *
from queue import PriorityQueue
import numpy as np

def h_e(node1, node2):
    x1 = node1[0]
    y1 = node1[1]
    x2 = node2[0]
    y2 = node2[1]
    euclidean_distance = np.sqrt(((x1-x2)**2) + ((y1-y2)**2))
    return euclidean_distance

def h_m(node1, node2):
    x1 = node1[0]
    y1 = node1[1]
    x2 = node2[0]
    y2 = node2[1]
    manhattan_distance = np.abs(x1 - x2) + np.abs(y1 -y2)
    return manhattan_distance

def h_c(node1, node2):
    x1 = node1[0]
    y1 = node1[1]
    x2 = node2[0]
    y2 = node2[1]
    chebyshev_distance = max(np.abs(x1-x2), np.abs(y1-y2))
    return chebyshev_distance


def a_star_e(maze, start: tuple=None) -> dict:
    maze_nodes = maze.grid
    initial_state = (maze.rows, maze.cols)
    goal = (1, 1)
    search_path = [initial_state]
    reverse_path = {}
    path = {}
    directions = ['E', 'S', 'N', 'W']
    g_values = {node: np.inf for node in maze_nodes}
    g_values[initial_state] = 0
    h_values = {node: np.inf for node in maze_nodes}
    h_values[initial_state] = h_e(initial_state, goal)
    f_values = {node: np.inf for node in maze_nodes}
    f_values[initial_state] = g_values[initial_state] + h_e(initial_state, goal)
    fringe = PriorityQueue()
    fringe.put((f_values[initial_state], h_values[initial_state], initial_state))

    while not (fringe.empty()):
        current_node = fringe.get()[2]
        search_path.append(current_node)
        if current_node == goal:
            break

        for direction in directions:
            if maze.maze_map[current_node][direction] == 1:
                if direction == 'E':
                    child_node = (current_node[0], current_node[1]+1)
                elif direction == 'S':
                    child_node = (current_node[0]+1, current_node[1])
                elif direction == 'N':
                    child_node = (current_node[0]-1, current_node[1])
                elif direction == 'W':
                    child_node = (current_node[0], current_node[1]-1)

                new_g_value = g_values[current_node] + 1
                new_f_value = new_g_value + h_e(child_node, goal)

                if new_f_value < f_values[child_node]:
                    g_values[child_node] = new_g_value
                    f_values[child_node] = new_f_value
                    fringe.put((f_values[child_node], h_e(child_node, goal), child_node))

                    reverse_path[child_node] = current_node

    trace_node = goal
    while trace_node != initial_state:
        path[reverse_path[trace_node]] = trace_node
        trace_node = reverse_path[trace_node]

    return search_path, reverse_path, path


def a_star_m(maze, start: tuple=None) -> dict:
    maze_nodes = maze.grid
    initial_state = (maze.rows, maze.cols)
    goal = (1, 1)
    search_path = [initial_state]
    reverse_path = {}
    path = {}
    directions = ['E', 'S', 'N', 'W']
    g_values = {node: np.inf for node in maze_nodes}
    g_values[initial_state] = 0
    h_values = {node: np.inf for node in maze_nodes}
    h_values[initial_state] = h_m(initial_state, goal)
    f_values = {node: np.inf for node in maze_nodes}
    f_values[initial_state] = g_values[initial_state] + h_m(initial_state, goal)
    fringe = PriorityQueue()
    fringe.put((f_values[initial_state], h_values[initial_state], initial_state))

    while not (fringe.empty()):
        current_node = fringe.get()[2]
        search_path.append(current_node)
        if current_node == goal:
            break

        for direction in directions:
            if maze.maze_map[current_node][direction] == 1:
                if direction == 'E':
                    child_node = (current_node[0], current_node[1]+1)
                elif direction == 'S':
                    child_node = (current_node[0]+1, current_node[1])
                elif direction == 'N':
                    child_node = (current_node[0]-1, current_node[1])
                elif direction == 'W':
                    child_node = (current_node[0], current_node[1]-1)

                new_g_value = g_values[current_node] + 1
                new_f_value = new_g_value + h_m(child_node, goal)

                if new_f_value < f_values[child_node]:
                    g_values[child_node] = new_g_value
                    f_values[child_node] = new_f_value
                    fringe.put((f_values[child_node], h_m(child_node, goal), child_node))

                    reverse_path[child_node] = current_node

    trace_node = goal
    while trace_node != initial_state:
        path[reverse_path[trace_node]] = trace_node
        trace_node = reverse_path[trace_node]

    return search_path, reverse_path, path


def a_star_c(maze, start: tuple=None) -> dict:
    maze_nodes = maze.grid
    initial_state = (maze.rows, maze.cols)
    goal = (1, 1)
    search_path = [initial_state]
    reverse_path = {}
    path = {}
    directions = ['E', 'S', 'N', 'W']
    g_values = {node: np.inf for node in maze_nodes}
    g_values[initial_state] = 0
    h_values = {node: np.inf for node in maze_nodes}
    h_values[initial_state] = h_c(initial_state, goal)
    f_values = {node: np.inf for node in maze_nodes}
    f_values[initial_state] = g_values[initial_state] + h_c(initial_state, goal)
    fringe = PriorityQueue()
    fringe.put((f_values[initial_state], h_values[initial_state], initial_state))

    while not (fringe.empty()):
        current_node = fringe.get()[2]
        search_path.append(current_node)
        if current_node == goal:
            break

        for direction in directions:
            if maze.maze_map[current_node][direction] == 1:
                if direction == 'E':
                    child_node = (current_node[0], current_node[1]+1)
                elif direction == 'S':
                    child_node = (current_node[0]+1, current_node[1])
                elif direction == 'N':
                    child_node = (current_node[0]-1, current_node[1])
                elif direction == 'W':
                    child_node = (current_node[0], current_node[1]-1)

                new_g_value = g_values[current_node] + 1
                new_f_value = new_g_value + h_c(child_node, goal)

                if new_f_value < f_values[child_node]:
                    g_values[child_node] = new_g_value
                    f_values[child_node] = new_f_value
                    fringe.put((f_values[child_node], h_c(child_node, goal), child_node))

                    reverse_path[child_node] = current_node

    trace_node = goal
    while trace_node != initial_state:
        path[reverse_path[trace_node]] = trace_node
        trace_node = reverse_path[trace_node]

    return search_path, reverse_path, path


if __name__ == '__main__':
    maze_size = (50, 50)
    m = maze(maze_size[0], maze_size[1])
    m.CreateMaze(loopPercent=100)

    seacrhing_path, reverse_path, path = a_star_m(m)

    a = agent(m, footprints=True, filled=True, shape='square', color=COLOR.blue)
    b = agent(m, 1, 1, goal=maze_size, footprints=True, filled=True, color=COLOR.yellow)
    c = agent(m, footprints=True, shape='arrow', color=COLOR.red)

    search_label = TextLabel(m, "Searching Steps", len(seacrhing_path))
    shortest_path_label = TextLabel(m, "Shortest Path Steps", len(path)+1)

    m.tracePath({a: seacrhing_path},showMarked=True, delay=10)
    m.tracePath({b: reverse_path}, delay=10)
    m.tracePath({c: path}, delay=15)

    m.run()

