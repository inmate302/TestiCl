import curses
import time

def check_terminal_size(stdscr):
    """Check if the terminal window is large enough for optimal display."""
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

def display_ascii_art(stdscr, art, start_y=2, start_x=60):
    """Display ASCII art at the specified position."""
    for y, line in enumerate(art.splitlines(), start_y):
        stdscr.addstr(y, start_x, line)
    stdscr.refresh()

def display_logo(stdscr, logo, pad):
    """Display the logo using a pad for scrolling effect."""
    for y, line in enumerate(logo.splitlines(), 2):
        pad.addstr(y, 0, line, 17)
    
    for i in range(20):
        stdscr.refresh()
        pad.refresh(0, 2, 0, 0, i, 42)
        time.sleep(0.1)
        if i == 16:
            continue

def display_controller_name(stdscr, name, y_pos=20, x_pos=86):
    """Display the controller name, handling long names."""
    try:
        # Truncate name if it's too long (max 30 characters)
        display_name = name[:30] if len(name) > 30 else name
        stdscr.addstr(y_pos, x_pos, display_name, 17)
    except curses.error:
        # If we still get an error, try a different position
        try:
            stdscr.addstr(y_pos, 60, display_name, 17)
        except curses.error:
            pass  # Silently fail if still can't display it 