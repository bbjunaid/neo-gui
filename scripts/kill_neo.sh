#!/bin/sh

# kill DEBUG NEO gui only
ps -W | grep "Debug/neo-gui" | awk '{print $1}' | xargs kill -f
