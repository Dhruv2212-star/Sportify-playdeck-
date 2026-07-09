
# The first step is making the schematic

## The main components required for this build are 
1. mechenical keyboard switches X4 (sw_push for schematic)x4
2. seeed studio XIAO RP2040 (MODULE-SEEDUINO-XIAO)x1
3. 0.91 Inch OLED Display ( we use a Pin Header for this- PinHeader_1x04_P2.54mm_Vertical)x1

## Final schematic should be as following- 
<img width="818" height="540" alt="Screenshot (233)" src="https://github.com/user-attachments/assets/8edd5c41-b754-498d-afb0-09756700aaf0" />


# Update the schematic to PCB and Route the traces 
<img width="1367" height="730" alt="Screenshot (228)" src="https://github.com/user-attachments/assets/64bf76d9-a3c6-40be-80b3-b9685db986f4" />
And once the traces and connections are made, create a rectangle and make sure all the components fit insite it.
IMPORTANT- the rectangle property should be set to "edge.cuts".

# Create the case 

## Bottom case 
<img width="1366" height="721" alt="Screenshot (229)" src="https://github.com/user-attachments/assets/f0c66cac-f81e-4409-ae28-defb631734a3" />
## top case  
<img width="1366" height="725" alt="Screenshot (239)" src="https://github.com/user-attachments/assets/f6863aa3-59bc-4278-bde5-783a664f1fcb" />


# ASSEMBELED FILE
this is an model of what your project will look life later 
<img width="1366" height="713" alt="Screenshot (234)" src="https://github.com/user-attachments/assets/1f5ccfd7-cdb1-468d-a018-39b5d2275be3" />


# you can download all the file from the 'productions' folder 
this way you would escape the trouble of recreating the PCB the case for it and you can build it yourself!!  
Now once you have the files ready, Order the PCB and 3D print the case files  
solder all the components in their places   
hot glue the pcb in the case for extra strength 

# Firmware flashing 

## instal circuitpython   
1. connect your microcontroler to your PC   
2. new drive called RPI-RP2 will appear    
3. paste "adafruit-circuitpython-seeeduino_xiao_rp2040-en_US-10.2.1" file from the 'Firmware' folder given    
4. The board automatically restarts  
5. the drive is now named 'CIRCUITPY'  
6. delete any file named 'code.py' in the CIRCUITPY drive if any  
7. now copy and past these files from the firmware folder  
8. "boot.py", "code.py", entire "lib" folder  
9. yout board should look like this  
CIRCUITPY/  

boot.py  

code.py  

lib/  
10. save and close the window and boot it  
# That's it! 
## open spotify and now you can control the pause, play, next, previous funtions without opening your spotify desktop application 
