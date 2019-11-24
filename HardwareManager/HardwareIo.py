#!/usr/bin/env python3
import time
import serial
from threading import Lock
from array import array
import binascii
from HardwareManager.HardwareConst import *

class HardwareIO(object):
    def __init__(self, port, baudrate=1000000, timeout=None):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_mutex = Lock()
        # try:
        self.ser = serial.Serial(port=self.port, baudrate=self.baudrate, timeout=self.timeout)
        # except:
            # print("could not open port")
            
    def __del__(self):
        self.close()
    
    def crc16(self, data_blk, data_blk_size, crc_accum=0):
        for j in range(data_blk_size):
            if type(data_blk[j]) is str:
                i = ((crc_accum >> 8) ^ ord(data_blk[j])) & 0xFF
                crc_accum = ((crc_accum << 8) ^ crc_table[i]) % (2 ** 16)
            else:
                i = ((crc_accum >> 8) ^ data_blk[j]) & 0xFF
                crc_accum = ((crc_accum << 8) ^ crc_table[i]) % (2 ** 16)
        return crc_accum

    def close(self):
        if self.ser:
            self.ser.flushInput()
            self.ser.flushOutput()
            self.ser.close()
    
    def __write_serial(self, data):
        self.ser.flushInput()
        self.ser.flushOutput()
        self.ser.write(data)
    
    def __read_response(self, servo_id):
        """
        Protocol version 2
        """
        data = []
        header_length = 7
        try:
            data.extend(self.ser.read(header_length))
            if not data[0:3] == [255, 255, 253]:
                pass
            packet_lenght = (data[6] << 8) | data[5]
            data.extend(self.ser.read(packet_lenght))
        except:
            pass
        calc_crc = self.crc16(data[:len(data)-2], packet_lenght + 5)
        checksum = (data[-1] << 8) | data[-2]
        if not calc_crc == checksum:
            pass
        return data

    def data_parser(self, response, len_servo_id, size):
        data_sliced = []
        temp = 0
        data = response[9:-2]
        # error not checked
        parsed_data=[]
        for i in range(0, len_servo_id):
            data_sliced.append(data[(2+size)*i:(2+size)*(i+1)])
        for j in range(0, len(data_sliced)):
            for k in range(0, size):
                temp = temp + (data_sliced[j][-size+k] << (8 * k))
            id_with_data = (data_sliced[j][0], data_sliced[j][1], temp)
            parsed_data.append(id_with_data)
            temp = 0
        return parsed_data

    # def read(self, servo_id, address, size):
    #     length = 7
    #     address_L = address & 0x00FF
    #     address_H = address >> 8
        # size_L = size & 0x00FF
        # size_H = size >> 8
    #     packet = [255, 255, 253, 0, servo_id, length, 
    #             0, DXL_READ_DATA, address_L, address_H, size_L, size_H]
    #     calc_crc = self.crc16(packet, len(packet))
    #     crc_L = calc_crc & 0x00FF
    #     crc_H = calc_crc >> 8
    #     packet.append(crc_L)
    #     packet.append(crc_H)
    #     packetStr = ''.join([chr(byte) for byte in packet])
    #     packetStr = array('B', packet).tostring()
    #     with self.serial_mutex:
    #         self.__write_serial(packetStr)
    #         data = self.__read_response(servo_id)
    #     return data
    
    # def write(self, servo_id, address, data):
    #     length = 5 + len(data)  # instruction, address, len(data), checksum

    #     length_L = length & 0x00FF
    #     length_H = length >> 8
        
    #     address_L = address & 0x00FF
    #     address_H = address >> 8
    #     packet = [255, 255, 253, 0, servo_id, length_L,length_H, DXL_WRITE_DATA, address_L, address_H]
    #     packet.extend(data)
    #     calc_crc = self.crc16(packet, len(data)+ 10)
    #     crc_L = calc_crc & 0x00FF
    #     crc_H = calc_crc >> 8
    #     # packet: FF  FF  ID LENGTH INSTRUCTION PARAM_1 ... CHECKSUM
    #     packet.append(crc_L)
    #     packet.append(crc_H)
    #     packetStr = ''.join([chr(byte) for byte in packet])
    #     packetStr = array('B', packet).tostring()
    #     with self.serial_mutex:
    #         self.__write_serial(packetStr)
    #         data = self.__read_response(servo_id)
    #     return data

    def sync_write(self, address, size, data):
        data_flattened = []
        for data in data:
            data_flattened.append(data[0])
            for i in range(0, size):
                temp = (data[1] >> (8 * i)) & 0xFF
                data_flattened.append(temp)
        length = 7 + len(data_flattened)
        length_L = length & 0x00FF
        length_H = length >> 8
        address_L = address & 0x00FF
        address_H = address >> 8
        size_L = size & 0x00FF
        size_H = size >> 8
        packet = [255, 255, 253, 0, DXL_BROADCAST_ID, length_L, length_H, DXL_SYNC_WRITE, address_L, address_H, size_L, size_H]
        packet.extend(data_flattened)
        calc_crc = self.crc16(packet, len(packet))
        crc_L = calc_crc & 0x00FF
        crc_H = calc_crc >> 8
        packet.append(crc_L)
        packet.append(crc_H)
        print("packet",packet)
        packetStr = ''.join([chr(byte) for byte in packet])
        packetStr = array('B', packet).tostring()
        with self.serial_mutex:
            self.__write_serial(packetStr)


    def sync_read(self, address, size, servo_ids):
        length = 7 + len(servo_ids)
        length_L = length & 0x00FF
        length_H = length >> 8
        address_L = address & 0x00FF
        address_H = address >> 8
        size_L = size & 0x00FF
        size_H = size >> 8
        packet = [255, 255, 253, 0, DXL_BROADCAST_ID, length_L, length_H, DXL_SYNC_READ, address_L, address_H, size_L, size_H]
        packet.extend(servo_ids)
        calc_crc = self.crc16(packet, len(packet))
        crc_L = calc_crc & 0x00FF
        crc_H = calc_crc >> 8
        packet.append(crc_L)
        packet.append(crc_H)
        packetStr = ''.join([chr(byte) for byte in packet])
        packetStr = array('B', packet).tostring()
        with self.serial_mutex:
            self.__write_serial(packetStr)
            data = self.__read_response(DXL_BROADCAST_ID)
        return data

    def get_model_number(self, servo_ids):
        response = self.sync_read(DXL_MODEL_NUMBER, 2, servo_ids)
        if response:
            pass
        return response

    def get_model_information(self, servo_ids):
        response = self.sync_read(DXL_MODEL_INFORMATION, 4, servo_ids)
        if response:
            pass
        return response

    def get_firmware_version(self, servo_ids):
        response = self.sync_read(DXL_FIRMWARE_VERSION, 1, servo_ids)
        if response:
            pass
        return response

    def get_led(self, servo_ids):
        response = self.sync_read(DXL_LED, 1, servo_ids)
        if response:
            status = self.data_parser(response, len(servo_ids), 1)
        return status

    def get_present_position(self, servo_ids):
        response = self.sync_read(DXL_PRESENT_POSITION,  4, servo_ids)
        if response:
            status = self.data_parser(response, len(servo_ids), 4)
        return status

    def get_IMU(self):
        response = self.sync_read(GYRO_X, 9, [CM_ID])
        if response:
            status =  self.data_parser(response, 1, 9)
        return status

    def get_button(self):
        response = self.sync_read(BUTTON1_STATE, 1, [CM_ID])
        if response:
            status = self.data_parser(response, 1, 1)
        return status

    def get_voltage(self, ids):
        response = self.sync_read(DXL_PRESENT_INPUT_VOLTAGE, 2, ids)
        if response:
            status = self.data_parser(response, len(ids), 2)
        return status

    def set_torque_enable(self, data):
        response = self.sync_write(DXL_TORQUE_ENABLE, 1, data)
        if response:
            pass
        return response

    def set_led(self, data):
        response = self.sync_write(DXL_LED, 1, data)
        if response:
            pass
        return response

    def set_goal_velocity(self, data):
        response = self.sync_write(DXL_GOAL_VELOCITY, 4, data)
        if response:
            pass
        return response

    def set_goal_position(self, data):
        response = self.sync_write(DXL_GOAL_POSITION, 4, data)
        print(response)
        if response:
            pass
        return response