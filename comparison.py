from pyamaze import maze,agent,COLOR,textLabel
from dijkstra import dijkstra
from aStar import a_star
from timeit import timeit

Maze = maze(20, 20)
Maze.CreateMaze(loopPercent=50)

c1 = agent(Maze, 5, 4, color=COLOR.red)
c2 = agent(Maze, 13, 10, color=COLOR.red)
c3 = agent(Maze, 1, 25, color=COLOR.red)
c4 = agent(Maze, 5, 19, color=COLOR.red)
c5 = agent(Maze, 3, 22, color=COLOR.red)
c6 = agent(Maze, 15, 7, color=COLOR.red)
c1.cost = 50
c2.cost = 10
c3.cost = 20
c4.cost = 300
c5.cost = 4
c6.cost = 7

d_cost, d_search, d_rev, d_path = dijkstra(Maze, c1, c2, c3, c4, c5, c6)
a_search, a_rev, a_path = a_star(Maze)

textLabel(Maze,'Dijkstra Path Length',len(d_path)+1)
textLabel(Maze,'A* Path Length',len(a_path)+1)
textLabel(Maze,'Dijkstra Search Length',len(d_search)+1)
textLabel(Maze,'A* Search Length',len(a_search)+1)

a1 = agent(Maze,footprints=True, color=COLOR.blue, filled=False)
a2 = agent(Maze,footprints=True, color=COLOR.red, filled=False)

Maze.tracePath({a1: d_path}, delay=100)
Maze.tracePath({a2: a_path}, delay=100)


t1=timeit(stmt='dijkstra(Maze)', number=1000, globals=globals())
t2=timeit(stmt='a_star(Maze)', number=1000, globals=globals())

textLabel(Maze,'Dijkstra Time', t1)
textLabel(Maze,'A* Time', t2)


Maze.run()