from algorithms import astar, dijkstra
import pygame
from node import node
from tkinter import *


RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def main(width, height, dims, diagonal_cost, adjacent_cost):
    global screen
    global WIN
    global start
    global end
    global ALGORITHM
    
    w = width / dims[1]
    h = height / dims[0]

    screen = pygame.display.set_mode((width, height))
    WIN = [[node((i, j), screen, w, h) for j in range(dims[1])] for i in range(dims[0])]
    for i in range(dims[0]):
        for j in range(dims[1]):
            WIN[i][j].show(WHITE, 0)
            WIN[i][j].show(BLACK, 1)

    start, end, ALGORITHM = ask(WIN)

    pygame.init()

    start.show(RED, 0)
    end.show(RED, 0)
    
    loop = True
    while loop:
        ev = pygame.event.get()

        for event in ev:
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
            if pygame.mouse.get_pressed()[0]:
                try:
                    pos = pygame.mouse.get_pos()
                    mousePress(pos, width, height, dims)
                except AttributeError:
                    pass
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    loop = False
                    run_algorithm(width, height, dims, diagonal_cost, adjacent_cost)


def mousePress(x, width, height, dims):
    t = x[1]
    w = x[0]
    g1 = t // (width // dims[1])
    g2 = w // (height // dims[0])
    try:
        acess = WIN[g1][g2]
        if acess != start and acess != end:
            if acess.visited == False:
                acess.show(BLACK, 0)
                acess.visited = True
    except IndexError:
        pass


def run_algorithm(width, height, dims, diagonal_cost, adjacent_cost):
    while True:
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.QUIT:
                pygame.quit()
        
        pygame.display.update()
        if ALGORITHM == "Dijkstra":
            dijkstra.find_path(start, end, width, height, dims, diagonal_cost, adjacent_cost, WIN, main)
        else:
            astar.find_path(start, end, width, height, dims, diagonal_cost, adjacent_cost, WIN, main)


def onsubmit():
    global start
    global end
    global ALGORITHM
    st = startBox.get().split(',')
    ed = endBox.get().split(',')
    start = WIN[int(st[0])-1][int(st[1])-1]
    end = WIN[int(ed[0])-1][int(ed[1])-1]
    ALGORITHM = algorithm.get()
    window.quit()
    window.destroy()


def ask(win):
    global WIN 
    global start
    global end
    global ALGORITHM
    global window
    global startBox
    global endBox
    global algorithm
    WIN = win
    window = Tk()
    label = Label(window, text='Start(Row,Col): ')
    startBox = Entry(window)
    label1 = Label(window, text='End(Row,Col): ')
    endBox = Entry(window)
    algorithm = StringVar(window, "Dijkstra")
    radio1 = Radiobutton(window,  text="Dijkstra", variable=algorithm, value="Dijkstra")
    radio2 = Radiobutton(window,  text="A*", variable=algorithm, value="A*")
    submit = Button(window, text='Submit', command=onsubmit)
    submit.grid(columnspan=2, row=4)
    radio2.grid(row=3, column=2)
    radio1.grid(row=3, column=1)
    label1.grid(row=1, pady=3)
    endBox.insert(0, '50,50')
    endBox.grid(row=1, column=1, pady=3)
    startBox.insert(0, '25,25')
    startBox.grid(row=0, column=1, pady=3)
    label.grid(row=0, pady=3)
    window.update()
    mainloop()
    return start, end, ALGORITHM
