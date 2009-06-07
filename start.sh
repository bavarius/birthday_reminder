#!/bin/sh -e

# display upcoming birthdays in a terminal (works under xubuntu)
cd python/birthday
xterm -T "Die nächsten Geburtstage" -fn 10x20 -fg yellow -hold +l -uc -wf -e python -u birthday.py
cd ~

exit 0
