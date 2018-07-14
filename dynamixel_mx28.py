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
                
        # Initialize PortHandler instance
        # Get methods and members of PortHandlerLinux
        self.portHandler = PortHandler(self.device)

        # Initialize PacketHandler instance
        # Get methods and members of Protocol1PacketHandler
        self.packetHandler = PacketHandler(PROTOCOL_VERSION)  
        
        # Open port
        if self.portHandler.openPort():
            print("Succeeded to open the port")
        else:
            print("Failed to open the port")
            quit()

        # Set port baudrate
        if self.portHandler.setBaudRate(self.baud):
            print("Succeeded to change the baudrate")
        else:
            print("Failed to change the baudrate")
            quit()   
            
    def __del__(self):
        self.portHandler.closePort()    
            
    def set_cw_limit(self,limit=0):
        dxl_comm_result, dxl_error = self.packetHandler.write2ByteTxRx(self.portHandler, self.dxl_id, ADDR_CW_ANGLE_LIMIT, limit)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % self.packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % self.packetHandler.getRxPacketError(dxl_error))
        else:
            print("Dynamixel CW limit set to %d" % limit)
            
    def set_ccw_limit(self,limit=0):
        dxl_comm_result, dxl_error = self.packetHandler.write2ByteTxRx(self.portHandler, self.dxl_id, ADDR_CCW_ANGLE_LIMIT, limit)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % self.packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % self.packetHandler.getRxPacketError(dxl_error))
        else:
            print("Dynamixel CCW limit set to %d" % limit)

    def set_wheel_mode(self):
        self.set_cw_limit(0)
        self.set_ccw_limit(0)
        
    def get_present_position(self):
        dxl_position = 99999 # error code
        dxl_position, dxl_comm_result, dxl_error = self.packetHandler.read2ByteTxRx(self.portHandler, self.dxl_id, ADDR_MX_PRESENT_POSITION)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % self.packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % self.packetHandler.getRxPacketError(dxl_error))  
        return dxl_position # returns 99999 if not successful else returns valid position
        
    def set_moving_speed(self,set_speed):
        dxl_comm_result, dxl_error = self.packetHandler.write2ByteTxRx(self.portHandler, self.dxl_id, ADDR_MX_MOVING_SPEED, set_speed)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % self.packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % self.packetHandler.getRxPacketError(dxl_error))                                
        
if __name__ == "__main__":
    dyna1 = dynamixel_mx28(dxl_id=3)
    dyna2 = dynamixel_mx28(dxl_id=4)   
    dyna1.set_wheel_mode()
    dyna2.set_wheel_mode()
    print("Pos1: %d, Pose2: %d" % (dyna1.get_present_position(), dyna2.get_present_position()))   

