# This file will parse the accelerometer data from the Freedom K64 board to a csv file
#  for use in generating visualizations
fp_g_accel = open('Test_parse.csv', 'w')  # G values for accel
fp_g_mag = open('Test_parse_mag.csv' , 'w')
fp_accel = open('Test_parse_accel.csv' , 'w')
fp_mag = open('Test_mag.csv' , 'w')

with open('first_drive_videoed.txt') as fp:
    for line in fp:
        if line.find("FXOS8700Q ACC:__ X=") != -1:
            index_x = line.find("FXOS8700Q ACC:__ X=") + len("FXOS8700Q ACC:__ X=")
            index_nxt = line.find("MAG: X=")
            index_y = line.find(" Y=")
            index_z = line.find(" Z=")
            fp_g_accel.write(str(line[index_x:index_y]) + ",")  # X value ,
            fp_g_accel.write(str(line[index_y + 3:index_z - 1]) + ",")  # Y value,
            fp_g_accel.write(str(line[index_z + 3:index_nxt - 1]) + "\n")  # Z value.
        if line.find("FXOS8700Q ACC:__ X=") != -1:
            index_x = line.find("MAG: X=") + len("MAG: X=")
            index_y = line.find("Y=", index_x)
            index_z = line.find("Z=", index_y)
            fp_g_mag.write(str(line[index_x:index_y-1]) + ",")
            fp_g_mag.write(str(line[index_y + 3:index_z-1]) + ",")
            fp_g_mag.write(str(line[index_z + 3:len(line)-1]) + "\n")
        if line.find("FXOS8700Q ACC: X=") != -1:
            index_x = line.find("FXOS8700Q ACC: X=") + len("FXOS8700Q ACC: X=")
            index_nxt = line.find("MAG: X=")
            index_y = line.find(" Y=")
            index_z = line.find(" Z=")
            fp_accel.write(str(line[index_x:index_y]) + ",")  # X value ,
            fp_accel.write(str(line[index_y + 3:index_z - 1]) + ",")  # Y value,
            fp_accel.write(str(line[index_z + 3:index_nxt - 1]) + "\n")  # Z value.
        if line.find("FXOS8700Q ACC: X=") != -1:
            index_x = line.find("MAG: X=") + len("MAG: X=")
            index_y = line.find(" Y=", index_x)
            index_z = line.find(" Z=", index_y)
            fp_mag.write(str(line[index_x:index_y]) + ",")  # X value ,
            fp_mag.write(str(line[index_y + 3:index_z - 1]) + ",")  # Y value,
            fp_mag.write(str(line[index_z + 3:len(line) - 1]) + "\n")  # Z value.

