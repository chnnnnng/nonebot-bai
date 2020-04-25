#!/bin/bash
echo "START PULLING FROM GIT"
git pull origin master
echo "PULL DONE, RESTART"
ps aux | grep bot.py | grep -v grep | awk '{print($2)}' | xargs kill -9
python bot.py
echo "DONE."