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
    'lazer_list':[],

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
    game_data['rocks'].append({'x':a,'y':b})
    game_data['available_x'].remove(a)
    game_data['available_y'].remove(b)

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
            # Collectibles
            # Passive Faces
            elif any(o['x'] == x and o['y'] == y for o in game_data['passive_faces']):
                row += game_data['passive_face']
            elif any(o['x'] == x and o['y'] == y for o in game_data['lazer_list']):
                row -= game_data['passive_face']
                row += game_data['leaf']
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
    elif key ==  "s" and y < game_data['height'] - 2:
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
def lazer_fire():
    lazer=1
    
    for i in range (1,4):
        game_data['lazer_list'].append(random.choice(game_data['passive_faces']))
        # if (o['x'] == x and o['y'] == y for o in lazer_list):
        #         row += game_data['leaf']
    lazer = 2
    

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
            lazer_fire()

curses.wrapper(main)