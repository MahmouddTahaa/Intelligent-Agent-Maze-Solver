from aStar import a_star_e, a_star_m, a_star_c
from pyamaze import maze,agent,COLOR,textLabel
from timeit import timeit


Maze = maze(20, 20)
Maze.CreateMaze(loopPercent=70)

e_search, e_rev, e_path = a_star_e(Maze)
m_search, m_rev, m_path = a_star_m(Maze)
c_search, c_rev, c_path = a_star_c(Maze)

textLabel(Maze,'Chebyshev Path Lenbth',len(c_path)+1)
textLabel(Maze,'Euclidean Path Length',len(e_path)+1)
textLabel(Maze,'Manhattan Path Length',len(m_path)+1)
textLabel(Maze,'Chebyshev Search Lenbth',len(c_search))
textLabel(Maze,'Euclidean Search Length',len(e_search))
textLabel(Maze,'Manhattan Search Length',len(m_search))

a1 = agent(Maze,footprints=True, color=COLOR.red, filled=False)
a2 = agent(Maze,footprints=True, color=COLOR.yellow, filled=False)
a3 = agent(Maze,footprints=True, color=COLOR.blue, filled=False)

Maze.tracePath({a1: c_search}, delay=50)
Maze.tracePath({a2: e_search}, delay=50)
Maze.tracePath({a3: m_search}, delay=50)


t1=timeit(stmt='a_star_e(Maze)', number=1000, globals=globals())
t2=timeit(stmt='a_star_m(Maze)', number=1000, globals=globals())
t3=timeit(stmt='a_star_c(Maze)', number=1000, globals=globals())

textLabel(Maze,'Chebyshev Time', t3)
textLabel(Maze,'Euclidean Time', t1)
textLabel(Maze,'Manhattan Time', t2)


Maze.run()