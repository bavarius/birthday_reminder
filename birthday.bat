@ECHO OFF
TITLE Anstehende Geburtstage
COLOR 2E
SET PROG_PATH=D:\Projekte\GitPlayground\birthday_reminder
python %PROG_PATH%\birthday.py -c %PROG_PATH%\format_template.csv
