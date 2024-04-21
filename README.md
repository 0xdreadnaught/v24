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

### Fans
- **Stepper Driver Cooling**: Employs a 5010 5V blower to cool the Octopus Pro stepper drivers.
  - [@SimplifiedLife](https://www.printables.com/@SimplifiedLife)'s shroud https://www.printables.com/model/494141-ultra-cool-btt-octopus-stepper-driver-fan-duct
![image](https://github.com/0xdreadnaught/v24/assets/983663/855f7938-c898-4b6a-a798-d95683b44ec9)

- **Nevermore V6**: A carbon filter air purification system (installation pending).
  - [@nevermore3d](https://github.com/nevermore3d)'s infamous filter https://github.com/nevermore3d/Nevermore_Micro/tree/master/V6
![image](https://github.com/0xdreadnaught/v24/assets/983663/1faf9b0b-0e58-40ff-bdf5-45fdc543c81c)

- **Chamber Vortex**: An ongoing project to install dual 5010 5V blowers for thorough chamber circulation.
  - HEPA and additional charcoal filtration is planned for late.r Likely in a remote "pod".
  - My design, `stls/vortex_blowers_l_r.stl`, use supports.
![image](https://github.com/0xdreadnaught/v24/assets/983663/9c2ff0d9-7e10-4594-9d81-2052e0d671e6)
![image](https://github.com/0xdreadnaught/v24/assets/983663/f0102abf-6125-4458-b997-4bfdd384882c)

### Buckets
- **Poop Bucket**: Catches the purge blobs.
  - From [@Sarge013](https://www.printables.com/@Sarge013)'s imodel https://www.printables.com/model/380486-voron-prime-pellet-bucket
- **Dingleberry Bucket**: Catches leaking filament and wipes against a brush.
  - From [@FunFunBoy](https://www.printables.com/@FunFunBoy)'s imodel https://www.printables.com/model/201999-nozzle-scrubber-with-a-little-bucket-for-voron-24
  - Brush wipe not yet implemented in the config.

### Macros
- **Print Start**: Modified better print_start macro.
  - Gets bed/nozzle/chamber temps and max X,Y ranges.
  - Enbles BTT filament sensor's encoder (off on boot with delayed gcode).
  - Enables BTT filament sensor's switch (off on boot with delayed gcode).
  - Full XYZ home.
  - Chamber soak if needed.
  - Quad_Gantry_Level if needed.
  - Stable_Z_Home to ensure z-offset accuracy.
    - Checks z-offset until it stops deviating. This helps ensure the bed has fully expanded from the heat.
    - From [@matthewlloyd](https://github.com/matthewlloyd)'s project: https://github.com/matthewlloyd/Klipper-Stable-Z-Home
  - Adaptive bed mesh.
    - Margin 5 seems to work well. Slicer has range set to build dimensions.
  - Move to corner and heat up nozzle to target temp
  - PRIMING
  - CLEAN
- **PRIMING**: Purge poop.
  - CLEAN.
  - Create poop blob.
  - Wipe nozzle off to the right.
  - Kick poop off to the left into the bucket.
  - CLEAN.
- **CLEAN**: Poop wipe.
  - Wipe nozzle a little.
    
### Scripts
- **save_toolhead_pos.sh**: Save the current XYZ location for the PAUSE macro.
  - Ensure `/tmp/toolhead_position.txt` exists.
  - echo args $1-$3, X,Y,Z to `toolhead_position.txt`.
    - The need for this arose from Klipper not wanting to pass custom variables between macros and I wanted a safer RESUME path.
- **restore_toolhead_pos.sh**: Move the toolhead back to the original position.
  - Gets the X,Y,Z from `toolhead_position.txt`.
  - Sends `G90` to the printer's MCU socket file, `/tmp/printer/mcu_socket` for me, somtimes it's `/tmp/printer`.
  - Sends the X, then Y moves.
    - Handling Z this way caused random problems so I have that handled in the macro when it turns the nozzle back on.
- **wipe_toolhead_pos.sh**: Purge `toolhead_position.txt` contents.
  - Just minsor security considering shell command access is risky.

## Warning
Proceed with caution: Implementing configurations or scripts from this repository should be done at your own risk, with a fire extinguisher readily available.
