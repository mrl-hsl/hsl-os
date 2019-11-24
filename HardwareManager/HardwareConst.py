"""
Hardwares IDs
"""
CM_ID = 200
HEAD_BUCK_ID = 100
RIGHT_HAND_BUCK_ID = 101
LEFT_HAND_BUCK_ID = 102
RIGHT_HIP_BUCK_ID = 103
RIGHT_KNEE_BUCK_ID = 105
LEFT_HIP_BUCK_ID = 104
LEFT_KNEE_BUCK_ID = 106
"""
CM Constants
"""
GYRO_X = 0
BUTTON1_STATE = 18
INPUT_VOLTAGE = 11
"""
Dynamixel protocol 2.0 Constants
"""
# Control Table of EEPROM Area
DXL_MODEL_NUMBER = 0          # size = 2
DXL_MODEL_INFORMATION = 2     # size = 4
DXL_FIRMWARE_VERSION = 6      # size = 1
DXL_ID = 7                    # size = 1
DXL_BAUD_RATE = 8             # size = 1
DXL_RETURN_DELAY_TIME = 9     # size = 1
DXL_DRIVE_MODE = 10           # size = 1
DXL_OPERATING_MODE = 11       # size = 1
DXL_SECONDARY_ID = 12         # size = 1
DXL_PROTOCOL_TYPE = 13        # size = 1
DXL_HOMING_OFFSET = 20        # size = 4
DXL_MOVING_THRESHOLD = 24     # size = 4
DXL_TEMPRATURE_LIMIT = 31     # size = 1
DXL_MAX_VOLTAGE_LIMIT = 32    # size = 2
DXL_MIN_VOLTAGE_LIMIT = 34    # size = 2
DXL_PWM_LIMIT = 36            # size = 2
DXL_ACCELERATION_LIMIT = 40   # size = 4
DXL_VELOCITY_LIMIT = 44       # size = 4
DXL_MAX_POSITION_LIMIT = 48   # size = 4
DXL_MIN_POSITION_LIMIT = 52   # size = 4
DXL_SHUTDOWN = 63             # size = 1
# Control Table of RAM Area
DXL_TORQUE_ENABLE = 64          # size = 1
DXL_LED = 65                    # size = 1
DXL_STATUS_RETURN_LEVEL = 68    # size = 1
DXL_REGISTRED_INSTRUCTION = 69  # size = 1
DXL_HARDWARE_ERROR_STATUS = 70  # size = 1
DXL_VELOCITY_I_GAIN = 76        # size = 2
DXL_VELOCITY_P_GAIN = 78        # size = 2
DXL_POSITION_D_GAIN = 80        # size = 2
DXL_POSITION_I_GAIN = 82        # size = 2
DXL_POSITION_P_GAIN = 84        # size = 2
DXL_FEEDFORWARD_2ND_GAIN = 88   # size = 2
DXL_FEEDFORWARD_1ST_GAIN = 90   # size = 2
DXL_BUS_WATCHDOG = 98           # size = 1
DXL_GOAL_PWM = 100              # size = 2
DXL_GOAL_VELOCITY = 104         # size = 4
DXL_PROFILE_ACCELERATION = 108  # size = 4
DXL_PROFILE_VELOCITY = 112      # size = 4
DXL_GOAL_POSITION = 116         # size = 4
DXL_REALTIME_TICK = 120         # size = 2
DXL_MOVING = 122                # size = 1
DXL_MOVING_STATUS = 123         # size = 1
DXL_PRESENT_PWM = 124           # size = 2            
DXL_PRESENT_LOAD = 126          # size = 2
DXL_PRESENT_VELOCITY = 128      # size = 4
DXL_PRESENT_POSITION = 132      # size = 4
DXL_VELOCITY_TRAJECTORY = 136   # size = 4
DXL_POSITION_TRAJECTORY = 140   # size = 4
DXL_PRESENT_INPUT_VOLTAGE = 144 # size = 2
DXL_PRESENT_TERMPRATURE = 146   # size = 1

# Status Return Levels
DXL_RETURN_NONE = 0
DXL_RETURN_READ = 1
DXL_RETURN_ALL = 2

# Instruction Set
DXL_PING = 1
DXL_READ_DATA = 2
DXL_WRITE_DATA = 3
DXL_REG_WRITE = 4
DXL_ACTION = 5
DXL_RESET = 6
DXL_SYNC_READ = 130
DXL_SYNC_WRITE = 131

# Broadcast Constant
DXL_BROADCAST_ID = 254

# Error Codes
DXL_INSTRUCTION_ERROR = 64
DXL_OVERLOAD_ERROR = 32
DXL_CHECKSUM_ERROR = 16
DXL_RANGE_ERROR = 8
DXL_OVERHEATING_ERROR = 4
DXL_ANGLE_LIMIT_ERROR = 2
DXL_INPUT_VOLTAGE_ERROR = 1
DXL_NO_ERROR = 0

# Static parameters
DXL_MIN_COMPLIANCE_MARGIN = 0
DXL_MAX_COMPLIANCE_MARGIN = 255

DXL_MIN_COMPLIANCE_SLOPE = 1
DXL_MAX_COMPLIANCE_SLOPE = 254

# These are guesses as Dynamixel documentation doesn't have any info about it
DXL_MIN_PUNCH = 0
DXL_MAX_PUNCH = 255

DXL_MAX_SPEED_TICK = 1023                   # maximum speed in encoder units
DXL_MAX_TORQUE_TICK = 1023                  # maximum torque in encoder units

KGCM_TO_NM = 0.0980665                      # 1 kg-cm is that many N-m
RPM_TO_RADSEC = 0.104719755                 # 1 RPM is that many rad/sec

# maximum holding torque is in N-m per volt
# maximum velocity is in rad/sec per volt
# DXL_MODEL_TO_PARAMS = \
# {
#     113: { 'name':               'DX-113',
#            'encoder_resolution': 1024,
#            'range_degrees':      300.0,
#            'torque_per_volt':    1.0 / 12.0,                       #  1.0 NM @ 12V
#            'velocity_per_volt':  (54 * RPM_TO_RADSEC) / 12.0,      #  54 RPM @ 12V
#            'rpm_per_tick':       0.111,
#            'features':           []
#          },
#     116: { 'name':               'DX-116',
#            'encoder_resolution': 1024,
#            'range_degrees':      300.0,
#            'torque_per_volt':    2.1 / 12.0,                       #  2.1 NM @ 12V
#            'velocity_per_volt':  (78 * RPM_TO_RADSEC) / 12.0,      #  78 RPM @ 12V
#            'rpm_per_tick':       0.111,
#            'features':           []
#          },
#     117: { 'name':               'DX-117',
#            'encoder_resolution': 1024,
#            'range_degrees':      300.0,
#            'torque_per_volt':    3.7 / 18.5,                       #  3.7 NM @ 18.5V
#            'velocity_per_volt':  (85 * RPM_TO_RADSEC) / 18.5,      #  85 RPM @ 18.5V
#            'rpm_per_tick':       0.111,
#            'features':           []
#          },
#      12: { 'name':               'AX-12',
#            'encoder_resolution': 1024,
#            'range_degrees':      300.0,
#            'torque_per_volt':    1.5 / 12.0,                       #  1.5 NM @ 12V
#            'velocity_per_volt':  (59 * RPM_TO_RADSEC) / 12.0,      #  59 RPM @ 12V
#            'rpm_per_tick':       0.111,
#            'features':           []
#          },
#     300: { 'name':               'AX-12W',
#            'encoder_resolution': 1024,
#            'range_degrees':      300.0,
#            'torque_per_volt':    0.2 / 12.0,                       # 0.2 NM @ 12V
#            'velocity_per_volt':  (470 * RPM_TO_RADSEC) / 12.0,     # 470 RPM @ 12V
#            'rpm_per_tick':       0.111,
#            'features':           []
#          },
#      18: { 'name':               'AX-18',
#            'encoder_resolution': 1024,
#            'range_degrees':      300.0,
#            'torque_per_volt':    1.8 / 12.0,                       #  1.8 NM @ 12V
#            'velocity_per_volt':  (97 * RPM_TO_RADSEC) / 12.0,      #  97 RPM @ 12V
#            'rpm_per_tick':       0.111,
#            'features':           []
#          },
#      10: { 'name':               'RX-10',
#            'encoder_resolution': 1024,
#            'range_degrees':      300.0,
#            'torque_per_volt':    1.3 / 12.0,                       #  1.3 NM @ 12V
#            'velocity_per_volt':  (54 * RPM_TO_RADSEC) / 12.0,      #  54 RPM @ 12V
#            'rpm_per_tick':       0.111,
#            'features':           []
#          },
#      24: { 'name':               'RX-24',
#            'encoder_resolution': 1024,
#            'range_degrees':      300.0,
#            'torque_per_volt':    2.6 / 12.0,                       #  2.6 NM @ 12V
#            'velocity_per_volt':  (126 * RPM_TO_RADSEC) / 12.0,     # 126 RPM @ 12V
#            'rpm_per_tick':       0.111,
#            'features':           []
#          },
#      28: { 'name':               'RX-28',
#            'encoder_resolution': 1024,
#            'range_degrees':      300.0,
#            'torque_per_volt':    3.7 / 18.5,                       #  3.7 NM @ 18.5V
#            'velocity_per_volt':  (85 * RPM_TO_RADSEC) / 18.5,      #  85 RPM @ 18.5V
#            'rpm_per_tick':       0.111,
#            'features':           []
#          },
#      64: { 'name':               'RX-64',
#            'encoder_resolution': 1024,
#            'range_degrees':      300.0,
#            'torque_per_volt':    5.3 / 18.5,                       #  5.3 NM @ 18.5V
#            'velocity_per_volt':  (64 * RPM_TO_RADSEC) / 18.5,      #  64 RPM @ 18.5V
#            'rpm_per_tick':       0.111,
#            'features':           []
#          },
#     106: { 'name':               'EX-106',
#            'encoder_resolution': 4096,
#            'range_degrees':      250.92,
#            'torque_per_volt':    10.9 / 18.5,                      # 10.9 NM @ 18.5V
#            'velocity_per_volt':  (91 * RPM_TO_RADSEC) / 18.5,      #  91 RPM @ 18.5V
#            'rpm_per_tick':       0.111,
#            'features':           [DXL_SENSED_CURRENT_L]
#          },     
#     107: { 'name':               'EX-106+',
#            'encoder_resolution': 4096,
#            'range_degrees':      250.92,
#            'torque_per_volt':    10.9 / 18.5,                      # 10.9 NM @ 18.5V
#            'velocity_per_volt':  (91 * RPM_TO_RADSEC) / 18.5,      #  91 RPM @ 18.5V
#            'rpm_per_tick':       0.111,
#            'features':           [DXL_SENSED_CURRENT_L]
#          },
#     360: { 'name':               'MX-12W',
#            'encoder_resolution': 4096,
#            'range_degrees':      360.0,
#            'torque_per_volt':    0.2 / 12.0,                        #  torque not specified!
#            'velocity_per_volt':  (470 * RPM_TO_RADSEC) / 12.0,      #  470 RPM @ 12.0V
#            'rpm_per_tick':       0.114,
#            'features':           [DXL_GOAL_ACCELERATION]
#          },
#      29: { 'name':               'MX-28',
#            'encoder_resolution': 4096,
#            'range_degrees':      360.0,
#            'torque_per_volt':    2.5 / 12.0,                       #  2.5 NM @ 12V
#            'velocity_per_volt':  (55 * RPM_TO_RADSEC) / 12.0,      #  54 RPM @ 12.0V
#            'rpm_per_tick':       0.114,
#            'features':           [DXL_GOAL_ACCELERATION]
#          },
#     310: { 'name':               'MX-64',
#            'encoder_resolution': 4096,
#            'range_degrees':      360.0,
#            'torque_per_volt':    6.0 / 12.0,                       #  6 NM @ 12V
#            'velocity_per_volt':  (63 * RPM_TO_RADSEC) / 12.0,      #  63 RPM @ 12.0V
#            'rpm_per_tick':       0.114,
#            'features':           [DXL_CURRENT_L, DXL_TORQUE_CONTROL_MODE, DXL_GOAL_ACCELERATION]
#          },
#     320: { 'name':               'MX-106',
#            'encoder_resolution': 4096,
#            'range_degrees':      360.0,
#            'torque_per_volt':    8.4 / 12.0,                       #  8.4 NM @ 12V
#            'velocity_per_volt':  (45 * RPM_TO_RADSEC) / 12.0,      #  45 RPM @ 12.0V
#            'rpm_per_tick':       0.114,
#            'features':           [DXL_CURRENT_L, DXL_TORQUE_CONTROL_MODE, DXL_GOAL_ACCELERATION]
#          },
# }

"""
CRC16 table
"""
crc_table = [
        0x0000, 0x8005, 0x800F, 0x000A, 0x801B, 0x001E, 0x0014, 0x8011,
        0x8033, 0x0036, 0x003C, 0x8039, 0x0028, 0x802D, 0x8027, 0x0022,
        0x8063, 0x0066, 0x006C, 0x8069, 0x0078, 0x807D, 0x8077, 0x0072,
        0x0050, 0x8055, 0x805F, 0x005A, 0x804B, 0x004E, 0x0044, 0x8041,
        0x80C3, 0x00C6, 0x00CC, 0x80C9, 0x00D8, 0x80DD, 0x80D7, 0x00D2,
        0x00F0, 0x80F5, 0x80FF, 0x00FA, 0x80EB, 0x00EE, 0x00E4, 0x80E1,
        0x00A0, 0x80A5, 0x80AF, 0x00AA, 0x80BB, 0x00BE, 0x00B4, 0x80B1,
        0x8093, 0x0096, 0x009C, 0x8099, 0x0088, 0x808D, 0x8087, 0x0082,
        0x8183, 0x0186, 0x018C, 0x8189, 0x0198, 0x819D, 0x8197, 0x0192,
        0x01B0, 0x81B5, 0x81BF, 0x01BA, 0x81AB, 0x01AE, 0x01A4, 0x81A1,
        0x01E0, 0x81E5, 0x81EF, 0x01EA, 0x81FB, 0x01FE, 0x01F4, 0x81F1,
        0x81D3, 0x01D6, 0x01DC, 0x81D9, 0x01C8, 0x81CD, 0x81C7, 0x01C2,
        0x0140, 0x8145, 0x814F, 0x014A, 0x815B, 0x015E, 0x0154, 0x8151,
        0x8173, 0x0176, 0x017C, 0x8179, 0x0168, 0x816D, 0x8167, 0x0162,
        0x8123, 0x0126, 0x012C, 0x8129, 0x0138, 0x813D, 0x8137, 0x0132,
        0x0110, 0x8115, 0x811F, 0x011A, 0x810B, 0x010E, 0x0104, 0x8101,
        0x8303, 0x0306, 0x030C, 0x8309, 0x0318, 0x831D, 0x8317, 0x0312,
        0x0330, 0x8335, 0x833F, 0x033A, 0x832B, 0x032E, 0x0324, 0x8321,
        0x0360, 0x8365, 0x836F, 0x036A, 0x837B, 0x037E, 0x0374, 0x8371,
        0x8353, 0x0356, 0x035C, 0x8359, 0x0348, 0x834D, 0x8347, 0x0342,
        0x03C0, 0x83C5, 0x83CF, 0x03CA, 0x83DB, 0x03DE, 0x03D4, 0x83D1,
        0x83F3, 0x03F6, 0x03FC, 0x83F9, 0x03E8, 0x83ED, 0x83E7, 0x03E2,
        0x83A3, 0x03A6, 0x03AC, 0x83A9, 0x03B8, 0x83BD, 0x83B7, 0x03B2,
        0x0390, 0x8395, 0x839F, 0x039A, 0x838B, 0x038E, 0x0384, 0x8381,
        0x0280, 0x8285, 0x828F, 0x028A, 0x829B, 0x029E, 0x0294, 0x8291,
        0x82B3, 0x02B6, 0x02BC, 0x82B9, 0x02A8, 0x82AD, 0x82A7, 0x02A2,
        0x82E3, 0x02E6, 0x02EC, 0x82E9, 0x02F8, 0x82FD, 0x82F7, 0x02F2,
        0x02D0, 0x82D5, 0x82DF, 0x02DA, 0x82CB, 0x02CE, 0x02C4, 0x82C1,
        0x8243, 0x0246, 0x024C, 0x8249, 0x0258, 0x825D, 0x8257, 0x0252,
        0x0270, 0x8275, 0x827F, 0x027A, 0x826B, 0x026E, 0x0264, 0x8261,
        0x0220, 0x8225, 0x822F, 0x022A, 0x823B, 0x023E, 0x0234, 0x8231,
        0x8213, 0x0216, 0x021C, 0x8219, 0x0208, 0x820D, 0x8207, 0x0202
    ]
