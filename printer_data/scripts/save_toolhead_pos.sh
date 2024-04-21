#!/bin/bash

# Debug for console
echo "Received X:$1 Y:$2 Z:$3"
# Make sure the file exists
touch /tmp/toolhead_position.txt
# Save coords
echo "$1 $2 $3" > /tmp/toolhead_position.txt
