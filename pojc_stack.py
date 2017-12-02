def get_maze_from_user(x_of_maze_for_get_maze):
    """
    get maze from user and return it
    :return:
     maze matrix 
    """

    # guide user
    print("now enter colma of maze then perss enter \n")
    print("for wall enter 1")
    print("for exit point enter $")
    print("for empty way enter 0")
    print("for start point enter *")
    # get maze from user
    temp_maze = [[j for j in input().split()] for _ in range(x_of_maze_for_get_maze)]

    # TODO: put something hear to check the maze

    return temp_maze


def find_start_point(temp_maze, x, y):
    # x of start point
    start_point_x = int(0)
    # y of start point
    start_point_y = int(0)
    # flag for check for more than a start point
    flag_for_start_point = 0
    # searche for start point in matrix
    for i_1 in range(x):
        for j_1 in range(y):
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

    place_of_maze_solver = [start_point_x, start_point_y]
    return place_of_maze_solver


def check_udlr(charec, map, x_max, y_max):
    """
    
    :param charec:
     place of solver
    :param map:
     matrix of maze
    :return: 
     0 for find a way but no exit point and all way pushed into stack
     1 for dead end
     2 for exit point finded and pushed in stack 
    """

    # check up & down & left & right
    # check up
    temp_up = check_one_side(charec, map, 1, 0, x_max, y_max)
    # check down
    temp_down = check_one_side(charec, map, -1, 0, x_max, y_max)
    # check left
    temp_left = check_one_side(charec, map, 0, 1, x_max, y_max)
    # check right
    temp_right = check_one_side(charec, map, 0, -1, x_max, y_max)

    # sum of temp's
    temp_sum = temp_up + temp_right + temp_left + temp_down
    if temp_down == 2 or temp_left == 2 or temp_right == 2 or temp_up == 2:
        # for debug
        print("UDLR find exit")

        return 2
    elif temp_sum == 4:
        # for debug
        print("UDLR find deadend")

        return 1
    else:
        # for debug
        print("UDLR find a way")

        return 0


def check_one_side(charec, map, up, left, x_max_maze, y_max_maze):
    """

    :param charec:
     place of solver
    :param map: 
     matrix of maze
    :param up: 
     if up == 1 : check up
     if up == 0 : check this row
     if up == -1 : check down
    :param left: 
     if left == 1 : check left
     if left == 0 : check this column
     if left == -1 : check right
    :return: 
     0 for find a way but no exit point
     1 for wall 
     2 for exit point
    """

    # make sure 'up' and 'left is int
    up = int(up)
    left = int(left)
    # put solver view in solver_x and solver_y
    solver_x = charec[0] - up
    solver_y = charec[1] - left
    # check edge's
    if solver_x < 0 or solver_x > x_max_maze or solver_y < 0 or solver_y > y_max_maze:
        # for debug
        #print("find wall")
        return 1
    # check
    elif map[solver_x][solver_y] == 0 or map[solver_x][solver_y] == '0':
        # add empty address to stack
        stack_list.append([solver_x, solver_y])
        # for debug
        #print("block is empty")
        return 0
    elif map[solver_x][solver_y] == 1 or map[solver_x][solver_y] == '1':
        # for debug
        #print("find wall")
        return 1
    elif map[solver_x][solver_y] == '$':
        stack_list.append([solver_x, solver_y])
        # for debug
        print("find exit")
        return 2


# ################### main ################### #

# the first line of input is the number of rows of the array
x_of_maze = int(input("Enter number of x(s),row(s): "))
y_of_maze = int(input("Enter number of y(s),col(s): "))

main_maze = get_maze_from_user(x_of_maze)

# show maze
for i_1 in range(x_of_maze):
    for j_1 in range(y_of_maze):
        print(main_maze[i_1][j_1], end=' ')
    print("")

# [x,y] for maze solver
place_of_solver = find_start_point(main_maze, x_of_maze, y_of_maze)

# stack , global
stack_list = []

# for debug test
print("check udlr = ", end='')
print(check_udlr(place_of_solver, main_maze, x_of_maze, y_of_maze))

# flag for while
flag_2 = 0
# this while call house in stack and move solver and make last block '1'
while flag_2 == 0:
    # check stack is empty or not
    if not stack_list:
        # for debug
        print("List is empty")
        flag_2 = 1
    else:
        solver_next_move = stack_list.pop()
        # for debug
        print("solver next move is: " + str(solver_next_move))

        # change 'place_of_solver' block to '1'
        main_maze[place_of_solver[0]][place_of_solver[1]] = int(1)
        # move solver to next house
        place_of_solver = solver_next_move
        # call check_udlr and do all thing for 'solver_next_move' and put result in 'result_of_udlr'
        result_of_udlr = check_udlr(place_of_solver, main_maze, x_of_maze, y_of_maze)


    flag_2 = 1
