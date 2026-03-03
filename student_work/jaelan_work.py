# The goals for this phase include:
# - Implement player movement (I suggest W/A/S/D or arrow keys).
# - Prevent the player from moving off the board or into obstacles.
# - Track total moves (for high-score).
# - Display the updated board after each move.

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
    'passive_faces':[
        
    ],

    # ASCII icons
    'turtle': "\U0001F422",
    'rock': "\U0001FAA8 ",
    'leaf': "\U0001F343",
    'passive_face': "\U0001F636 ",
    'empty' : "  "
}

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
            # Collectibles
            # Passive Faces
            elif any(o['x'] == x and o['y'] == y for o in game_data['passive_faces']):
                row += game_data['passive_face']
            else:
                row += game_data['empty']
        stdscr.addstr(y, 0, row, curses.color_pair(1))

    stdscr.addstr(game_data['height'] + 1, 0,
                  f"Moves Survived: {game_data['player']['score']}",
                  curses.color_pair(1))
    stdscr.addstr(game_data['height'] + 2, 0,
                  "Move with W/A/S/D, Q to quit",
                  curses.color_pair(1))
    stdscr.refresh()

def move_player(key):
    x = game_data['player']['x']
    y = game_data['player']['y']

    new_x, new_y = x, y
    key = key.lower()

    if key == "w" and y > 1:
        new_y -= 1
    elif key == "s" and y < game_data['height'] - 2:
        new_y += 1
    elif key == "a" and x > 1:
        new_x -= 1
    elif key == "d" and x < game_data['width'] - 2:
        new_x += 1
    else:
        return  # Invalid key or move off board

    # Check for obstacles
    if any(o['x'] == new_x and o['y'] == new_y for o in game_data['rocks']):
        return
    lazer=0

    # Update position and increment score
    game_data['player']['x'] = new_x
    game_data['player']['y'] = new_y
    if lazer == 0:
        game_data['player']['score'] += 1
    #when we go to fire lazer, we put it into stages, as lazer with variable. 
    #Then when its done, and we've survived, we reset to zero and scores update

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)

    draw_board(stdscr)

    while True:
        try:
            key = stdscr.getkey()
        except:
            key = None

        if key:
            if key.lower() == "q":
                break

            move_player(key)
            draw_board(stdscr)

curses.wrapper(main)