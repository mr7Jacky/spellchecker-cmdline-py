import time
import sys

toolbar_width = 50

# setup toolbar
sys.stdout.write("% 4.2f%%|%s|" % (0,(" " * toolbar_width)))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+3)) # return to start of line, after '['

for i in range(toolbar_width):
    time.sleep(0.1) # do real work here
    # update the bar
    sys.stdout.write('\r')
    percent = float((i+1)/toolbar_width) * 100
    sys.stdout.write("% 4.2f%%|%s" % (percent, ("■" * i)))
    sys.stdout.flush()

sys.stdout.write("|\n") # this ends the progress bar
