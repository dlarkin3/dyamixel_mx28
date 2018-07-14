#!/usr/bin/env python

import os
from dynamixel_sdk import *                    # Uses Dynamixel SDK library
import cv2
import numpy as np

# Control table address
ADDR_CW_ANGLE_LIMIT         = 6
ADDR_CCW_ANGLE_LIMIT        = 8
ADDR_MX_TORQUE_ENABLE       = 24               # Control table address is different in Dynamixel model
ADDR_MX_LED_ONOFF           = 25               # http://emanual.robotis.com/docs/en/dxl/mx/mx-28/#control-table-of-ram-area
ADDR_MX_D_GAIN              = 26
ADDR_MX_I_GAIN              = 27
ADDR_MX_P_GAIN              = 28
ADDR_MX_GOAL_POSITION       = 30
ADDR_MX_MOVING_SPEED        = 32
ADDR_MX_TORQUE_LIMIT        = 34
ADDR_MX_PRESENT_POSITION    = 36
ADDR_MX_PRESENT_SPEED       = 38
ADDR_MX_PRESENT_LOAD        = 40
ADDR_MX_PRESENT_VOLTAGE     = 42
ADDR_MX_PRESENT_TEMPERATURE = 43
ADDR_MX_REGISTERED          = 44
ADDR_MX_MOVING              = 46
ADDR_MX_LOCK                = 47
ADDR_MX_PUNCH               = 48
ADDR_MX_REALTIME_TICK       = 50
ADDR_MX_GOAL_ACCELERATION   = 73

# Protocol version
PROTOCOL_VERSION            = 1.0               # See which protocol version is used in the Dynamixel

# Default setting
DXL_ID                      = 3                 # Dynamixel ID : 1
BAUDRATE                    = 1000000             # Dynamixel default baudrate : 57600
DEVICENAME                  = '/dev/dynamixel'    # Check which port is being used on your controller
TORQUE_ENABLE               = 1                 # Value for enabling the torque
TORQUE_DISABLE              = 0                 # Value for disabling the torque



# Initialize PortHandler instance
# Set the port path
# Get methods and members of PortHandlerLinux or PortHandlerWindows
portHandler = PortHandler(DEVICENAME)

# Initialize PacketHandler instance
# Set the protocol version
# Get methods and members of Protocol1PacketHandler or Protocol2PacketHandler
packetHandler = PacketHandler(PROTOCOL_VERSION)

# Open port
if portHandler.openPort():
    print("Succeeded to open the port")
else:
    print("Failed to open the port")
    print("Press any key to terminate...")
    getch()
    quit()

# Set port baudrate
if portHandler.setBaudRate(BAUDRATE):
    print("Succeeded to change the baudrate")
else:
    print("Failed to change the baudrate")
    print("Press any key to terminate...")
    getch()
    quit()

# Enable Dynamixel Torque
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL_ID, ADDR_MX_TORQUE_ENABLE, TORQUE_ENABLE)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))
else:
    print("Dynamixel has been successfully connected")
    
# Set CW Limit
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID, ADDR_CW_ANGLE_LIMIT, 0)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))
else:
    print("Dynamixel has been successfully connected")
    
# Set CW Limit
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID, ADDR_CCW_ANGLE_LIMIT, 0)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))
else:
    print("Dynamixel has been successfully connected")
    
def nothing(x):
    pass    
    
cv2.namedWindow('image')
cv2.createTrackbar('Speed','image',1024,2047,nothing)
cv2.createTrackbar('Direction','image',0,1,nothing)
img = np.full((300,512,3), 55)

while 1:
    cv2.imshow('image',img)

    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break
    
    set_speed = cv2.getTrackbarPos('Speed','image')# - 255

    # Get present position
    dxl_position, dxl_comm_result, dxl_error = packetHandler.read2ByteTxRx(portHandler, DXL_ID, ADDR_MX_PRESENT_POSITION)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))
        
    if (dxl_position < 1500 and set_speed >  1024):
        set_speed = 1024
    if (dxl_position > 3600 and set_speed <  1023):
        set_speed = 0
        
    print("Speed, Position:%d, %d" % (set_speed,dxl_position) )
    
    # Write goal velocity
    dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID, ADDR_MX_MOVING_SPEED, set_speed)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))

    
cv2.destroyAllWindows()
# Close port
portHandler.closePort()    

