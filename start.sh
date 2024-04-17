#!/bin/sh -e

# display upcoming birthdays in a terminal (works under xubuntu)
cd python/birthday
xterm -T "Die nächsten Geburtstage" -fn 10x20 -bg black -fg yellow -hold +l -uc -wf -e python2 -u birthday.py
cd ~

exit 0
