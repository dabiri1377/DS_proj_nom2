# def get_maze_from_user():




# ################### main ################### #

#### get maze
# the first line of input is the number of rows of the array
row_of_maze = int(input("Enter numer of row(s): "))
col_of_maze = int(input("Enter numer of col(s): "))
# guide user
print("now enter colma of maze then perss enter \n")
print("for wall enter 1")
print("for exit point enter $")
print("for empty way enter 0")
print("for start point enter *")
# get maze from user

temp_maze = [[j for j in input().split()] for i in range(row_of_maze)]

# TODO: put something hear to chake the maze

# show maze
for i_1 in range(row_of_maze):
    for j_1 in range(col_of_maze):
        print(temp_maze[i_1][j_1], end=' ')
    print("")

##### find start point
# x of start point
start_point_x = int(0)
# y of start point
start_point_y = int(0)
# flag for chake for more than a start point
flag_for_start_point = 0
# searche for start point in matrix
for i_1 in range(row_of_maze):
    for j_1 in range(col_of_maze):
        if temp_maze[i_1][j_1] == '*':
            if flag_for_start_point == 0:
                # for debug
                print("start point = ", end='')
                print("x= " + str(i_1) + "y= " + str(j_1))
                start_point_x = i_1
                start_point_y = j_1
                flag_for_start_point = 1
            else:
                print("Err: more than 1 start point")

# [x,y] for maze solver
place_of_solver = [start_point_x, start_point_y]
# stack , global
stack_list = []


def check_UDLR(charec):
    # for debug
    print("UDLR")


def check_one_side(charec, map, up, left):
    """

    :param charec:
     place of solver
    :param map: 
     matrix of maze
    :param up: 
     if up == 1 : check up
     if up == 0 : check down
    :param left: 
     if left == 1 : check left
     if left == 0 : check rigth
    :return: 
     1 for dead end 
     2 for exit point
     0 for find a way but no exit point
    """

    # check up is open to check
    if charec[0] - 1 > 0:
        # check up
        if temp_maze[charec[0] - 1][charec[1]] == 0 or temp_maze[charec[0] - 1][charec[1]] == '0':
            stack_list.append([charec[0] - 1][charec[1]])
            # for debug
            print("up is empty")
        if temp_maze[charec[0] - 1][charec[1]] == '$':
            # for debug
            print("find exit")

    # check down is open to check
    if (charec[0] + 1) > 0:
        # check down
        if temp_maze[charec[0] + 1][charec[1]] == 0 or temp_maze[charec[0] + 1][charec[1]] == '0':
            stack_list.append([charec[0] + 1][charec[1]])
            # for debug
            print("down is empty")

    # check left is open to check
    if charec[1] - 1 > 0:
        # check left
        if temp_maze[charec[0]][charec[1] - 1] == 0 or temp_maze[charec[0]][charec[1] - 1] == '0':
            stack_list.append([charec[0]][charec[1] - 1])
            # for debug
            print("left is empty")

    # check right is open to check
    if charec[1] + 1 > 0:
        # check right
        if temp_maze[charec[0]][charec[1] + 1] == 0 or temp_maze[charec[0]][charec[1] + 1] == '0':
            stack_list.append([charec[0]][charec[1] + 1])
            # for debug
            print("right is empty")
