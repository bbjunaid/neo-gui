#!/bin/sh

touch scripts/commands/neo_restart_sync
git add .
git commit -am 'adding neo restart command'
git push origin master
