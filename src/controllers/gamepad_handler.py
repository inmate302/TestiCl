import pygame
import curses
from ..art.ascii_art import (
    HEADER, LS_UP, LS_DOWN, LS_LEFT, LS_RIGHT,
    RS_UP, RS_DOWN, RS_LEFT, RS_RIGHT
)

class GamepadHandler:
    def __init__(self):
        pygame.init()
        self.joysticks = {}
        self.done = False

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
            if event.value >= 0 and event.value != 1:
                for y, line in enumerate(HEADER.splitlines(), 2):
                    stdscr.addstr(y, 60, line)
                    stdscr.refresh()
            if event.value == 1:
                for y, line in enumerate(LS_RIGHT.splitlines(), 2):
                    stdscr.addstr(y+8, 60, line)
                    stdscr.refresh()
            if event.value < 0:
                for y, line in enumerate(LS_LEFT.splitlines(), 2):
                    stdscr.addstr(y+8, 60, line)
                    stdscr.refresh()

        if event.axis == 1:  # Left stick Y
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

        if event.axis == 3:  # Right stick X
            if event.value >= 0 and event.value != 1:
                for y, line in enumerate(HEADER.splitlines(), 2):
                    stdscr.addstr(y, 60, line)
                    stdscr.refresh()
            if event.value == 1:
                for y, line in enumerate(RS_RIGHT.splitlines(), 2):
                    stdscr.addstr(y+8, 60, line)
                    stdscr.refresh()
            if event.value < 0:
                for y, line in enumerate(RS_LEFT.splitlines(), 2):
                    stdscr.addstr(y+8, 60, line)
                    stdscr.refresh()

        if event.axis == 4:  # Right stick Y
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