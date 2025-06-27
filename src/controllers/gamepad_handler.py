import pygame
import curses
import os
import sys
from ..art.ascii_art import (
    HEADER, LS_UP, LS_DOWN, LS_LEFT, LS_RIGHT,
    RS_UP, RS_DOWN, RS_LEFT, RS_RIGHT, OPPOSITES_LR, OPPOSITES_RL,
    OPPOSITES_UD, OPPOSITES_DU, BOTH_LEFT, BOTH_RIGHT, BOTH_UP, BOTH_DOWN,
    LSDOWN_RSLEFT, LSDOWN_RSRIGHT, LSUP_RSLEFT, LSUP_RSRIGHT,
    RSDOWN_LSLEFT, RSDOWN_LSRIGHT, RSUP_LSLEFT, RSUP_LSRIGHT,
    LOGO
)
from .controller_mapping import parse_gamecontrollerdb, get_default_mapping


class GamepadHandler:
    def __init__(self,):
        pygame.init()
        self.joysticks = {}
        self.done = False
        self.ls_left = False
        self.ls_right = False
        self.rs_left = False
        self.rs_right = False
        self.ls_up = False
        self.ls_down = False
        self.rs_up = False
        self.rs_down = False
        self.c = 0
        self.name = None
        try:
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()
            self.controller_guid = self.joystick.get_guid()
            self.name = self.joystick.get_name()
            
        except pygame.error:
            self.joystick = None
            self.controller_guid = None
        if getattr(sys, 'frozen', False):
            self.script_dir = os.path.dirname(sys.executable)
        else:
            self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.relative_path = 'gamecontrollerdb.txt'
        self.controller_mappings = parse_gamecontrollerdb(os.path.join(self.script_dir, self.relative_path))
        self.default_mapping = get_default_mapping(self.controller_guid, self.controller_mappings)
        
        """if self.controller_guid not in self.controller_mappings and self.controller_guid != None:
            raise Exception(f"Agregale ESTA {self.controller_guid}, Nelsito")
        elif self.controller_guid == None:
            pass"""

        if self.controller_guid not in self.controller_mappings and self.controller_guid != None:
            nintendont = ("Switch", "Nintendo", "SN30", "SFC", "SNES")
            pureisuteshon = ("PS", "PS2", "PS3", "PS4", "PS5", "playstation")
            for i in self.controller_mappings:
                if any(i in self.name for i in nintendont ):
                    self.default_mapping = {0: '0', 1: '1', 2: '4', 3: '12', 4: '13', 5: '14', 6: '11', 7: '5', 8: '9', 9: '4', 10: '7', 11: '4', 12: '0', 13: '1', 14: '15', 15: '10', 16: '8', 17: '5', 18: '2', 19: '3', 20: '6', 21: '2', 22: '3'}
                elif any(i in self.name for i in pureisuteshon):
                    self.default_mapping = {0: '0', 1: '1', 2: '4', 3: '12', 4: '13', 5: '14', 6: '11', 7: '5', 8: '9', 9: '7', 10: '4', 11: '4', 12: '0', 13: '1', 14: '10', 15: '8', 16: '5', 17: '3', 18: '4', 19: '3', 20: '9', 21: '13', 22: '2', 23: '3'}                
                else:
                    self.default_mapping = {0: '0', 1: '1', 2: '6', 3: '04', 4: '08', 5: '02', 6: '01', 7: '10', 8: '4', 9: '8', 10: '2', 11: '0', 12: '1', 13: '5', 14: '9', 15: '5', 16: '3', 17: '4', 18: '7', 19: '2', 20: '3', 21: '', 22: ''}
        elif self.controller_guid == None:
            pass
        
        """   
        self.controller = None
        try:
            self.joystick = pygame.joystick.Joystick(0)
        except pygame.error:
            pass
        self.controller_guid = self.controller.get_guid()
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.relative_path = '../gamecontrollerdb.txt'
        self.controller_mappings = parse_gamecontrollerdb(os.path.join(self.script_dir, self.relative_path))
        self.default_mapping = get_default_mapping(self.controller_guid, self.controller_mappings)
"""
       
    def update_controller(self):
        try:
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()
            self.controller_guid = self.joystick.get_guid()
            self.controller_mappings = parse_gamecontrollerdb(os.path.join(self.script_dir, self.relative_path))
            self.default_mapping = get_default_mapping(self.controller_guid, self.controller_mappings)
        except pygame.error:
            self.joystick = None
            self.controller_guid = None
            self.controller_mappings = None
            self.default_mapping = None

        if self.controller_guid not in self.controller_mappings and self.controller_guid != None:
            nintendont = ("Switch", "Nintendo", "SN30", "SFC", "SNES")
            pureisuteshon = ("PS", "PS2", "PS3", "PS4", "PS5", "playstation")
            for i in self.controller_mappings:
                if any(i in self.name for i in nintendont ):
                    self.default_mapping = {0: '0', 1: '1', 2: '4', 3: '12', 4: '13', 5: '14', 6: '11', 7: '5', 8: '9', 9: '4', 10: '7', 11: '4', 12: '0', 13: '1', 14: '15', 15: '10', 16: '8', 17: '5', 18: '2', 19: '3', 20: '6', 21: '2', 22: '3'}
                elif any(i in self.name for i in pureisuteshon):
                    self.default_mapping = {0: '0', 1: '1', 2: '4', 3: '12', 4: '13', 5: '14', 6: '11', 7: '5', 8: '9', 9: '7', 10: '4', 11: '4', 12: '0', 13: '1', 14: '10', 15: '8', 16: '5', 17: '3', 18: '4', 19: '3', 20: '9', 21: '13', 22: '2', 23: '3'}
                else:
                    self.default_mapping = {0: '0', 1: '1', 2: '6', 3: '04', 4: '08', 5: '02', 6: '01', 7: '10', 8: '4', 9: '8', 10: '2', 11: '0', 12: '1', 13: '5', 14: '9', 15: '5', 16: '3', 17: '4', 18: '7', 19: '2', 20: '3', 21: '', 22: ''}
        elif self.controller_guid == None:
            pass
        
        
    def check_opposite_movements(self, stdscr):
        """Check for and display opposite thumbstick movements."""
        if (self.ls_left and self.rs_right):
            for y, line in enumerate(OPPOSITES_LR.splitlines(), 2):
                stdscr.addstr(y+8, 60, line)
                stdscr.refresh()
        elif (self.ls_right and self.rs_left):
            for y, line in enumerate(OPPOSITES_RL.splitlines(), 2):
                stdscr.addstr(y+8, 60, line)
                stdscr.refresh()
        elif (self.ls_up and self.rs_down):
            for y, line in enumerate(OPPOSITES_UD.splitlines(), 2):
                stdscr.addstr(y+8, 60, line)
                stdscr.refresh()
        elif (self.ls_down and self.rs_up):
            for y, line in enumerate(OPPOSITES_DU.splitlines(), 2):
                stdscr.addstr(y+8, 60, line)
                stdscr.refresh()
        elif (self.ls_left and self.rs_left):
            for y, line in enumerate(BOTH_LEFT.splitlines(), 2):
                stdscr.addstr(y+8, 60, line)
                stdscr.refresh()
        elif (self.ls_right and self.rs_right):
            for y, line in enumerate(BOTH_RIGHT.splitlines(), 2):
                stdscr.addstr(y+8, 60, line)
                stdscr.refresh()
        elif (self.ls_up and self.rs_up):
            for y, line in enumerate(BOTH_UP.splitlines(), 2):
                stdscr.addstr(y+8, 60, line)
                stdscr.refresh()
        elif (self.ls_down and self.rs_down):
            for y, line in enumerate(BOTH_DOWN.splitlines(), 2):
                stdscr.addstr(y+8, 60, line)
                stdscr.refresh()
        else:
            for y, line in enumerate(HEADER.splitlines(), 2):
                stdscr.addstr(y, 60, line)
                stdscr.refresh()

    def check_both_movements(self, stdscr):
        """Check for and display same thumbstick movements."""
        if (self.ls_left and self.rs_left):
            for y, line in enumerate(BOTH_LEFT.splitlines(), 2):
                stdscr.addstr(y+8, 60, line)
                stdscr.refresh()
        elif (self.ls_right and self.rs_right):
            for y, line in enumerate(BOTH_RIGHT.splitlines(), 2):
                stdscr.addstr(y+8, 60, line)
                stdscr.refresh()
        elif (self.ls_up and self.rs_up):
            for y, line in enumerate(BOTH_UP.splitlines(), 2):
                stdscr.addstr(y+8, 60, line)
                stdscr.refresh()
        elif (self.ls_down and self.rs_down):
            for y, line in enumerate(BOTH_DOWN.splitlines(), 2):
                stdscr.addstr(y+8, 60, line)
                stdscr.refresh()
        else:
            for y, line in enumerate(HEADER.splitlines(), 2):
                stdscr.addstr(y, 60, line)
                stdscr.refresh()

    def check_other_movements(self, stdscr):
        """Check for and display other thumbstick simultaneous movements."""
        if (self.ls_down and self.rs_left):
            for y, line in enumerate(LSDOWN_RSLEFT.splitlines(), 2):
                stdscr.addstr(y+8, 60, line)
                stdscr.refresh()
        elif (self.ls_down and self.rs_right):
            for y, line in enumerate(LSDOWN_RSRIGHT.splitlines(), 2):
                stdscr.addstr(y+8, 60, line)
                stdscr.refresh()
        elif (self.ls_up and self.rs_left):
            for y, line in enumerate(LSUP_RSLEFT.splitlines(), 2):
                stdscr.addstr(y+8, 60, line)
                stdscr.refresh()
        elif (self.ls_up and self.rs_right):
            for y, line in enumerate(LSUP_RSRIGHT.splitlines(), 2):
                stdscr.addstr(y+8, 60, line)
                stdscr.refresh()
        elif (self.rs_down and self.ls_left):
            for y, line in enumerate(RSDOWN_LSLEFT.splitlines(), 2):
                stdscr.addstr(y+8, 60, line)
                stdscr.refresh()
        elif (self.rs_down and self.ls_right):
            for y, line in enumerate(RSDOWN_LSRIGHT.splitlines(), 2):
                stdscr.addstr(y+8, 60, line)
                stdscr.refresh()
        elif (self.rs_up and self.ls_left):
            for y, line in enumerate(RSUP_LSLEFT.splitlines(), 2):
                stdscr.addstr(y+8, 60, line)
                stdscr.refresh()
        elif (self.rs_up and self.ls_right):
            for y, line in enumerate(RSUP_LSRIGHT.splitlines(), 2):
                stdscr.addstr(y+8, 60, line)
                stdscr.refresh()
        else:
            for y, line in enumerate(HEADER.splitlines(), 2):
                stdscr.addstr(y, 60, line)
                stdscr.refresh()


    def handle_joystick_button_down(self, stdscr, event):
        """Handle joystick button press events."""
        self.update_controller()
        A = int(self.default_mapping[0][0])
        B = int(self.default_mapping[1][0])
        back = int(self.default_mapping[2][0])
        guide = int(self.default_mapping[7][0])
        leftshoulder = int(self.default_mapping[8][0])
        leftstick = int(self.default_mapping[9][0])
        rightshoulder = int(self.default_mapping[13][0])
        rightstick = int(self.default_mapping[14][0])
        start = int(self.default_mapping[18][0])
        X = int(self.default_mapping[19][0])
        Y = int(self.default_mapping[20][0])
        lefttrigger = int(self.default_mapping[10][0])
        righttrigger = int(self.default_mapping[15][0])
        
        if event.button == A:
            stdscr.addstr(11, 113, "   ", curses.A_REVERSE)
        if event.button == B:
            stdscr.addstr(9, 118, "   ", curses.A_REVERSE)
        if event.button == X:
            stdscr.addstr(9, 108, "   ", curses.A_REVERSE)
        if event.button == Y:
            stdscr.addstr(7, 113, "   ", curses.A_REVERSE)
        if event.button == leftshoulder:
            stdscr.addstr(4, 74, "     ")
            stdscr.addstr(4, 74, "_____")
        if event.button == rightshoulder:
            stdscr.addstr(4, 112, "     ")
            stdscr.addstr(4, 112, "_____")
        if event.button == lefttrigger:
            stdscr.addstr(3, 74, "     ")
            stdscr.addstr(3, 74, "_____")
        if event.button == righttrigger:
            stdscr.addstr(3, 112, "     ")
            stdscr.addstr(3, 112, "_____")
        if event.button == back:
            stdscr.addstr(9, 88 , "   ", curses.A_REVERSE)
        if event.button == start:
            stdscr.addstr(9, 100, "   ", curses.A_REVERSE)
        if event.button == guide:
            stdscr.addstr(12, 93, "   ", curses.A_REVERSE)
        if event.button == leftstick:
            stdscr.addstr(14, 87, "L3")
        if event.button == rightstick:
            stdscr.addstr(14, 101, "R3")
        if event.button == leftstick and event.button == rightstick or event.button == back:
            stdscr.bkgd(curses.color_pair(self.c))
            for y, line in enumerate(LOGO.splitlines(), 2):
                stdscr.addstr(y, 0, line)
                stdscr.refresh()
            stdscr.refresh()
            self.c += 1
            if self.c > 15:
                stdscr.bkgd(curses.color_pair(0))
                for y, line in enumerate(LOGO.splitlines(), 2):
                    stdscr.addstr(y, 0, line)
                    stdscr.refresh()
                stdscr.refresh()
                self.c = 0
                

    def handle_joystick_hat_motion(self, stdscr, event):
        """Handle D-pad input events."""
        self.update_controller()
        dpdown = self.default_mapping[3][0]
        dpleft = self.default_mapping[4][0]
        dpright = self.default_mapping[5][0]
        dpup = self.default_mapping[6][0]
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
                for y, line in enumerate(HEADER.splitlines(), 2):
                    stdscr.addstr(y, 60, line)

    def handle_joystick_axis_motion(self, stdscr, event):
        """Handle analog stick and trigger input events."""
        #self.update_controller()
        leftx = int(self.default_mapping[11][0])
        lefty = int(self.default_mapping[12][0])
        lefttrigger = int(self.default_mapping[10][0])
        rightx = int(self.default_mapping[16][0])
        righty = int(self.default_mapping[17][0])
        righttrigger = int(self.default_mapping[15][0])

        if event.axis == leftx:  # Left stick X
            self.ls_left = event.value < 0
            self.ls_right = event.value == 1
            #if not (self.ls_left or self.ls_right):
            for y, line in enumerate(HEADER.splitlines(), 2):
                    stdscr.addstr(y, 60, line)
                    stdscr.refresh()
            if self.ls_right:
                for y, line in enumerate(LS_RIGHT.splitlines(), 2):
                    stdscr.addstr(y+8, 60, line)
                    stdscr.refresh()
            elif self.ls_left:
                for y, line in enumerate(LS_LEFT.splitlines(), 2):
                    stdscr.addstr(y+8, 60, line)
                    stdscr.refresh()
            if (self.ls_left and self.rs_right) or (self.ls_right and self.rs_left):
                self.check_opposite_movements(stdscr)
            if (self.ls_left and self.rs_left) or (self.ls_right and self.rs_right):
                self.check_both_movements(stdscr)
            if (self.rs_down and self.ls_left) or (self.rs_down and self.ls_right) or (self.rs_up and self.ls_left) or (self.rs_up and self.ls_right):
                self.check_other_movements(stdscr)

        if event.axis == lefty:  # Left stick Y
            self.ls_up = event.value < - 0.5
            self.ls_down = event.value > 0.800
            for y, line in enumerate(HEADER.splitlines(), 2):
                stdscr.addstr(y, 60, line)
                stdscr.refresh()
            if event.value > 0 and event.value > 0.800:
                for y, line in enumerate(LS_DOWN.splitlines(), 2):
                    stdscr.addstr(y+8, 60, line)
                    stdscr.refresh()
            elif event.value < -0.5:
                for y, line in enumerate(LS_UP.splitlines(), 2):
                    stdscr.addstr(y+8, 60, line)
                    stdscr.refresh()
            if (self.ls_up and self.rs_down) or (self.ls_down and self.rs_up):
                self.check_opposite_movements(stdscr)
            if (self.ls_up and self.rs_up) or (self.ls_down and self.rs_down):
                self.check_both_movements(stdscr)
            if (self.ls_down and self.rs_left) or (self.ls_down and self.rs_right) or (self.ls_up and self.rs_left) or (self.ls_up and self.rs_right):
                self.check_other_movements(stdscr)

        if event.axis == rightx:  # Right stick X
            self.rs_left = event.value < 0
            self.rs_right = event.value == 1
            #if not (self.rs_left or self.rs_right):
            for y, line in enumerate(HEADER.splitlines(), 2):
                stdscr.addstr(y, 60, line)
                stdscr.refresh()
            if self.rs_right:
                for y, line in enumerate(RS_RIGHT.splitlines(), 2):
                    stdscr.addstr(y+8, 60, line)
                    stdscr.refresh()
            elif self.rs_left:
                for y, line in enumerate(RS_LEFT.splitlines(), 2):
                    stdscr.addstr(y+8, 60, line)
                    stdscr.refresh()
            if (self.ls_right and self.rs_left) or (self.ls_left and self.rs_right):
                self.check_opposite_movements(stdscr)
            if (self.ls_left and self.rs_left) or (self.ls_right and self.rs_right):
                self.check_both_movements(stdscr)
            if (self.ls_down and self.rs_left) or (self.ls_down and self.rs_right) or (self.ls_up and self.rs_left) or (self.ls_up and self.rs_right):
                self.check_other_movements(stdscr)

        if event.axis == righty:  # Right stick Y
            self.rs_up = event.value < - 0.5
            self.rs_down = event.value > 0.800
            for y, line in enumerate(HEADER.splitlines(), 2):
                stdscr.addstr(y, 60, line)
                stdscr.refresh()
            if event.value > 0 and event.value > 0.800:
                for y, line in enumerate(RS_DOWN.splitlines(), 2):
                    stdscr.addstr(y+8, 60, line)
                    stdscr.refresh()
            elif event.value < -0.5:
                for y, line in enumerate(RS_UP.splitlines(), 2):
                    stdscr.addstr(y+8, 60, line)
                    stdscr.refresh()
            if (self.ls_up and self.rs_down) or (self.ls_down and self.rs_up):
                self.check_opposite_movements(stdscr)
            if (self.ls_up and self.rs_up) or (self.ls_down and self.rs_down):
                self.check_both_movements(stdscr)
            if (self.rs_down and self.ls_left) or (self.rs_down and self.ls_right) or (self.rs_up and self.ls_left) or (self.rs_up and self.ls_right):
                self.check_other_movements(stdscr)

        if event.axis == lefttrigger:  # Left trigger
            if event.value == 1:
                stdscr.addstr(3, 74, "     ")
                stdscr.addstr(3, 74, "_____")
            if event.value < 1:
                for y, line in enumerate(HEADER.splitlines(), 2):
                    stdscr.addstr(y, 60, line)

        if event.axis == righttrigger:  # Right trigger
            if event.value == 1:
                stdscr.addstr(3, 112, "     ")
                stdscr.addstr(3, 112, "_____")
            if event.value < 1:
                for y, line in enumerate(HEADER.splitlines(), 2):
                    stdscr.addstr(y, 60, line)

        #self.check_opposite_movements(stdscr)

    def handle_joystick_button_up(self, stdscr):
        """Handle joystick button release events."""
        for y, line in enumerate(HEADER.splitlines(), 2):
            stdscr.addstr(y, 60, line)

    def handle_joystick_device_added(self, stdscr, event):
        """Handle controller connection events."""
        self.update_controller()
        joy = pygame.joystick.Joystick(event.device_index)
        self.joysticks[joy.get_instance_id()] = joy
        stdscr.refresh()
        for y, line in enumerate(HEADER.splitlines(), 2):
            stdscr.addstr(y, 60, line)

    def handle_joystick_device_removed(self, stdscr, event):
        """Handle controller disconnection events."""
        del self.joysticks[event.instance_id]
        stdscr.refresh()
        msg = "Please, connect a controller..."
        stdscr.addstr(10, 80, msg, 17) 
