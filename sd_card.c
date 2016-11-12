#include "mbed.h"
#include "SDFileSystem.h"
#include "FXOS8700Q.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//Port Assignments________________________________________________________________________________________________
FXOS8700Q_acc acc( PTE25, PTE24, FXOS8700CQ_SLAVE_ADDR1); // Proper Ports and I2C Address for K64F Freedom board
FXOS8700Q_mag mag( PTE25, PTE24, FXOS8700CQ_SLAVE_ADDR1); // Proper Ports and I2C Address for K64F Freedom board


Serial pc(USBTX, USBRX);
//MotionSensor Data given in terms of gravity
MotionSensorDataUnits mag_data;
MotionSensorDataUnits acc_data;
//MotionSensor Data Raw - Meaning that it gives in non 'Gs'
MotionSensorDataCounts mag_raw;
MotionSensorDataCounts acc_raw;
//SD card initialization  "sd" is what the directory is called. to access it is "/sd"
SDFileSystem sd(PTE3, PTE1, PTE2, PTE4, "sd"); // MOSI, MISO, SCK, CS
//File initialization
FILE *fp_raw;
FILE *fp_

int main()
{
    //for in terms of gravity ratings
    float faX, faY, faZ;
    float fmX, fmY, fmZ;
    //for raw data
    int16_t raX, raY, raZ;
    int16_t rmX, rmY, rmZ;
    
    
    acc.enable(); //Enable Motion Sensor
    
    //pc.printf("Initializing \n");
    mkdir("/sd/test", 0777);
    fp_log = fopen("/sd/log.txt")
    fp_= fopen("/sd/test/testing.csv", "a+");
    fp_raw = fopen("/sd/test/testing_raw.csv", "a+");
    if (fp == NULL || fp_raw == NULL) {
        fprintf(fp_log,"Unable to write the file \n");
    } else {
        fprintf(fp,"Begin Here _______________________________________________");
        fprintf(fp_raw, "Begin Here _____________________________________________");
        fclose(fp);
        fclose(fp_raw);
        int count = 0;
        while(true){
            count =0;
            fp = fopen("/sd/test/testing.csv", "a+");
            fp_raw = fopen("/sd/test/testing_raw.csv","a+");
            while (count <100) {
                acc.getAxis(acc_data);
                mag.getAxis(mag_data);
                fprintf(fp,"%1.5f,%1.5f,%1.5f, ", acc_data.x, acc_data.y, acc_data.z);
                fprintf(fp,"%4.3f, %4.3f, %4.3f\r\n", mag_data.x, mag_data.y, mag_data.z);
                acc.getAxis(acc_raw);
                mag.getAxis(mag_raw);
                fprintf(fp_raw,"%d,%d,%d,", acc_raw.x, acc_raw.y, acc_raw.z);
                fprintf(fp_raw,"%d, %d,%d\r\n", mag_raw.x, mag_raw.y, mag_raw.z);
                wait(.001);
                count = count +1;
            }
            fclose(fp);
        }
        
    }
    

}
