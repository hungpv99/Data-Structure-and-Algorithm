from operator import itemgetter
import matplotlib.pyplot as plt
import math
from random import randint

def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    dx = x1 - x2
    dy = y1 - y2

    return math.sqrt(dx*dx + dy*dy)

def random_points(n, b):
    points = []
    for i in range(n):
        points.append((randint(1, b),randint(1, b)))
    return points


def kdtree(points, depth=0):

    try:
        k = len(points[0])
    except IndexError:
        return None

    axis = depth % k
    
    points.sort(key=itemgetter(axis))

    median = len(points) // 2

    return {
        'point' : points[median],
        'left' : kdtree(points[:median], depth+1),
        'right' : kdtree(points[median+1:], depth+1)
    }

def closer_distance(pivot, p1, p2):
    if p1 == None:
        return p2
    if p1 == None:
        return p1

    d1 = distance(p1, pivot)
    d2 = distance(p2, pivot)

    if d1 < d2:
        return p1
    else:
        return p2

best_list = []
def add(point):
    global best_list
    if point not in best_list:
        best_list.append(point)
    best_list.sort()
    if len(best_list) > 3:
        best_list.pop()

def kdtree_closest_point(root, point_target, depth=0, k=2):
    global best_list
    if root == None:
        return None
    
    axis = depth % k

    next_branch = None
    opposite_branch = None

    if point_target[axis] < root['point'][axis]:
        next_branch = root['left']
        opposite_branch = root['right']
    else:
        next_branch = root['right']
        opposite_branch = root['left']

    add((distance(point_target, root['point']), root['point']))

    best_branch = kdtree_closest_point(next_branch, point_target, depth+1)
    if best_branch != None:
        p = (distance(best_branch, point_target), best_branch)
        add(p)

    #best = closer_distance(point_target,best_branch, root['point'])

    if distance(best_list[-1][1], point_target) > abs(point_target[axis] - root['point'][axis]):
        best_branch = kdtree_closest_point(opposite_branch, point_target, depth+1)
        if best_branch != None:
            p = (distance(best_branch, point_target), best_branch)
            add(p)
        #best = closer_distance(point_target, best_branch, best)

    return best_list[0][1]
    

def show(points, point_target, point_result=None):
    xs = [x[0] for x in points]
    ys = [x[1] for x in points]

    xr = [x[1][0] for x in point_result]
    yr = [x[1][1] for x in point_result]

    plt.scatter(xs, ys, color='black')
    plt.scatter(point_target[0], point_target[1], color='red')
    plt.scatter(xr, yr, color='yellow')
    plt.show()  

if __name__ == '__main__':
    N = 10
    B = 1000
    points = random_points(N, B)
    point_target = (randint(1, B),randint(1, B))
    tree = kdtree(points)
    best = kdtree_closest_point(tree, point_target)
    print(best_list)
    show(points, point_target, best_list)