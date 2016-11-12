## Introduction
This project uses a Freedom K64 Development board. It specifically writes data from the 6-axis combo Sensor, Accelerometer and Magnetometer, every **100th** of a second to the microSD card. 
### `sd_card.c`
file is complied on mbed and the .bin file is sent to the [Freedom K64 board](https://developer.mbed.org/platforms/FRDM-K64F/). 
###Parser Folder
Contains Python Parser, file to be parsed, and parsed files. This will be used to take data from the text file and sent to csv for easier use of data for visualizations. **Only needed for 1st Edition** (Now writes directly to csv file)

### mbed Link
[Mbed Repository](https://developer.mbed.org/users/rahutchinson/code/FRDRMK64_AccelDATA2SD/)
