# Path-Finder
Visualize the difference between different path finding algorithms

![screenshot](https://github.com/ihammadasghar/Path-Finder/blob/update-readme/screenshots/joint.png)

## Setting up:
1. Clone it `git clone https://github.com/ihammadasghar/path-finder.git`
2. `cd path-finder`
3. Make a virtual environment `python -m venv venv`
4. Activate it `venv\scripts\activate`
5. Download requirements `pip install -r requirements.txt`
6. Run Path Finder: `python program.py`
NOTE: If the python/pip commands don't work for you try `python3` and `pip3` or `py` (python version issues)
 
## Instructions:
1. Specify Start & End node
2. Mouse drag - build walls around the nodes
3. SPACEBAR - Begin search for path

You can also try it on gitpod, but not recomended: [![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/ihammadasghar/Path-Finder)

## Dijkstra:
Searches nodes around it putting the least costing nodes high in priority
## A*:
searches nodes around it while also having a sense of direction towards the end, takes into account the distance to the end node while as well as the cost while prioritizing.

## Advanced Program settings:
If you'd like you could play around with more advanced settings of the program, following settings can be played around with in settings.py.
- Dimensions (Rows, Cols)
- Diagonal Node cost (Changing node cost will effect prioritizing of the algorithm and makes it take interesting paths)
- Adjacent Node cost
- Width & Height of the screen


