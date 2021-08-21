#!/bin/bash

read -p 'message: ' m 

git add . && git commit -m $m && git push

echo "Your commit message"
echo $m
