import sys
import random

#size of maze
SIZE = (15,15)

#directions
N, S, E, W = 1, 2, 4, 8

#dictionary with directions
GO_DIR = {N: (0,-1), S : (0,1), E : (1, 0), W : (-1, 0)}

#reverse
REVERSE = {E : W, W : E, N : S, S : N}

#init maze
maze = list(list(0 for i in range(SIZE[0])) for j in range(SIZE[1]))

def dig(x, y):
    
    #random direction
    dirs = [N, S, W, E]
    random.shuffle(dirs)

    for dir in dirs:
        new_x = x + GO_DIR[dir][0]
        new_y = y + GO_DIR[dir][1]

        if (new_x in range(SIZE[0])) and (new_y in range(SIZE[1])) and (maze[new_y][new_x] == 0):

            maze[y][x] |= dir
            maze[new_y][new_x] |= REVERSE[dir]

            dig(new_x, new_y)

def create_more_way():

    for i in range(5):
        x = random.randint(1,SIZE[0]-2)
        y = random.randint(1,SIZE[1]-2)

        if maze[x][y] & N == 0:
            maze[y][x] |= N
            new_x = x + GO_DIR[N][0]
            new_y = y + GO_DIR[N][1]
            maze[new_y][new_x] |= REVERSE[N]

        elif maze[x][y] & S == 0:
            maze[y][x] |= S
            new_x = x + GO_DIR[S][0]
            new_y = y + GO_DIR[S][1]
            maze[new_y][new_x] |= REVERSE[S]

        elif maze[x][y] & E == 0:
            maze[y][x] |= E
            new_x = x + GO_DIR[E][0]
            new_y = y + GO_DIR[E][1]
            maze[new_y][new_x] |= REVERSE[E]

        elif maze[x][y] & W == 0:
            maze[y][x] |= W
            new_x = x + GO_DIR[W][0]
            new_y = y + GO_DIR[W][1]
            maze[new_y][new_x] |= REVERSE[W]

def draw():
    # prints the seed (for reference) and the lab size
    print("_" * (SIZE[0] * 2))
    for j in range(SIZE[1]):
        x = random.randint(0,9)
        if j!=0:
            print("|", end='')
        else:
            print ("_", end='')
        for i in range(SIZE[0]):
            if (maze[j][i] & S != 0):
                print(" ", end='')
            else:
                print("_", end='')
            if (maze[j][i] & E != 0):
                if ((maze[j][i] | maze[j][i+1]) & S != 0):
                    print(" ", end='')
                else:
                    print("_", end='')
            elif (j==SIZE[1]-1) & (i==SIZE[0]-1):
                print("_", end='')
            else:
                print("|", end='')
        print("")

maze_cpy = maze.copy()
total_way = []

def find_way_bfs(x,y):
    global total_way
    trace = [-1 for i in range(SIZE[0]*SIZE[1])]
    queue = []
    queue.append((x,y))
    trace[0] = -2
    while queue:
        x,y = queue.pop(0)
        dirs = [N, S, W, E]

        if (x == SIZE[0]-1) and (y == SIZE[1] -1):
            way = []
            
            y_ = trace[-1] % SIZE[0]
            x_ = trace[-1] // SIZE[0]

            while x_ != 0 or y_ != 0:
                way.append((x_,y_))
                index = x_ * SIZE[0] + y_
                y_ = trace[index] % SIZE[0]
                x_ = trace[index] // SIZE[0]
        
            total_way.append(way)
            trace = [-1 for i in range(SIZE[0]*SIZE[1])]
            find_way_bfs(0,0)

        for dir in dirs:
            if maze_cpy[x][y] & dir != 0:

                new_x = x + GO_DIR[dir][1]
                new_y = y + GO_DIR[dir][0]
                if (new_x in range(SIZE[0])) and (new_y in range(SIZE[1])) and trace[new_x*SIZE[0]+new_y] == -1:

                    maze_cpy[x][y] ^= dir
                    maze_cpy[new_x][new_y] ^= REVERSE[dir]
                    
                    trace[new_x*SIZE[0]+new_y] = x * SIZE[0] +y
                    queue.append((new_x, new_y))

def print_output(index):
    
    print("_" * (SIZE[0] * 2))
    for j in range(SIZE[1]):
        x = random.randint(0,9)
        if j!=0:
            print("|", end='')
        else:
            print ("_", end='')
        for i in range(SIZE[0]):
            if (maze[j][i] & S != 0):
                if (j,i) in total_way[index]:
                    print("*", end='')
                else:
                    print(" ", end='')
            else:
                if (j,i) in total_way[index]:
                    print("*", end='')
                else:
                    print("_", end='')
            if (maze[j][i] & E != 0):
                if ((maze[j][i] | maze[j][i+1]) & S != 0):
                    if (j,i) in total_way[index]:
                        print("*", end='')
                    else:
                        print(" ", end='')
                else:
                    if (j,i) in total_way[index]:
                        print(" ", end='')
                    else:
                        print("_", end='')
            elif (j==SIZE[1]-1) & (i==SIZE[0]-1):
                print(" ", end='')
            else:
                print("|", end='')
        print("")

arr_scores = list(list(0 for i in range(SIZE[0])) for j in range(SIZE[1]))
def generate_random_scores():
    for i in range(SIZE[0]):
        for j in range(SIZE[1]):
            arr_scores[i][j] = random.randint(-2, 9)

def find_max_score():
    max_score = -100
    i = -1
    index = -1
    for way in total_way:
        i+=1
        score = 0
        for (x,y) in way:
            score += arr_scores[x][y]
            
        if score > max_score:
            max_score = score
            index = i

        
    return index, max_score

if __name__ == '__main__':
    dig(SIZE[0]//2, SIZE[1]//2)
    create_more_way()
    draw()
    find_way_bfs(0,0)
    generate_random_scores()
    
    index, maxscore = find_max_score()
    print_output(index)
    print(total_way)
    #print('max_score = ' + str(maxscore))
    print('finish')