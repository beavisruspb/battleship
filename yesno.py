import curses

gtitle = "" 
gtext = ""
gresult = False

def yesno(text, title = ""):
    global gtitle
    global gtext
    global gresult
    gtitle = title
    gtext = text
    curses.wrapper(window)
    
def window(stdscr):
    k = 0
    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    #corsore visible: 0 - invisible
    curses.curs_set(0)

    selectMenu = 0

    while (k != ord("q")):

        # Initialization
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        items = [
            "Yes",
            "No"
        ]        

        # Start colors in curses
        curses.start_color()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_GREEN)
        curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)

        if k == curses.KEY_DOWN:
            selectMenu += 1
        elif k == curses.KEY_UP:
            selectMenu -= 1

        selectMenu = max(0, selectMenu)
        selectMenu = min(len(items)-1, selectMenu)

        start_x = int((width) // 2)  - int(len(gtitle) // 2) - int(len(gtitle) % 2)
        start_y = int(height // 3) - 3

        #Рисуем заголовок
        stdscr.addstr(start_y, start_x, gtitle, curses.color_pair(2))
        start_y += 2

        #Рисуем текст
        start_x = int((width) // 2)  - int(len(gtext) // 2) - int(len(gtext) % 2)
        stdscr.addstr(start_y, start_x, gtext)
        start_y += 2

        #Рисуем меню
        i = 0
        for item in items:
            start_x = int((width) // 2)  - int(len(item) // 2) - int(len(item) % 2)
            if i == selectMenu:
                stdscr.addstr(start_y + i, start_x, item, curses.color_pair(1))
            else:
                stdscr.addstr(start_y + i, start_x, item)
            i += 1

        # Refresh the screen
        stdscr.refresh()

        # Wait for next input
        k = stdscr.getch()

yesno("text", "title")