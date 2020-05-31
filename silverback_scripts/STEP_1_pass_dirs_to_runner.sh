#!/bin/bash

clear

DATADIR="results/"
echo "# Starting..."
echo "# {Details}"

for path in $DATADIR*; do
    [ -d "${path}" ] || continue # if not a directory, skip
    dirname="$(basename "${path}")"
    echo ""
    echo "# Passing: "$dirname
    #passes the directory to the next script.
    bash silverback_scripts/runner_MS_analysis.sh $dirname $DATADIR
    #exit
done
