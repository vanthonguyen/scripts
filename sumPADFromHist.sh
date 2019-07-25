#!/bin/sh
awk 'NR > 11 {sum += $6} END {print sum}' $1
