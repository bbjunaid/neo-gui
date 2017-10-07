#!/bin/sh

rm scripts/commands/neo_restart_sync
git add .
git commit -am 'removing restart command'
git push origin master
