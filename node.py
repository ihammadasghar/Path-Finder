from pygame.draw import rect
from pygame.display import update
from math import sqrt

RED = (255, 0, 0)
YELLOW = (247, 224, 12)
ORANGE = (245, 169, 29)

class node:
    def __init__(self, cords, screen, w, h):
        self.cords = cords
        self.cost = 0.0
        self.visited = False
        self.previous = None
        self.screen = screen
        self.width = w
        self.height = h
        self.distance_to_end = 0.0
    
    def show(self, color, st):
        
        rect(self.screen, color, (self.cords[1] * self.width, self.cords[0] * self.height, self.width, self.height), st)
        update()

    def path(self, color, st):
        rect(self.screen, color, (self.cords[1] * self.width, self.cords[0] * self.height, self.width, self.height), st)
        update()
    
def create_path(start, end):
    print("creating path...")
    path = [start]
    node = end    
    while node.cords != start.cords:
        path.append(node)
        node.path(RED, 0)
        node = node.previous
    print("Path created")
    return path


def get_neighbours(node, end, dims, diagonal_cost, adjacent_cost, WIN):
    row = node.cords[0]
    col = node.cords[1]
    #  Neighbours positions
    top = row-1
    bottom = row+1
    left = col-1
    right = col+1
    neighbours = [(top, left), (top, col), (top, right), (row, left), (row, right),  (bottom, left), (bottom, col), (bottom, right)]
    nodes = []
    for i in neighbours:
        #  Check if cords are out of bounds
        if i[0] >= 0 and i[1] >= 0: 
            if i[0] < dims[0] and i[1] < dims[1]:
                n = WIN[i[0]][i[1]]

                #  Calculating distance to end
                start_row = n.cords[0]
                start_col = n.cords[1]
                end_row = end.cords[0]
                end_col = end.cords[1]
                a = end_row - start_row
                b = end_col - start_col

                if end_row - start_row < 0:
                    a = start_row - end_row

                if b < 0:
                    b = start_col - end_col

                distance_to_end = sqrt((a**2)+(b**2))

                #  Calculating cost
                cost = 0.0
                if i[0] != row and i[1] != col:  #if its an edge neighbour
                    cost = node.cost + diagonal_cost
                else:
                    cost = node.cost + adjacent_cost 

                if not n.visited or n.cost > cost:
                    n.cost = cost
                    n.distance_to_end = distance_to_end
                    n.show(YELLOW, 0)
                    n.visited = True
                    n.previous = node
                    nodes.append(n)

    return nodes