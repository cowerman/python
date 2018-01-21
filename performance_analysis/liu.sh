#!/bin/sh

cat ./logs | grep "your want" > cat_log
python anl.py ./cat_log 
