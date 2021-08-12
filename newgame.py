import curses

def start(stdscr):

    stdscr.clear()
    stdscr.refresh()
    height, width = stdscr.getmaxyx()

    start_x = int((width) // 2)  - int(len("New Game") // 2) - int(len("New Game") % 2)
    start_y = int(height // 3)

    stdscr.addstr(start_y, start_x, "New Game", curses.A_REVERSE)

    # Refresh the screen
    stdscr.refresh()
    # Wait for next input
    k = stdscr.getch()

    stdscr.clear()
    stdscr.refresh()