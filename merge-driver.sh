#!/bin/sh
# Custom merge driver script to concatenate changes from both branches
# Parameters: %A - current file, %O - base file, %B - other file

echo "Merging $2 (base), $3 (other) into $1 (current)"
# Concatenate changes for simplicity. Adjust as needed for your requirements.
echo '<<<<<<< HEAD' > $1
cat $2 >> $1
echo '=======' >> $1
cat $3 >> $1
echo '>>>>>>>' >> $1
