#!/bin/bash

# The script expects the printer MCU socket path as the first argument
printer_mcu_socket=$1

if [ -z "$printer_mcu_socket" ]; then
    echo "Error: Printer MCU socket path not provided."
    exit 1
fi

# Read the positions from the file
read -r x_pos y_pos z_pos < /tmp/toolhead_position.txt

echo "X:$x_pos"
echo "Y:$y_pos"
echo "Z:$z_pos"

# Move the toolhead relative to its current position
echo "G90" > "$printer_mcu_socket"
echo "G1 X${x_pos} F6000" > "$printer_mcu_socket"
echo "G1 Y${y_pos} F6000" > "$printer_mcu_socket"
#echo "G1 Z${z_pos} F6000" > "$printer_mcu_socket"
#echo "G91" > "$printer_mcu_socket"

