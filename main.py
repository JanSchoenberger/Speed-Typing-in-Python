import curses 
from curses import wrapper
# Def steht hier für Define.

def start_screen(stdscr):
    stdscr.clear() 
    stdscr.addstr("Willkommen zu der Speed Typing App :)")
    stdscr.addstr("\nPress any key to begin !") 
    stdscr.refresh()
    stdscr.getkey()

def wpm_test(stdscr):
    target_text = "Hello User, this is a test text for you to write."
    current_text = []
    # Programming can be very hard.
    
    
    while True:
        key = stdscr.getkey()
        
        if ord(key) == 27:
            break # Das ist also die ESC-Taste. Das hat mit ASCII zutun, sehr gut.
        
        
        current_text.append(key) # Ich mag es sehr Fortschritte in Python zu machen.

        stdscr.clear()
        stdscr.addstr(target_text)
        stdscr.refresh()
        
        for char in current_text:
            stdscr.addstr(char, curses.color_pair(1))

        stdscr.refresh()
# Ich habe unter anderem gelernt das programmieren mehr zu lernen.
# Ich will mehr mit Linux arbeiten um Computer besser im Grunde zu begreifen.

# An einem bestimmten Punkt muss man Pausen machen.
# Es ist beeindruckend wie viel mehr man mit Android Programmieren will als mit IOS.
def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
# Änderung für den Intitialen Push. Dafür muss ich denke ich nichtmal soetwas schreiben.
    start_screen(stdscr)
    wpm_test(stdscr)
wrapper(main) 

# Ich werde dieses Programm später in JS übersetzten.