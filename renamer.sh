#!/usr/bin/env bash
:'
This shell script copies all the jpg files in the directory and returns them
in an ordered pair of file names
'
i=1
for file in *.jpg
do
 mv "$file" "$i".jpg
 i=$(($i+1))
done
