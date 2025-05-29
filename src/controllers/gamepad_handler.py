import pygame
import curses
from ..art.ascii_art import (
    HEADER, LS_UP, LS_DOWN, LS_LEFT, LS_RIGHT,
    RS_UP, RS_DOWN, RS_LEFT, RS_RIGHT, OPPOSITES_LR, OPPOSITES_RL,
    OPPOSITES_UD, OPPOSITES_DU, BOTH_LEFT, BOTH_RIGHT, BOTH_UP, BOTH_DOWN,
    LSDOWN_RSLEFT, LSDOWN_RSRIGHT, LSUP_RSLEFT, LSUP_RSRIGHT,
    RSDOWN_LSLEFT, RSDOWN_LSRIGHT, RSUP_LSLEFT, RSUP_LSRIGHT
)

class GamepadHandler:
    def __init__(self):
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
        if event.button == 0:
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

    def handle_joystick_hat_motion(self, stdscr, event):
        """Handle D-pad input events."""
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
        if event.axis == 0:  # Left stick X
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

        if event.axis == 1:  # Left stick Y
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

        if event.axis == 3:  # Right stick X
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

        if event.axis == 4:  # Right stick Y
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

        if event.axis == 2:  # Left trigger
            if event.value == 1:
                stdscr.addstr(3, 74, "     ")
                stdscr.addstr(3, 74, "_____")
            if event.value < 1:
                for y, line in enumerate(HEADER.splitlines(), 2):
                    stdscr.addstr(y, 60, line)

        if event.axis == 5:  # Right trigger
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
