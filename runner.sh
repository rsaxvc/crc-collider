#!/bin/sh
cat english-words/words*.txt | awk '{print tolower($0)}' | sort | uniq | python collision_checker.py

