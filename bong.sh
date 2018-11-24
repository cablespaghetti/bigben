#!/bin/bash
hour=$(date +%-I)
for i in $(seq 1 $hour); do toot+="BONG "; done
/usr/local/bin/toot post "$toot" --media=./images/${hour}.jpg
