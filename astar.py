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
    result = messagebox.askokcancel('Path Found', ('Shortest costing path costs: '+ str(lowest_cost_node.cost) + '\n would you like to re run the program?'))
    if result == True:
        main(width, height, dims, diagonal_cost, adjacent_cost)
    else:
        pygame.quit()
    
    return path