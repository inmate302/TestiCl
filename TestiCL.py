# /// script
# dependencies = [
#   "pygame",
# ]
# ///

'# coding=utf-8'

import pygame
import curses
import time
from curses import wrapper



def main(stdscr):
    # the (r) prefix is to make the string raw, so the backslashes are not treated as escape characters.
    header = r"""
             _=====_                               _=====_      
            / ===== \                             / ===== \     
          +.-'_____'-.---------------------------.-'_____'-.+   
         /   |     |  '.       S O N Y A       .'  |  _  |   \  
        / ___| /|\ |___ \                     / ___| /_\ |___ \ 
       / |      |      | ;  __           _   ; | _         _ | ;
       | | <---   ---> | | |__|         |_:> | ||_|       (_)| |
       | |___   |   ___| ;SELECT       START ; |___       ___| ;
       |\    | \|/ |    / ___    ___     ___  \    | (X) |    /|
       | \   |_____|  .'/.....\ |___|  /.....\ '.  |_____|  .' |
       |  '-.______.-' /.     .\ANALOG/.     .\  '-._____.-'   |
       |               |.     .|------|.     .|                |
       |              /\ ..... /      \ ..... /\               |
       |             /  '.___.'        '.___.'  \              |
       |            /                            \             |
        \          /                              \           / 
         \________/                                \_________/  """
    #                        PS2 CONTROLLER                       

    


    pygame.init()
    joysticks = {}
    done = False
    curses.curs_set(0)
    
    def check_terminal_size():
        max_y, max_x = stdscr.getmaxyx()
        if max_x < 120 or max_y < 30:
            stdscr.clear()
            resize_msg = "Please resize your terminal window to at least 120x30 characters for optimal display"
            y_pos = min(max_y - 2, max_y // 2)
            x_pos = max(0, (max_x - len(resize_msg)) // 2)
            try:
                stdscr.addstr(y_pos, x_pos, resize_msg, curses.A_BOLD)
                stdscr.refresh()
                return False
            except curses.error:
                try:
                    stdscr.addstr(0, 0, "Please resize terminal window", curses.A_BOLD)
                    stdscr.refresh()
                    return False
                except curses.error:
                    return False
        return True

    # Initial size check
    if not check_terminal_size():
        stdscr.getch()
        stdscr.clear()
    
    joystick_count = pygame.joystick.get_count()
    #window_2 = curses.newwin(60, 60, 0, 60)            
    if joystick_count == 0:
        msg = "Please, connect a controller..."
        stdscr.addstr(10, 80, msg, 17)
    else:
        stdscr.clear()
        for y, line in enumerate(header.splitlines(), 2):
            stdscr.addstr(y, 60, line)
    
    curses.start_color()
    curses.init_color(17, 200,200,200)
    pad = curses.newpad(20,42)
    testi = '''
    ███████ ███  ██████████ ██ ██████ ██    
    █ ███ █ █    ██ ██  ██  ██ ███ ██ ██    
      ███   ██    ██    ██  ██ ███    ██    
      ███   ██   █ ██   ██  ██ ███ ██ ██    
      ███   █  █ ██ ██  ██  ██ ███ ██ ██    
      ███   ████ █████  ██  ██ ██  ██ ██   █
      ███                      ███ ██ ██ ███
      ███                      ██████ ██████ 
      
      
      
      
      
      
    A CLI gamepad input tester
      '''
        
    stdscr.refresh()
    for y, line in enumerate(testi.splitlines(), 2):
        pad.addstr(y, 0, line, 17)
    

        
    for i in range(20):
        #stdscr.clear()
        stdscr.refresh()
        pad.refresh(0, 2, 0, 0, i, 42)
        time.sleep(0.1)
        if i == 16:
            continue
    
#    thumbsticks = curses.newpad(8,25) ##### wanted to be fancy with it and use pads and windows and shit... 
#					     but shit kept erroring out.
#    thumbstickLup = r"""
# /.....   ___     ___  \
#'.     . |___|  /.....\ 
#/.     .\ANALOG/.     .\
#| ..... |------|.     .| 
#\       /      \ ..... /
# '.___.'        '.___.' """
#
##########################################################################################################
#
#
#  Here's where the stuff for the thumbsticks will go.
#   
#
##########################################################################################################

    #######################   LS UP   #######################
    ls_up = r"""
       |\    | \|/ |    /.....   ___     ___  \    | (X) |    /|
       | \   |_____|  .'.     . |___|  /.....\ '.  |_____|  .' |
       |  '-.______.-' /.     .\ANALOG/.     .\  '-._____.-'   |
       |               | ..... |------|.     .|                |
       |              /\       /      \ ..... /\               |
       |             /  '.___.'        '.___.'  \              |"""
    
    #######################  LS DOWN  #######################
    ls_down = r"""
       |\    | \|/ |    / ___    ___     ___  \    | (X) |    /|
       | \   |_____|  .'/     \ |___|  /.....\ '.  |_____|  .' |
       |  '-.______.-' / ..... \ANALOG/.     .\  '-._____.-'   |
       |               |.     .|------|.     .|                |
       |              /\.     ./      \ ..... /\               |
       |             /  '.....'        '.___.'  \              |"""
    
    #######################  LS LEFT  $$#####################
    ls_left = r"""
       |\    | \|/ |    / ___    ___     ___  \    | (X) |    /|
       | \   |_____|  .....   \ |___|  /.....\ '.  |_____|  .' |
       |  '-.______.-.     .   \ANALOG/.     .\  '-._____.-'   |
       |             .     .   |------|.     .|                |
       |              .....    /      \ ..... /\               |
       |             /  '.___.'        '.___.'  \              |"""

    ######################  LS RIGHT  #######################
    ls_right = r"""
       |\    | \|/ |    / ___    ___     ___  \    | (X) |    /|
       | \   |_____|  .'/   .....___|  /.....\ '.  |_____|  .' |
       |  '-.______.-' /   .     .ALOG/.     .\  '-._____.-'   |
       |               |   .     .----|.     .|                |
       |              /\    .....     \ ..... /\               |
       |             /  '.___.'        '.___.'  \              |"""

    #######################   RS UP   #######################
    rs_up = r"""
       |\    | \|/ |    / ___    ___    ..... \    | (X) |    /|
       | \   |_____|  .'/.....\ |___|  .     . '.  |_____|  .' |
       |  '-.______.-' /.     .\ANALOG/.     .\  '-._____.-'   |
       |               |.     .|------| ..... |                |
       |              /\ ..... /      \       /\               |
       |             /  '.___.'        '.___.'  \              |"""

    #######################  RS DOWN  #######################
    rs_down = r"""
       |\    | \|/ |    / ___    ___     ___  \    | (X) |    /|
       | \   |_____|  .'/.....\ |___|  /     \ '.  |_____|  .' |
       |  '-.______.-' /.     .\ANALOG/ ..... \  '-._____.-'   |
       |               |.     .|------|.     .|                |
       |              /\ ..... /      \.     ./\               |
       |             /  '.___.'        '.....'  \              |"""

    #######################  RS LEFT  #######################
    rs_left = r"""
       |\    | \|/ |    / ___    ___     ___  \    | (X) |    /|
       | \   |_____|  .'/.....\ |___|.....   \ '.  |_____|  .' |
       |  '-.______.-' /.     .\ANAL.     .   \  '-._____.-'   |
       |               |.     .|----.     .   |                |
       |              /\ ..... /     .....    /\               |
       |             /  '.___.'        '.___.'  \              |"""

    ######################  RS RIGHT  #######################
    rs_right = r"""
       |\    | \|/ |    / ___    ___     ___  \    | (X) |    /|
       | \   |_____|  .'/.....\ |___|  /   ......  |_____|  .' |
       |  '-.______.-' /.     .\ANALOG/   .     .'-._____.-'   |
       |               |.     .|------|   .     .              |
       |              /\ ..... /      \    .....               |
       |             /  '.___.'        '.___.'  \              |"""

    ######################  BOTH LEFT  $#####################
    both_left = r""" 
       |\    | \|/ |    / ___    ___     ___  \    | (X) |    /|
       | \   |_____|  .....   \ |___|.....   \ '.  |_____|  .' |
       |  '-.______.-.     .   \ANAL.     .   \  '-._____.-'   |
       |             .     .   |----.     .   |                |
       |              .....    /     .....    /\               |
       |             /  '.___.'        '.___.'  \              |"""


    ######################  BOTH RIGHT  #####################
    both_right = r"""
       |\    | \|/ |    / ___    ___     ___  \    | (X) |    /|
       | \   |_____|  .'/   .....___|  /   ......  |_____|  .' |
       |  '-.______.-' /   .     .ALOG/   .     .'-._____.-'   |
       |               |   .     .----|   .     .              |
       |              /\    .....     \    .....               |
       |             /  '.___.'        '.___.'  \              |"""

    ######################   BOTH UP   ######################
    both_up = r"""
       |\    | \|/ |    /.....   ___    ..... \    | (X) |    /|
       | \   |_____|  .'.     . |___|  .     . '.  |_____|  .' |
       |  '-.______.-' /.     .\ANALOG/.     .\  '-._____.-'   |
       |               | ..... |------| ..... |                |
       |              /\       /      \       /\               |
       |             /  '.___.'        '.___.'  \              |"""

    ######################  BOTH DOWN  #####################
    both_down = r"""
       |\    | \|/ |    / ___    ___     ___  \    | (X) |    /|
       | \   |_____|  .'/     \ |___|  /     \ '.  |_____|  .' |
       |  '-.______.-' / ..... \ANALOG/ ..... \  '-._____.-'   |
       |               |.     .|------|.     .|                |
       |              /\.     ./      \.     ./\               |
       |             /  '.....'        '.....'  \              |"""

            
    while not done:
        # Check terminal size at the start of each loop iteration
        if not check_terminal_size():
            stdscr.getch()
            stdscr.clear()
            continue

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True  # Flag that we are done so we exit this loop.

            if event.type == pygame.JOYBUTTONDOWN:
                #print("Joystick button pressed.")
                if event.button == 0:
                    joystick = joysticks[event.instance_id]
                    stdscr.addstr(11, 113, "   ", curses.A_REVERSE)
                if event.button == 1:
                    stdscr.addstr(9, 118, "   ", curses.A_REVERSE)
                if event.button == 2:
                    stdscr.addstr(9, 108, "   ", curses.A_REVERSE)
                if event.button == 3:
                    stdscr.addstr(7, 113, "   ", curses.A_REVERSE)
                if event.button == 4:
                    stdscr.addstr(4, 74, "     ")
                    stdscr.addstr(4, 74, "_____")
                if event.button == 5:
                    stdscr.addstr(4, 112, "     ")
                    stdscr.addstr(4, 112, "_____")
                if event.button == 6:
                    stdscr.addstr(9, 88, "   ", curses.A_REVERSE)
                if event.button == 7:
                    stdscr.addstr(9, 100, "   ", curses.A_REVERSE)
                if event.button == 8:
                    stdscr.addstr(9, 86, "", curses.A_REVERSE)
                if event.button == 9:
                    stdscr.addstr(14, 87, "LS")
                if event.button == 10:
                    stdscr.addstr(14, 101, "RS")
            if event.type == pygame.JOYHATMOTION:
                if event.hat == 0:
                    if event.value == (-1,0):
                        stdscr.addstr(9, 71, "   ", curses.A_REVERSE)
                    if event.value == (-1,1):
                        stdscr.addstr(9, 71, "   ", curses.A_REVERSE)
                        stdscr.addstr(7, 75, "   ", curses.A_REVERSE)
                    if event.value == (-1,-1):
                        stdscr.addstr(9, 71, "   ", curses.A_REVERSE)
                        stdscr.addstr(11, 75, "   ", curses.A_REVERSE)
                    if event.value == (1,0):
                        stdscr.addstr(9, 79, "   ", curses.A_REVERSE)
                    if event.value == (1,1):
                        stdscr.addstr(9, 79, "   ", curses.A_REVERSE)
                        stdscr.addstr(7, 75, "   ", curses.A_REVERSE)
                    if event.value == (1,-1):
                        stdscr.addstr(9, 79, "   ", curses.A_REVERSE)
                        stdscr.addstr(11, 75, "   ", curses.A_REVERSE)
                    if event.value == (0,-1):
                        stdscr.addstr(11, 75, "   ", curses.A_REVERSE)
                    if event.value == (0,1):
                        stdscr.addstr(7, 75, "   ", curses.A_REVERSE)
                    if event.value == (0,0):
                        #stdscr.clear()
                        for y, line in enumerate(header.splitlines(), 2):
                            stdscr.addstr(y, 60, line)

#######################   Left and right thumbsticks go down here    #########################################################

            if event.type == pygame.JOYAXISMOTION:
                if event.axis == 0:
                    if event.value >= 0 and event.value != 1:
                        for y, line in enumerate(header.splitlines(), 2):
                            stdscr.addstr(y, 60, line)
                            stdscr.refresh()
                    if event.value == 1:
                        for y, line in enumerate(ls_right.splitlines(), 2):
                            stdscr.addstr(y+8, 60, line)
                            stdscr.refresh()
                    if event.value < 0:
                        for y, line in enumerate(ls_left.splitlines(), 2):
                            stdscr.addstr(y+8, 60, line)
                            stdscr.refresh()
                    
                    #if event.value < 1:
                        #stdscr.clear()
                       # for y, line in enumerate(header.splitlines(), 2):
                           # stdscr.addstr(y, 60, line)
                if event.axis == 1:
                    for y, line in enumerate(header.splitlines(), 2):
                        stdscr.addstr(y, 60, line)
                        stdscr.refresh()
                    if event.value > 0 and event.value > 0.800:
                        for y, line in enumerate(ls_down.splitlines(), 2):
                            stdscr.addstr(y+8, 60, line)
                            stdscr.refresh()
                    elif event.value < -0.5:
                    	for y, line in enumerate(ls_up.splitlines(), 2):
                            stdscr.addstr(y+8, 60, line)
                            stdscr.refresh()
                           # for y, line in enumerate(thumbstickLup.splitlines(), 2):
                               # thumbsticks.addstr(y, 0, line)
                                #thumbsticks.refresh(0, 0, 9, 83, 16, 108)
                
                if event.axis == 3:
                    if event.value >= 0 and event.value != 1:
                        for y, line in enumerate(header.splitlines(), 2):
                            stdscr.addstr(y, 60, line)
                            stdscr.refresh()
                    if event.value == 1:
                        for y, line in enumerate(rs_right.splitlines(), 2):
                            stdscr.addstr(y+8, 60, line)
                            stdscr.refresh()
                    if event.value < 0:
                        for y, line in enumerate(rs_left.splitlines(), 2):
                            stdscr.addstr(y+8, 60, line)
                            stdscr.refresh()
                    
                if event.axis == 4:
                    for y, line in enumerate(header.splitlines(), 2):
                        stdscr.addstr(y, 60, line)
                        stdscr.refresh()
                    if event.value > 0 and event.value > 0.800:
                        for y, line in enumerate(rs_down.splitlines(), 2):
                            stdscr.addstr(y+8, 60, line)
                            stdscr.refresh()
                    elif event.value < -0.5:
                    	for y, line in enumerate(rs_up.splitlines(), 2):
                            stdscr.addstr(y+8, 60, line)
                            stdscr.refresh()     
             
#############################    Left and right triggers go down here    #########################################################

                if event.axis == 2:
                    if event.value == 1:
                        stdscr.addstr(3, 74, "     ")
                        stdscr.addstr(3, 74, "_____")
                    if event.value < 1:
                        #stdscr.clear()
                        for y, line in enumerate(header.splitlines(), 2):
                            stdscr.addstr(y, 60, line)
                if event.axis == 5:
                    if event.value == 1:
                        stdscr.addstr(3, 112, "     ")
                        stdscr.addstr(3, 112, "_____")
                    if event.value < 1:
                        #stdscr.clear()
                        for y, line in enumerate(header.splitlines(), 2):
                            stdscr.addstr(y, 60, line)
                    #if joystick.rumble(0, 0.7, 500):
                        #print(f"Rumble effect played on joystick {event.instance_id}")

            if event.type == pygame.JOYBUTTONUP:
                #stdscr.clear()
                for y, line in enumerate(header.splitlines(), 2):
                    stdscr.addstr(y, 60, line)

            # Handle hotplugging
            if event.type == pygame.JOYDEVICEADDED:
                joy = pygame.joystick.Joystick(event.device_index)
                joysticks[joy.get_instance_id()] = joy
                stdscr.refresh()
                for y, line in enumerate(header.splitlines(), 2):
                    stdscr.addstr(y, 60, line)

            if event.type == pygame.JOYDEVICEREMOVED:
                del joysticks[event.instance_id]
                stdscr.refresh()
                msg = "Please, connect a controller..."
                stdscr.addstr(10, 80, msg, 17)


        joystick_count = pygame.joystick.get_count()
        
	
        for joystick in joysticks.values():
            jid = joystick.get_instance_id()
                        

                #window_2.addstr(14, 86, msg, 17)
            #print(f"Joystick {jid}")
            
            #window_1 = curses.newwin(3, 40, 20, 60)
            #window_1.refresh()
		
            # Get the name from the OS for the controller/joystick.
            name = joystick.get_name()
            try:
                # Truncate name if it's too long (max 30 characters)
                display_name = name[:30] if len(name) > 30 else name
                stdscr.addstr(20, 86, display_name, 17)
            except curses.error:
                # If we still get an error, try a different position
                try:
                    stdscr.addstr(20, 60, display_name, 17)
                except curses.error:
                    pass  # Silently fail if  still can't display it
            #TODO: we still need to properly represent the ascii art with resizing.

            guid = joystick.get_guid()

            power_level = joystick.get_power_level()


            axes = joystick.get_numaxes()

            for i in range(axes):
                axis = joystick.get_axis(i)
          

        #buttons = ["A","B","X","Y","LB","RB","LT","RT","Select", "Start"]
        #buttons = joystick.get_numbuttons()

        #for i in range(buttons):
         #   button = joystick.get_button(i)
            #if button == 1:
                #stdscr.addstr(11, 113, "   ", curses.A_REVERSE)
                #stdscr.refresh()

        stdscr.refresh()
        #stdscr.getch()

wrapper(main)
