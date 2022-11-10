#!/bin/bash
[ -e output.txt ] && rm output.txt
nohup python -u $1 > output.txt < /dev/null &
echo $! > PID_current.txt