import sys,os
import curses

def draw_menu(stdscr):
    k = 0
    cursor_x = 0
    cursor_y = 0

    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    selectMenu = 0

    # Loop where k is the last character pressed
    while (k != ord('q')):

        # Initialization
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        menuItems = [
            "menu 1",
            "menu 2",
            "menu 3",
            "menu 4",
            "exit"
        ]

        # Start colors in curses
        curses.start_color()
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
        curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_GREEN)

        if k == curses.KEY_DOWN:
            selectMenu += 1
        elif k == curses.KEY_UP:
            selectMenu -= 1
        elif k == 10:
            if selectMenu == len(menuItems) - 1:
                break
            elif selectMenu == 0:
                import newgame
                newgame.start(stdscr)

        selectMenu = max(0, selectMenu)
        selectMenu = min(len(menuItems)-1, selectMenu)

        #Рисуем меню
        i = 0
        for item in menuItems:
            start_x = int((width) // 2)  - int(len(item) // 2) - int(len(item) % 2)
            start_y = int(height // 3) - int(len(menuItems) // 2)
            if i == selectMenu:
                stdscr.addstr(start_y + i, start_x, item, curses.color_pair(2))
            else:
                stdscr.addstr(start_y + i, start_x, item)
            i += 1

        # Declaration of strings
        statusbarstr = "Press 'q' to exit | STATUS BAR | Select menu nomber: {} | Menu count: {} | Key press code: {}".format(selectMenu + 1, len(menuItems), k)

        # Render status bar
        stdscr.attron(curses.color_pair(1))
        stdscr.addstr(height-1, 0, statusbarstr)
        stdscr.addstr(height-1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
        stdscr.attroff(curses.color_pair(1))

        # Refresh the screen
        stdscr.refresh()

        # Wait for next input
        k = stdscr.getch()

def main():
    curses.wrapper(draw_menu)

if __name__ == "__main__":
    main()