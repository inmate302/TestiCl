# /// script
# dependencies = [
#   "pygame",
# ]
# ///

'# coding=utf-8'

import curses
import pygame
import random
from curses import wrapper
from .art.ascii_art import HEADER, LOGO
from .utils.terminal import (
    check_terminal_size,
    display_ascii_art,
    display_logo,
    display_controller_name
)
from .controllers.gamepad_handler import GamepadHandler
from .art.quotes import QUOTES

def main(stdscr):
    # Initialize curses
    curses.curs_set(0)
    curses.start_color()
    curses.can_change_color()
    curses.use_default_colors()
    curses.termattrs()
    curses.has_extended_color_support()
    curses.init_color(1, 501, 0, 0) #MAROON
    curses.init_color(2, 1000, 1000, 941) #IVORY
    curses.init_color(3, 1000, 956, 309) #LEMON_YELLOW
    curses.init_color(4, 200, 200, 200) #GRAY
    curses.init_color(5, 576, 800, 917) #BABY_BLUE
    curses.init_color(6, 0, 0, 501) #NAVY_BLUE
    curses.init_color(7, 223, 1000, 78) #GREEN
    curses.init_pair(1, curses.COLOR_BLACK, 3)
    curses.init_pair(2, curses.COLOR_WHITE, 4)    
    curses.init_pair(3, 2, 1)
    curses.init_pair(4, 1, 2)
    curses.init_pair(5, 2, 5)
    curses.init_pair(6, 2, 6)
    curses.init_pair(7, 7, curses.COLOR_BLACK)
    color_pair_list = (0, 1, 2 ,3)
    stdscr.nodelay(1)
    
    # Create pad for logo
    pad = curses.newpad(20, 44)
    
    # Initialize gamepad handler
    gamepad = GamepadHandler()

    # MOTD or Quotes
    lines = QUOTES.splitlines()
    
    line = random.choice(lines)
    
    # Initial size check
    if not check_terminal_size(stdscr):
        stdscr.getch()
        stdscr.clear()
    
    # Check for connected controllers
    joystick_count = pygame.joystick.get_count()
    if joystick_count == 0:
        msg = "Please, connect a controller..."
        stdscr.addstr(10, 80, msg)
    else:
        stdscr.clear()
        display_ascii_art(stdscr, HEADER)
    
    # Display logo
    display_logo(stdscr, LOGO, pad)
    
    # Main event loop
    while not gamepad.done:
        # Check terminal size at the start of each loop iteration
        if not check_terminal_size(stdscr):
            stdscr.getch()
            stdscr.clear()
        

        stdscr.addstr(26, 6, line, curses.A_ITALIC)
    


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gamepad.done = True
                
            elif event.type == pygame.JOYBUTTONDOWN:
                gamepad.handle_joystick_button_down(stdscr, event)
                
            elif event.type == pygame.JOYHATMOTION:
                gamepad.handle_joystick_hat_motion(stdscr, event)
                
            elif event.type == pygame.JOYAXISMOTION:
                gamepad.handle_joystick_axis_motion(stdscr, event)
                
            elif event.type == pygame.JOYBUTTONUP:
                gamepad.handle_joystick_button_up(stdscr)
                
            elif event.type == pygame.JOYDEVICEADDED:
                gamepad.handle_joystick_device_added(stdscr, event)
                
            elif event.type == pygame.JOYDEVICEREMOVED:
                gamepad.handle_joystick_device_removed(stdscr, event)
            
        # Display controller information
        for joystick in gamepad.joysticks.values():
            name = joystick.get_name()
            display_controller_name(stdscr, name)
            
        stdscr.refresh()

if __name__ == "__main__":
    wrapper(main) 
