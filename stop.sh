#!/bin/bash
ps aux | grep bot.py | grep -v grep | awk '{print($2)}' | xargs kill -9
ps aux | grep webserver.py | grep -v grep | awk '{print($2)}' | xargs kill -9
