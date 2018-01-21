#!/bin/sh

cat ./logs | grep "CWPGT Pattern test: update WP for gfn" > cat_log
python anl.py ./cat_log 
