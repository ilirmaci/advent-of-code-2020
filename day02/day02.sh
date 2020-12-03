#!/usr/bin/env sh

cat day02_input.txt | tr - ' ' | tr -d : | awk '{split($4, arr, $3); res=(length(arr) - 1); tot += ((res >= $1) && (res <= $2))}; END {print tot}'
cat day02_input.txt | tr - ' ' | tr -d : | awk '{first = substr($4, $1, 1); second = substr($4, $2, 1); res=((first == $3) || (second == $3)) && (first != second); tot += res}; END {print tot}'
