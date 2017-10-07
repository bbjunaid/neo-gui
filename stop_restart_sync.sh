#!/bin/sh

rm scripts/commands/restart_sync
git add .
git commit -am 'removing restart command'
git push origin master
