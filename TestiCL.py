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
       |\    | \|/ |    /  _     ___      _   \    | (X) |    /|
       | \   |_____|  .','" "', |___|  ,'" "', '.  |_____|  .' |
       |  '-.______.-' /       \ANALOG/       \  '-._____.-'   |
       |               |       |------|       |                |
       |              /\       /      \       /\               |
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
                    stdscr.addstr(4, 112, "     ")
                    stdscr.addstr(4, 112, "_____")
                if event.button == 5:
                    stdscr.addstr(4, 74, "     ")
                    stdscr.addstr(4, 74, "_____")
                if event.button == 6:
                    stdscr.addstr(9, 88, "   ", curses.A_REVERSE)
                if event.button == 7:
                    stdscr.addstr(9, 100, "   ", curses.A_REVERSE)
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
            if event.type == pygame.JOYAXISMOTION:
                if event.axis == 2:
                    if event.value == 1:
                        stdscr.addstr(3, 112, "     ")
                        stdscr.addstr(3, 112, "_____")
                    if event.value < 1:
                        #stdscr.clear()
                        for y, line in enumerate(header.splitlines(), 2):
                            stdscr.addstr(y, 60, line)
                if event.axis == 5:
                    if event.value == 1:
                        stdscr.addstr(3, 74, "     ")
                        stdscr.addstr(3, 74, "_____")
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
