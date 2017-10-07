#!/bin/sh

ps -W | grep "neo-gui" | awk '{print $1}' | xargs kill -f
