# Write your game here

# The goals for this phase include:
# - Pick out some icons for your game
# - Establish a starting position for each icon
# - Pick a size for your playing space
# - Print your playing space with starting position of each icon

# To make this work, you may have to type this into the terminal --> pip install curses
import curses
import random

game_data = {
    'width': 7,
    'height': 7,
    'player': {"x": 3, "y": 3, "score": 0, "energy": 10, "max_energy": 10},
    'rocks': [
        {"x": 0, "y": 0},
        {"x": 0, "y": 6},
        {"x": 6, "y": 0},
        {"x": 6, "y": 6},
    ],
    'passive_faces':[
        {"x": 0, "y": 1},
        {"x": 0, "y": 2},
        {"x": 0, "y": 3},
        {"x": 0, "y": 4},
        {"x": 0, "y": 5},
        {"x": 1, "y": 0},
        {"x": 1, "y": 6},
        {"x": 2, "y": 0},
        {"x": 2, "y": 6},
        {"x": 3, "y": 0},
        {"x": 3, "y": 6},
        {"x": 4, "y": 0},
        {"x": 4, "y": 6},
        {"x": 5, "y": 0},
        {"x": 5, "y": 6},
        {"x": 6, "y": 1},
        {"x": 6, "y": 2},
        {"x": 6, "y": 3},
        {"x": 6, "y": 4},
        {"x": 6, "y": 5},
    ],

    'available_x': [1, 2, 3, 4, 5], 
    'available_y': [1, 2, 3, 4, 5],

    # ASCII icons
    'turtle': "\U0001F422",
    'rock': "\U0001FAA8 ",
    'leaf': "\U0001F343",
    'passive_face': "\U0001F636",
    'empty': "  "
}

for i in range(4):
    a = game_data['available_x'][random.randint(0,4-i)]
    b = game_data['available_y'][random.randint(0,4-i)]
    print(f"setting rock as x:{a} and y:{b}")
    game_data['rocks'].append({'x':a,'y':b})
    game_data['available_x'].remove(a)
    game_data['available_y'].remove(b)
print(game_data['rocks'])

for i in range(8):
    if game_data['rocks'][i]['x'] == 3 and game_data['rocks'][i]['y'] == 3:
        game_data['player']['y'] = 2

def draw_board(stdscr):
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_WHITE, -1)

    stdscr.clear()
    for y in range(game_data['height']):
        row = ""
        for x in range(game_data['width']):
            # Player
            if x == game_data['player']['x'] and y == game_data['player']['y']:
                row += game_data['turtle']
            # Obstacles
            elif any(o['x'] == x and o['y'] == y for o in game_data['rocks']):
                row += game_data['rock']
            # Passive Faces
            elif any(o['x'] == x and o['y'] == y for o in game_data['passive_faces']):
                row += game_data['passive_face']
            else:
                row += game_data['empty']
        stdscr.addstr(y, 0, row, curses.color_pair(1))

    stdscr.refresh()
    stdscr.getkey()  # pause so player can see board

curses.wrapper(draw_board)

