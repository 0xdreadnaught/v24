# Voron 2.6783 - Lilith

This repository contains configuration backups and custom scripts for my Voron 2.4, dubbed Lilith. 
Lilith, the evil daughter of Diablo, parallels 3D printing's dark allure—both look cool and may burn your house down in the middle of the night.

These scripts and configs are not intended for public replication but serve as a cautionary showcase of what not to do with your Voron 2.4.

## Structure

- **Configs**: Contains Klipper configuration files for different printer components.
  - The configuration is divided into supplementary files for easier management and readability.
- **Scripts**: Includes various utility scripts used for enhanced printer operations.
  - Utilizes shell commands and direct MCU socket communication for refined toolhead pathing during resume:
    - Moves X, then Y, then Z to prevent nozzle collisions—unlike Ellis' direct XYZ approach.
- **Temporary Data**: Uses `/tmp/toolhead_position.txt` to store the current toolhead position, critical for custom resume logic.
  - Created by `save_position.sh` if it doesn't exist. 

## Key Components

### Fans Configuration
- **Stepper Driver Cooling**: Employs a 5010 5V blower to cool the Octopus Pro stepper drivers.
- **Nevermore V6**: A carbon filter air purification system (installation pending).
- **Chamber Vortex**: An ongoing project to install dual 5010 5V blowers, aiming to establish a temperature-controlled chamber environment.

### Macros
- **Print Start**: Custom `print_start` macro optimized to mitigate initial extrusion mishaps:
  - Initiates with a small "poop" extrusion at coordinates (5,5,0) to ensure a clean start.
  - Automatically "kicks" this extrusion to the left into a designated bucket to prevent fan interference and print defects.

### Scripts
- **restore_toolhead_pos.sh**: Script that restores the toolhead position using `/tmp/toolhead_position.txt`, ensuring accurate placement post-pause or interruption. This script executes moves in a sequence that prioritizes the mechanical integrity of the print and printer.

## Usage
This repository is intended for backup purposes; adjustments may be necessary for alignment with your specific Klipper setup and printer configuration. Review and modify paths and settings cautiously.

## Contributions
While not designed for direct use, contributions or discussions on improvements are welcome! Feel free to fork, submit pull requests, or open issues if you have enhancements or corrections to suggest.

## Warning
Proceed with caution: Implementing configurations or scripts from this repository should be done at your own risk, with a fire extinguisher readily available.
