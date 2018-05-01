#!/bin/sh
echo "starting"
echo "++++++++++++++++++++++++++++++++++"
git add .
echo "add finish!"
echo "++++++++++++++++++++++++++++++++++"
echo "Input commit words:"  
read input  
git commit -m "$input" 
echo "commit done!"
echo "++++++++++++++++++++++++++++++++++"
git push origin master
echo "push done!"
echo "++++++++++++++++++++++++++++++++++"
echo "finish, great job!"
