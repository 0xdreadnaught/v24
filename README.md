# Voron 2.6873 - Lilith

This repository contains configuration backups and custom scripts for my Voron 2.4, dubbed Lilith. 
Lilith, the evil daughter of Diablo, parallels 3D printing's dark allure—both look cool and may burn your house down in the middle of the night.

These scripts and configs are not intended for public replication but serve as a cautionary showcase of what not to do with your Voron 2.4.
The base printer is a Siboor v2.4r2 Aug(Dec refresh). The only thing remaining from Siboor is the OS on the BTT-pi.


### Fans
- **Stepper Driver Cooling**: Employs a 5010 5V blower to cool the Octopus Pro stepper drivers.
  - [@SimplifiedLife](https://www.printables.com/@SimplifiedLife)'s shroud https://www.printables.com/model/494141-ultra-cool-btt-octopus-stepper-driver-fan-duct
    - I did have to cut off the last driver segment because it was colliding with the fuse. It has no impact on performance.

    ![image](https://github.com/0xdreadnaught/v24/assets/983663/855f7938-c898-4b6a-a798-d95683b44ec9)
    ![image](https://github.com/0xdreadnaught/v24/assets/983663/bf8da60f-11c6-4741-9b34-3dc42d34a9fd)
    
  - Engaged drivers at 27.5C ambient, fully soaked:
  
    ![image](https://github.com/0xdreadnaught/v24/assets/983663/7f2bfe7b-e6e1-42de-a889-46b6e6264e7d)
    
  - Driver fan at 100%:
  
    ![image](https://github.com/0xdreadnaught/v24/assets/983663/3ea95ebd-f6c8-4324-a45e-54ac6e5dbe1b)
    
  - With skirt fans at 60% and driver fan at 100%:
  
    ![image](https://github.com/0xdreadnaught/v24/assets/983663/31aba975-3d73-4e7c-9d0e-4eccf26b360e)


- **Nevermore V6**: Activated charcoal air purification system (wiring incomplete).
  - [@nevermore3d](https://github.com/nevermore3d)'s infamous filter https://github.com/nevermore3d/Nevermore_Micro/tree/master/V6

    ![image](https://github.com/0xdreadnaught/v24/assets/983663/edb0063b-23db-4f00-8894-26dd83046037)

- **Chamber Vortex**: An ongoing project to install custom activated charcoal/HEPA filtration.
  - My "design", `stls/vortex_blowers_l_r.stl`, use supports.
    - The mount is a remix of [@Sarge013](https://www.printables.com/@Sarge013)'s poop bucket mount.
    - May need to move it a tad further away, 2mil plate clearance currently. We'll see if it melts during ABS/ASA prints.

    ![image](https://github.com/0xdreadnaught/v24/assets/983663/9c2ff0d9-7e10-4594-9d81-2052e0d671e6)
    ![image](https://github.com/0xdreadnaught/v24/assets/983663/f0102abf-6125-4458-b997-4bfdd384882c)

### Buckets
- **Poop Bucket**: Catches the purge blobs.
  - From [@Sarge013](https://www.printables.com/@Sarge013)'s imodel https://www.printables.com/model/380486-voron-prime-pellet-bucket
  - Modified with a cable channel and SBC cutout to allow the UFP sensor to run under it. It was that or builr a cable for it.
    - STL not yet added to `stls/`.

      ![image](https://github.com/0xdreadnaught/v24/assets/983663/386c0f0d-882d-420e-afe4-1ec4d18009be)
      ![image](https://github.com/0xdreadnaught/v24/assets/983663/1681bb32-2ae9-43b6-b158-0f37bb4d921e)

- **Dingleberry Bucket**: Catches leaking filament and wipes against a brush.
  - From [@FunFunBoy](https://www.printables.com/@FunFunBoy)'s model https://www.printables.com/model/201999-nozzle-scrubber-with-a-little-bucket-for-voron-24

    ![image](https://github.com/0xdreadnaught/v24/assets/983663/73664480-ffb9-4918-9376-24f3002caa03)


### Sensors
- **Ultra Fine Partical(UFP) Sensor**: Detect dust and other fine particals in the chamber.
  - AITRIP SDS011.
  - Detection ranges: 0.3-2.5 microns & 2.5-10.0 microns.
  - Polled with `python3 ufp_check.py` for now.

    ![image](https://github.com/0xdreadnaught/v24/assets/983663/2cec0a13-1a85-48d9-aeb3-0982386c0a87)

- **Volatile Organic Compound(VOC) Sensor**: Detect VOCs in the chamber.
  - SGP40. Not yet wired up.
 
- **X/Y Endstops**: Sensorless homing just seems silly to me when microswitches are accurate, cheap, small, and easy to setup.
  - The Chaotic Lab CNC kit would crash into itself during homing, mainly the Y axis. To remediate this I just stuck some tabs from a cut up CompTIA Pentest+ card. The red matches well.
    - This also stopped the toolhead from catching on the cable chain, which happened every once in a while.

      ![image](https://github.com/0xdreadnaught/v24/assets/983663/06f64b24-84e3-4e2f-85fa-b06db0962d8e)
      ![image](https://github.com/0xdreadnaught/v24/assets/983663/ea547306-eba6-437c-aaba-e562e70e2e6c)


### Misc Mods
- **Sturdy Handles**: Gotta move the thing sometimes.
  - [@Jeoje](https://github.com/jeoje)'s handles from https://github.com/VoronDesign/VoronUsers/tree/main/printer_mods/jeoje/Sturdy_Handles

    ![image](https://github.com/0xdreadnaught/v24/assets/983663/93200d64-7cbb-4c63-8d0d-63b60f6b1bdf)

- **Rock and Roll**: Easier electronics access.
  - [@RockNLol](https://github.com/RockNLol)'s project https://github.com/VoronDesign/VoronUsers/tree/main/printer_mods/RockNLol/RockNRoll

    ![image](https://github.com/0xdreadnaught/v24/assets/983663/b3e9a281-0d24-4d2b-b3e8-aabfbb21b3e1)

- **Lilith Handles**: Just the normal Voron PC tabs with Lilith glued on. Loctite 480 works fantastic for filament to metal/glass/filaments.

  ![image](https://github.com/0xdreadnaught/v24/assets/983663/414df465-0397-4d25-ad32-556a499492f3)
  ![image](https://github.com/0xdreadnaught/v24/assets/983663/2d18f4ba-9826-4b9c-b18d-13a54791771d)

- **SB LEDs**: StealthBurner LED NeoPixel support.
  - [@nemgrea](https://github.com/nemgrea)'s https://github.com/VoronDesign/Voron-Stealthburner/blob/main/Firmware/stealthburner_leds.cfg

    ![image](https://github.com/0xdreadnaught/v24/assets/983663/b8232f8d-44af-474c-98c4-1df60c041135)


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
- **PRINT_END**: Standard end macro.
  - Clear the bed mesh just to be sure it can't be loaded by accident on the next print.
  - Disable Filament encoder and switch sensors.
- **PRIMING**: Purge poop.
  - CLEAN.
  - Create poop blob.
  - Wipe nozzle off to the right.
  - Kick poop off to the left into the bucket.
  - CLEAN.

https://github.com/0xdreadnaught/v24/assets/983663/5e7ff68e-c6dc-4241-8806-f2f68643afed

    
- **CLEAN**: Poop wipe.
  - Wipe nozzle a little.
- **PAUSE**: Modified Ellis' PAUSE macro.
  - Save off X,Y,Z to file to bypass lack of custom variable support.
- **RESUME**: Modified Ellis' RESUME macro.
  - Load X,Y,Z from file and move Z last to mitigate nozzle collisions as much as possible.
- **M486**: Cancel Object command for Exclude Object support.
- **Calibrate_Estep**: Aid for calibration e-step/rotation_distance.
  - Home Z.
  - Move to 50mm off build plate.
  - Move to front center.
  - Set nozzle to specified temp, 150 if not specified.
    
### Scripts
- **save_toolhead_pos.sh**(Deprecated): Save the current XYZ location for the PAUSE macro.
  - Ensure `/tmp/toolhead_position.txt` exists.
  - echo args $1-$3, X,Y,Z to `toolhead_position.txt`.
    - The need for this arose from Klipper not wanting to pass custom variables between macros and I wanted a safer RESUME path.
- **restore_toolhead_pos.sh**(Deprecated): Move the toolhead back to the original position.
  - Gets the X,Y,Z from `toolhead_position.txt`.
  - Sends `G90` to the printer's MCU socket file, `/tmp/printer/mcu_socket` for me, somtimes it's `/tmp/printer`.
  - Sends the X, then Y moves.
    - Handling Z this way caused random problems so I have that handled in the macro when it turns the nozzle back on.
- **wipe_toolhead_pos.sh**(Deprecated): Purge `toolhead_position.txt` contents.
  - Just minor security considering shell command access is risky.
- **ufp_check.py**: Get the UFP sensor data.
  - Still WIP since there's no native way to add this data into mainsail. Will likely build a Klipper-Screen replacement.

    ![image](https://github.com/0xdreadnaught/v24/assets/983663/598c0297-4c00-45eb-9efd-e8cbdd2782bd)

### Quirks
- **No Back Panel**: The back panel is currently removed to facilitate PLA printing. Other panels let in too much dog hair(yay husky and 2x labs lol).
  - Using a custom mount for the filament couplers for now.

    ![image](https://github.com/0xdreadnaught/v24/assets/983663/7ca6156c-b52f-4b3b-8c0e-9029681c6ade)

## Warning
Proceed with caution: Implementing configurations or scripts from this repository should be done at your own risk, with a fire extinguisher readily available.


# To-Do

## Firmware and Software Enhancements
- [x] Refactor pause/resume macros to use Klipper's internal variable system instead of shell commands.

## Sensor Integration and Data Aggregation
- [ ] Wire up the VOC sensor to the printer.
- [ ] Develop a script for aggregating VOC sensor data, drawing inspiration from `ufp_check.py`.

## Interface Development
- [ ] Design and implement a new LCD interface to display UFP/VOC sensor data and provide quick-access printer commands (pause/resume/cancel).
- [ ] Incorporate a physical switch to toggle between klipper-screen and the new interface.

## Hardware Installation
- [ ] Pin and connect the Nevermore V6 carbon filter.
- [ ] Install and wire the vortex blowers, using wago clips to connect to the Octopus board.

## Structural Build-out
- [ ] Construct and mount the back panel and exhaust system, including the filter pod (can be initially empty).
- [ ] Design and fabricate an external air filtration pod using 20x20 aluminum extrusions and PC paneling to match the main chassis.
  - [ ] Ensure the pod includes activated charcoal and HEPA filters, alongside fans for proper airflow.
