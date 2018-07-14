#!/usr/bin/env python

from dynamixel_sdk import *                    # Uses Dynamixel SDK library

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

PROTOCOL_VERSION            = 1.0               # See which protocol version is used in the Dynamixel
TORQUE_ENABLE               = 1                 # Value for enabling the torque
TORQUE_DISABLE              = 0                 # Value for disabling the torque

class dynamixel_mx28:

    def __init__(self, dxl_id=3, baud=1000000, device='/dev/dynamixel'):
        self.dxl_id = dxl_id
        self.baud = baud
        self.device = device
        
        
        
        
