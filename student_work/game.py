# Write your game here

# The goals for this phase include:
# - Pick out some icons for your game
# - Establish a starting position for each icon
# - Pick a size for your playing space
# - Print your playing space with starting position of each icon

# To make this work, you may have to type this into the terminal --> pip install curses
import curses

game_data = {
    'width': 7,
    'height': 7,
    'player': {"x": 3, "y": 3, "score": 0, "energy": 10, "max_energy": 10},
    'rocks': [
        # {"x": 0, "y": 0},
        # {"x": 0, "y": 1},
        # {"x": 0, "y": 2},
        # {"x": 0, "y": 3},
        # {"x": 0, "y": 4},
        # {"x": 0, "y": 5},
        # {"x": 0, "y": 6},
        # {"x": 0, "y": 7},
        # {"x": 1, "y": 0},
        # {"x": 2, "y": 0},
        # {"x": 3, "y": 0},
        # {"x": 4, "y": 0},
        # {"x": 5, "y": 0},
        # {"x": 6, "y": 0},
        # {"x": 7, "y": 0},
        # {"x": 1, "y": 1},
        # {"x": 2, "y": 2},
        # {"x": 3, "y": 3},
        # {"x": 4, "y": 4},
        # {"x": 5, "y": 5},
        # {"x": 6, "y": 6},

    ],
    'passive_face':[
        
    ],

    # ASCII icons
    'turtle': "\U0001F422",
    'rock': "\U0001FAA8 ",
    'leaf': "\U0001F343",
    'passive_face': "\U0001F636 "
}

for i in range(7):
    x = i
    for i in range(7):
        y = i
        game_data['rocks'].append({'x':x,'y':y})

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
            else:
                row += game_data['empty']
        stdscr.addstr(y, 0, row, curses.color_pair(1))

    stdscr.refresh()
    stdscr.getkey()  # pause so player can see board

curses.wrapper(draw_board)

