import pygame
from tkinter import messagebox
from tkinter import *
from node import create_path, get_neighbours


RED = (255, 0, 0)
YELLOW = (247, 224, 12)
ORANGE = (245, 169, 29)


def find_path(start, end, width, height, dims, diagonal_cost, adjacent_cost, WIN, main):
    print("A* in process...")
    end.show((255, 8, 127), 0)
    start.show((255, 8, 127), 0)
    priority = []
    start.visited = True
    lowest_cost_node = start

    while lowest_cost_node.cords != end.cords:
        neighbours = get_neighbours(lowest_cost_node, end, dims, diagonal_cost, adjacent_cost, WIN)
        for node in neighbours:
            priority.append(node)
        
        lowest_cost_node = priority[0]
        
        for node in priority:
            if  lowest_cost_node.cost + lowest_cost_node.distance_to_end > node.cost + node.distance_to_end:
                lowest_cost_node = node

        lowest_cost_node.show(ORANGE, 0)
        priority.remove(lowest_cost_node)

    end.show((255, 8, 127), 0)
    print("A* completed.")
    path = create_path(start, lowest_cost_node)

    Tk().wm_withdraw()
    result = messagebox.askokcancel('Program Finished', ('The program finished, the shortest distance \n to the path is ' + str(lowest_cost_node.cost) + ' blocks away, \n would you like to re run the program?'))
    if result == True:
        main(width, height, dims, diagonal_cost, adjacent_cost)
    else:
        pygame.quit()
    
    return path


# def create_path(start, end):
#     print("creating path...")
#     path = [start]
#     node = end    
#     while node.cords != start.cords:
#         path.append(node)
#         node.path(RED, 0)
#         node = node.previous
#     print("Path created")
#     return path


# def get_neighbours(node, end, dims, diagonal_cost, adjacent_cost, WIN):
#     row = node.cords[0]
#     col = node.cords[1]
#     #  Neighbours positions
#     top = row-1
#     bottom = row+1
#     left = col-1
#     right = col+1
#     neighbours = [(top, left), (top, col), (top, right), (row, left), (row, right),  (bottom, left), (bottom, col), (bottom, right)]
#     nodes = []
#     for i in neighbours:
#         #  Check if cords are out of bounds
#         if i[0] >= 0 and i[1] >= 0: 
#             if i[0] < dims[0] and i[1] < dims[1]:
#                 n = WIN[i[0]][i[1]]

#                 #  Calculating distance to end
#                 start_row = n.cords[0]
#                 start_col = n.cords[1]
#                 end_row = end.cords[0]
#                 end_col = end.cords[1]
#                 a = end_row - start_row
#                 b = end_col - start_col

#                 if end_row - start_row < 0:
#                     a = start_row - end_row

#                 if b < 0:
#                     b = start_col - end_col

#                 distance_to_end = sqrt((a**2)+(b**2))

#                 #  Calculating cost
#                 cost = 0.0
#                 if i[0] != row and i[1] != col:  #if its an edge neighbour
#                     cost = node.cost + diagonal_cost
#                 else:
#                     cost = node.cost + adjacent_cost 

#                 if not n.visited or n.cost > cost:
#                     n.cost = cost
#                     n.distance_to_end = distance_to_end
#                     n.show(YELLOW, 0)
#                     n.visited = True
#                     n.previous = node
#                     nodes.append(n)

#     return nodes