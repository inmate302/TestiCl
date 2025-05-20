'# coding=utf-8'
import pygame
import curses
from curses import wrapper



def main(stdscr):
    header = """ 
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
    stdscr.clear()
    for y, line in enumerate(header.splitlines(), 2):
        stdscr.addstr(y, 60, line)
    while not done:
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
                # This event will be generated when the program starts for every
                # joystick, filling up the list without needing to create them manually.
                joy = pygame.joystick.Joystick(event.device_index)
                joysticks[joy.get_instance_id()] = joy
                #print(f"Joystick {joy.get_instance_id()} connencted")

            if event.type == pygame.JOYDEVICEREMOVED:
                del joysticks[event.instance_id]
                #print(f"Joystick {event.instance_id} disconnected")


        joystick_count = pygame.joystick.get_count()


        for joystick in joysticks.values():
            jid = joystick.get_instance_id()
            #print(f"Joystick {jid}")


            # Get the name from the OS for the controller/joystick.
            name = joystick.get_name()
            stdscr.addstr(19, 86, name.center(33))
            #print(f"Joystick name: {name}")

            guid = joystick.get_guid()

            power_level = joystick.get_power_level()

            # Usually axis run in pairs, up/down for one, and left/right for
            # the other. Triggers count as axes.
            axes = joystick.get_numaxes()
            #print(f"Number of axes: {axes}")

        for i in range(axes):
                axis = joystick.get_axis(i)
                #print(f"Axis {i} value: {axis:>6.3f}")
          

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